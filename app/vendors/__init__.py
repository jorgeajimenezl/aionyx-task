from typing import Dict, List
from .base import VendorInput, VendorOutput, Vendor

# Vendors
from .openai import OpenAI, AzureOpenAI
from .anthropic import Anthropic

# Few examples of vendors
VENDORS_CLS: List[Vendor] = [
    OpenAI,
    AzureOpenAI,
    Anthropic,
]

AVAIlABLE_VENDORS: Dict[str, type] = {vendor.name: vendor for vendor in VENDORS_CLS}
