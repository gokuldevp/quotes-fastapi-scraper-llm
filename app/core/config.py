import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "quotes.json")

BASE_URL = str(os.getenv("BASE_URL"))

WIDTH = int(os.getenv("WIDTH"))
HEIGHT = int(os.getenv("HEIGHT"))
HEADLESS = bool(os.getenv("HEADLESS"))
TIMEOUT = int(os.getenv("TIMEOUT"))
RETRY_COUNT = int(os.getenv("RETRY_COUNT"))

USERNAME = os.getenv("SCRAPER_USERNAME")
PASSWORD = os.getenv("SCRAPER_PASSWORD")
