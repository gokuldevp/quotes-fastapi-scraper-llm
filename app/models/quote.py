from pydantic import BaseModel
from typing import List
from datetime import datetime

class Quote(BaseModel):
    quote: str
    author: str
    tags: List[str]
    cached_at: datetime
