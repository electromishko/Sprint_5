from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthorizationLocators


class TestUILogoutUser:

    def test_user_logout(self, driver, login_user):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.LOGOUT_BUTTON))
        driver.find_element(*AuthorizationLocators.LOGOUT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.LOGIN_BUTTON)).is_displayed()
