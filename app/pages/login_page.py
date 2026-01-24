from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.pages.base_page import BasePage
from app.core.config import TIMEOUT

class LoginPage(BasePage):
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.XPATH, '//input[@value="Login"]')
    LINK_LOGOUT = (By.LINK_TEXT, "Logout")

    def go_to_login_page(self):
        self.open_url()
        self.driver.find_element(*self.LINK_LOGIN).click()
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def login(self, username, password):
        self.go_to_login_page()
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(username)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        self.wait.until(EC.presence_of_element_located(self.LINK_LOGOUT))

