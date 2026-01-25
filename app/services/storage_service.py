import json
import os
from app.core.config import DATA_FILE

class StorageService:
    """Service to handle storage of quotes"""
    
    @staticmethod
    def save(quotes: list[dict]):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(quotes, f, indent=2)

    @staticmethod
    def load() -> list[dict]:
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)