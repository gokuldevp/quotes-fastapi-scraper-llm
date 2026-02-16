import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "quotes.json")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")

BASE_URL = os.getenv("BASE_URL")

WIDTH = int(os.getenv("WIDTH", 1920))
HEIGHT = int(os.getenv("HEIGHT", 1080))
TIMEOUT = int(os.getenv("TIMEOUT", 10))
RETRY_COUNT = int(os.getenv("RETRY_COUNT", 3))

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

USERNAME = os.getenv("SCRAPER_USERNAME")
PASSWORD = os.getenv("SCRAPER_PASSWORD")

GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("MODEL", "gemini-2.5-flash-lite")
SYSTEM_PROMPT = """
You are a helpful assistant that summarizes quotes from the website 'Quotes to Scrape'.
You are provided with a list of quotes found on a webpage.
Your task is to extract the quotes and their authors, and return them in a structured JSON format.
The JSON should be an array of objects, where each object has the following structure:
{
    "quote": text,
    "author": author,
    "tags": [tag1, tag2, ...]
}
"""
