from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthorizationLocators

class TestUILoginUser:

    def test_user_login(self, driver, login_user):
        user_text = driver.find_element(*AuthorizationLocators.USER_TEXT).text
        avatar_attribute = driver.find_element(*AuthorizationLocators.USER_AVATAR).get_attribute('xmlns')
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.LOGOUT_BUTTON))

        assert user_text == 'User.' and avatar_attribute == 'http://www.w3.org/2000/svg'
