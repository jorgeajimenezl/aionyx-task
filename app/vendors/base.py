import abc
from typing import Optional
from pydantic import BaseModel, Field


class VendorInput(BaseModel):
    model: str = Field(..., description="Model name to use.")
    prompt: str = Field(..., description="The prompt to pass into the model.")

    temperature: Optional[float] = Field(
        None, description="What sampling temperature to use."
    )
    max_tokens: Optional[int] = Field(
        None, ge=0, description="The maximum number of tokens to generate."
    )


class VendorOutput(BaseModel):
    response: str = Field(..., description="The response from the model.")


class Vendor(abc.ABC):
    name: str = Field(..., description="The name of the vendor.")

    @abc.abstractmethod
    def completation(self, input: VendorInput) -> VendorOutput:
        pass
