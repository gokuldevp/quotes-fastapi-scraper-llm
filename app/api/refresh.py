from fastapi import APIRouter
from app.services.quote_scraper import QuoteScraper
from fastapi import HTTPException
from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()

@router.post("/refresh")
def refresh_quotes():
    try:
        scraper = QuoteScraper()
        quotes = scraper.run()
        return {"count": len(quotes), "source": "scraped"}
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to scrape quotes: {str(e)}"
        )
