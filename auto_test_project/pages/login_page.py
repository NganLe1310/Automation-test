from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.base_test import BaseTest
import time

class LoginPage(BaseTest):
    def perform_login(self, username="Admin", password="admin123"):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name")))
        time.sleep(10)