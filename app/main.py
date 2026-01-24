from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.health import router as health_router
from app.api.refresh import router as refresh_router
from app.api.quote import router as quote_router
from app.core.logger import setup_logging, get_logger
from app.services.storage_service import StorageService
from app.core.cache import QuoteCache

setup_logging()
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    quotes = StorageService.load()
    if quotes:
        QuoteCache.set_quotes(quotes)
        logger.info(f"Loaded {len(quotes)} quotes from disk into cache")
    else:
        logger.info("No existing quotes.json found on startup")
    yield
    logger.info("Application shutting down")

app = FastAPI(title="Automation Task", lifespan=lifespan)

app.include_router(health_router)
app.include_router(refresh_router)
app.include_router(quote_router)
