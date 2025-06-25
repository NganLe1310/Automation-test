from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(BaseTest):
    def test_valid_login():    
        login_page = LoginPage(self.driver)
        login_page.do_login()
