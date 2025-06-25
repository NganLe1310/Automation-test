from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.base_test import BaseTest
import time

class LoginPage():
    __init__(self, driver):
    self.driver = driver
    self.username_input = (By.NAME, "username")
    self.password_input = (By.NAME, "password")
    self.login_btn = (By.XPATH, "//button[@type="submit"]")
    def do_login(self, username="Admin", password="admin123"):
        enter_username(username)
        enter_password(password)
        click_login()
        # self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        # self.driver.find_element(By.NAME, "password").send_keys(password)
        # self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        # self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name")))
        # time.sleep(10)

    def enter_username(self, username):
        username = driver.find_element(*self.username_input)
        username.send_keys(username)
    def enter_password(self, password):
        password = driver.find_element(*self.password_input)
        password.send_keys(password)
    def click_login(self):
        driver.find_element(*self.login_btn).click()
