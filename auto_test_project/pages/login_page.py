from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage  
 
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.XPATH, "//input[@placeholder='Username']")
        self.password_field = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")
 
    def input_username(self, username):
        username_input = self.wait_element(self.username_field)
        username_input.send_keys(username)
       
 
    def input_password(self, password):
        password_input = self.wait_element(self.password_field)
        password_input.send_keys(password)
 
    def click_login_button(self):
        self.click(self.login_button)
   
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()
