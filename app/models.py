from pydantic import Field

from app.vendors import VendorInput, VendorOutput

class CompletationRequest(VendorInput):
    vendor: str = Field(..., description="The name of the vendor.")

class CompletationResponse(VendorOutput):
    id: str = Field(..., description="The id this specific completation.")