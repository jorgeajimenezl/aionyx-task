from .base import Vendor, VendorInput, VendorOutput

from langchain_community.chat_models import ChatAnthropic


class Anthropic(Vendor):
    name = "anthropic"

    def __init__(self) -> None:
        super().__init__()
        self.model = ChatAnthropic()

    def completation(self, input: VendorInput) -> str:
        return VendorOutput(            
            response=self.model.invoke(
                input.prompt, model=input.model, temperature=input.temperature
            ).content
        )
