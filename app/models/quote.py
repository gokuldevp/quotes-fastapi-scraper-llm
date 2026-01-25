from pydantic import BaseModel
from typing import List
from datetime import datetime

class Quote(BaseModel):
    """Data model for a quote."""
    quote: str
    author: str
    tags: List[str]
    cached_at: datetime
