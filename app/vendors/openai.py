from .base import Vendor, VendorInput, VendorOutput

from langchain_openai import ChatOpenAI, AzureChatOpenAI


class OpenAI(Vendor):
    name = "openai"

    def __init__(self) -> None:
        super().__init__()
        self.model = ChatOpenAI()

    def completation(self, input: VendorInput) -> VendorOutput:
        return VendorOutput(            
            response=self.model.invoke(
                input.prompt, model=input.model, temperature=input.temperature
            ).content
        )


class AzureOpenAI(Vendor):
    name = "azure-openai"

    def __init__(self) -> None:
        super().__init__()
        self.model = AzureChatOpenAI()

    def completation(self, input: VendorInput) -> VendorOutput:
        return VendorOutput(
            response=self.model.invoke(
                input.prompt, model=input.model, temperature=input.temperature
            ).content
        )
