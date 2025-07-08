from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
 
class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_title = (By.XPATH, "//h6[contains(@class, 'oxd-text')]")
    def wait_for_dashboard_to_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.dashboard_title)
        )