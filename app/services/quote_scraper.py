from app.services.browser_manager import BrowserManager
from app.services.login_service import LoginService
from app.pages.quotes_page import QuotesPage
from app.services.storage_service import StorageService
from app.core.cache import QuoteCache
from app.core.logger import get_logger
from app.core.config import RETRY_COUNT

logger = get_logger(__name__)

class QuoteScraper:
    """Service to scrape quotes from the website."""
    def run(self):
        with BrowserManager() as driver:
            logger.info("Browser started")

            login_service = LoginService(driver)
            login_service.login(RETRY_COUNT)

            quotes_page = QuotesPage(driver)
            quotes = quotes_page.scrape_quotes()

            StorageService.save(quotes)
            QuoteCache.set_quotes(quotes)

            logger.info("Scraping completed")
            return quotes
