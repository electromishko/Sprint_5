from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthorizationLocators
import data
import pytest

class TestUILoginUser:

    @pytest.mark.parametrize(
        'test_scenario, case_number',
        [
            ['login', 1],
            ['logout', 2]
        ]
    )
    def test_user_login_logout(self, driver, create_user, test_scenario, case_number):
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.EMAIL_FIELD)
        )

        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(create_user[0])
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(create_user[1])
        driver.find_element(*AuthorizationLocators.MAIN_LOGIN_BUTTON).click()

        if case_number == 1:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located(AuthorizationLocators.USER_TEXT)
            )
            user_text = driver.find_element(*AuthorizationLocators.USER_TEXT).text
            avatar_attribute = driver.find_element(*AuthorizationLocators.USER_AVATAR).get_attribute('xmlns')
            assert user_text == 'User.' and avatar_attribute == 'http://www.w3.org/2000/svg'

        elif case_number == 2:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located(AuthorizationLocators.LOGOUT_BUTTON)
            )
            driver.find_element(*AuthorizationLocators.LOGOUT_BUTTON).click()

            create_ad_text = driver.find_element(*AuthorizationLocators.CREATE_AD_BUTTON).text
            assert create_ad_text == 'Разместить объявление'
