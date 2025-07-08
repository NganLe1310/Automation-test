import pytest
import allure
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.configReader import ImportJson 
from pages.dashboard_page import DashboardPage
class TestLogin(BaseTest):
    @allure.title("Login successfully")
    @allure.description("Valid username and password should log in successfully.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        username, password = ImportJson.read_credentials("testsetting.json")
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        DashboardPage(self.driver).wait_for_dashboard_to_load()