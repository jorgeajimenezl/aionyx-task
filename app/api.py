from typing import List

from dotenv import load_dotenv, find_dotenv
from fastapi import Body, FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
import uuid
import lru
import os
import json

from app.models import (
    CompletationRequest,
    CompletationResponse,
)

from app.vendors import Vendor, AVAIlABLE_VENDORS

load_dotenv(find_dotenv())

app = FastAPI(
    title="Aionyx Task",
    version="1.0",
    description="Development of a Middleware API for AI Models",
)

with open("app/data/example_request.json") as f:
    example_request = json.load(f)

pool = lru.LRU(os.getenv("MODELS_POOL_SIZE", 10))


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


@app.post("/completation", response_model=CompletationResponse, tags=["Completations"])
def completation(body: CompletationRequest = Body(..., example=example_request)):
    """
    Completation endpoint
    """
    if body.vendor not in AVAIlABLE_VENDORS:
        raise HTTPException(
            status_code=404, detail={"error": f"Vendor {body.vendor} not available."}
        )
    
    if body.vendor not in pool:
        vendor_cls = AVAIlABLE_VENDORS[body.vendor]
        pool[body.vendor] = vendor_cls()
    vendor: Vendor = pool[body.vendor]
    id = uuid.uuid4()

    try:
        ret = vendor.completation(body)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail={"error": f"Vendor {body.vendor} failed."}
        ) from e

    # TODO: Cache the response in a database using the id as key
    # TODO: Add all kinda logging

    return {
        "id": id.hex,
        "response": ret.response,
    }


@app.get("/vendors", response_model=List[str], tags=["Vendors"])
def vendors():
    """
    List all the available vendors
    """
    return list(AVAIlABLE_VENDORS.keys())
