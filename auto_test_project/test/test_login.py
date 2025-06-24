from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login():
    login_page = LoginPage()
    login_page.perform_login()

    user_dropdown = WebDriverWait(login_page.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    assert user_dropdown.is_displayed()
    

    login_page.quit_driver()