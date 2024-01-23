from .base import Vendor, VendorInput, VendorOutput

from langchain_community.chat_models import ChatAnthropic


class Anthropic(Vendor):
    name = "anthropic"

    def __init__(self) -> None:
        super().__init__()
        self.llm = ChatAnthropic()

    def completation(self, input: VendorInput) -> VendorOutput:
        return VendorOutput(            
            response=self.llm.invoke(
                input.prompt,
                model=input.model,
                temperature=input.temperature,
                max_tokens_to_sample=input.max_tokens,
            ).content
        )
