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
