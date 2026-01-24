from selenium.webdriver.common.by import By
from app.pages.base_page import BasePage

class QuotesPage(BasePage):
    ITEMS_QUOTE_CLASS_NAME = (By.CLASS_NAME, "quote")
    TEXT_CLASS_NAME = (By.CLASS_NAME, "text")
    AUTHOR_CLASS_NAME = (By.CLASS_NAME, "author")
    TAGS_CLASS_NAME = (By.CLASS_NAME, "tag")

    def scrape_quotes(self):
        quotes_data = []

        for quote in self.driver.find_elements(*self.ITEMS_QUOTE_CLASS_NAME):
            text = quote.find_element(*self.TEXT_CLASS_NAME).text
            author = quote.find_element(*self.AUTHOR_CLASS_NAME).text
            tags = [
                tag.text
                for tag in quote.find_elements(*self.TAGS_CLASS_NAME)
            ]

            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

        return quotes_data
