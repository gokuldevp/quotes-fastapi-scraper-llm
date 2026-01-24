from fastapi import APIRouter
from app.services.quote_scraper import QuoteScraper

router = APIRouter()

@router.post("/refresh")
def refresh_quotes():
    scraper = QuoteScraper()
    quotes = scraper.run()

    return {
        "count": len(quotes),
        "source": "scraped"
    }
