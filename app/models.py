from typing import Dict, List, Literal, Optional
from pydantic import BaseModel

from app.vendors import VendorInput, VendorOutput

class CompletationRequest(VendorInput):
    vendor: str

class CompletationResponse(VendorOutput):
    id: str