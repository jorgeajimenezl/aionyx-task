from .base import Vendor, VendorInput, VendorOutput

from langchain_openai import ChatOpenAI, AzureChatOpenAI


class OpenAI(Vendor):
    name = "openai"

    def __init__(self) -> None:
        super().__init__()
        self.llm = ChatOpenAI()

    def completation(self, input: VendorInput) -> VendorOutput:
        return VendorOutput(
            response=self.llm.invoke(
                input.prompt,
                model=input.model,
                temperature=input.temperature or 0.7,
                max_tokens=input.max_tokens,
            ).content
        )


class AzureOpenAI(Vendor):
    name = "azure-openai"

    def __init__(self) -> None:
        super().__init__()
        self.llm = AzureChatOpenAI()

    def completation(self, input: VendorInput) -> VendorOutput:
        return VendorOutput(
            response=self.llm.invoke(
                input.prompt,
                model=input.model,
                temperature=input.temperature or 0.7,
                max_tokens=input.max_tokens,
            ).content
        )
