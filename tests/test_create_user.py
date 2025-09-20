from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AuthorizationLocators
import data
import pytest

faker = Faker()

class TestUICreateUser:

    @pytest.mark.parametrize(
        'login, password, case_number',
        [
            [faker.ascii_free_email(), faker.password(), 1],
            [faker.text(15), faker.password(), 2],
            ['electro@mail.ru', '666666', 3]
        ]
    )
    def test_user_creation(self, driver, create_user, login, password, case_number):
        driver.get(data.web_link)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(AuthorizationLocators.LOGIN_BUTTON)
        )
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.NO_ACCOUNT_BUTTON)
        )
        driver.find_element(*AuthorizationLocators.NO_ACCOUNT_BUTTON).click()

        if case_number == 3:
            login = create_user[0]
            password = create_user[1]
        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()

        if case_number == 1:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located(AuthorizationLocators.USER_TEXT)
            )
            user_text = driver.find_element(*AuthorizationLocators.USER_TEXT).text
            assert user_text == 'User.'

        elif case_number == 2:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located(AuthorizationLocators.ERROR_TEXT)
            )
            error_text = driver.find_element(*AuthorizationLocators.ERROR_TEXT).text
            assert error_text == 'Ошибка'

            assert driver.find_element(*AuthorizationLocators.EMAIL_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
            assert driver.find_element(*AuthorizationLocators.PASSWORD_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
            assert driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'

        elif case_number == 3:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located(AuthorizationLocators.ERROR_TEXT)
            )
            error_text = driver.find_element(*AuthorizationLocators.ERROR_TEXT).text
            assert error_text == 'Ошибка'

