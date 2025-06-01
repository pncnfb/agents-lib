from typing import List
from pydantic import BaseModel

class SingleSourceRes(BaseModel):
    """
    SingleSourceRes
    """
    text: str
    link: str

class WebResponseAugmented(BaseModel):
    """
    WebResponseAugmented
    """
    response: str
    references: List[SingleSourceRes]