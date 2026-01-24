from selenium.webdriver.common.by import By
from app.core.config import BASE_URL, WIDTH, HEIGHT

class BasePage:
    LINK_LOGIN = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(BASE_URL)
        self.driver.set_window_size(WIDTH, HEIGHT)