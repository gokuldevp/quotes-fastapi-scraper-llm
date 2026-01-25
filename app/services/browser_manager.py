from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.core.config import HEADLESS

class BrowserManager:
    """Context manager to handle browser lifecycle."""
    def __enter__(self):
        options = Options()
        if HEADLESS:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver:
            self.driver.quit()
