import abc
from typing import Optional
from pydantic import BaseModel

class VendorInput(BaseModel):
    model: str
    prompt: str
    
    temperature: float = 0.7
    max_tokens: int = 250

class VendorOutput(BaseModel):
    response: str

class Vendor(abc.ABC):
    name: str

    @abc.abstractmethod
    def completation(self, input: VendorInput) -> VendorOutput:
        pass