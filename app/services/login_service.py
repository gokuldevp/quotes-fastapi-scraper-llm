from app.pages.login_page import LoginPage
from app.core.config import USERNAME, PASSWORD
from app.core.logger import get_logger
from app.core.screenshot import take_screenshot
from app.core.exceptions import EXPECTED_LOGIN_EXCEPTIONS

logger = get_logger(__name__)

class LoginService:
    """Service to handle login functionality."""
    def __init__(self, driver):
        self.driver = driver
        self.page = LoginPage(driver)

    def login(self, retries: int):
        for attempt in range(1, retries + 1):
            try:
                self.page.login(USERNAME, PASSWORD)
                logger.info("Login successful")
                return
            except EXPECTED_LOGIN_EXCEPTIONS as e:
                take_screenshot(self.driver, prefix=f"login_failed_attempt_{attempt}")
                logger.warning(f"Login attempt {attempt} failed: {e}")

        raise RuntimeError("Login failed after retries")
