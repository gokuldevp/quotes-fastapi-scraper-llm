from selenium.webdriver.common.by import By
from app.pages.base_page import BasePage
from app.services.ai_services import AIService
import json

class QuotesPage(BasePage):
    """Page object for the quotes page."""

    ITEMS_QUOTE_CLASS_NAME = (By.CLASS_NAME, "quote")
    
    ai_service = AIService()

    def scrape_quotes(self):
        quotes_data = []

        # Extract raw text from each quote element
        for quote in self.driver.find_elements(*self.ITEMS_QUOTE_CLASS_NAME):
            quotes_data.append(quote.text)
        
        # Send to AI service (expects a list, returns JSON string)
        ai_response = self.ai_service.generate_quote(quotes_data)
        
        # Parse the AI's JSON string response into Python objects
        parsed_quotes = json.loads(ai_response)
        
        # Return as formatted JSON string
        return parsed_quotes