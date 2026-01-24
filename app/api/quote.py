import random
from fastapi import APIRouter, HTTPException
from app.core.cache import QuoteCache
from app.models.quote import Quote

router = APIRouter()

@router.get("/quote/random", response_model=Quote)
def random_quote():
    if not QuoteCache.has_data():
        raise HTTPException(
            status_code=503,
            detail="No cached quotes available. Trigger /refresh first."
        )

    return random.choice(QuoteCache.get_quotes())
