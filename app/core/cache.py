from datetime import datetime

class QuoteCache:
    _quotes = []
    _cached_at = None

    @classmethod
    def set_quotes(cls, quotes):
        cls._quotes = quotes
        cls._cached_at = datetime.utcnow().isoformat()

    @classmethod
    def get_quotes(cls):
        return [
            {**q, "cached_at": cls._cached_at} for q in cls._quotes
        ]
    
    @classmethod
    def has_data(cls):
        return len(cls._quotes) > 0