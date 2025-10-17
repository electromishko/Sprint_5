from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AuthorizationLocators
import data

faker = Faker()

class TestUICreateUser:

    def test_register_valid_user_succesful(self, driver):
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.NO_ACCOUNT_BUTTON)
        )
        driver.find_element(*AuthorizationLocators.NO_ACCOUNT_BUTTON).click()

        login = faker.email()
        password = faker.password()
        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.USER_TEXT))
        user_text = driver.find_element(*AuthorizationLocators.USER_TEXT).text
        assert user_text == 'User.'

    def test_register_invalid_email_error(self, driver):
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*AuthorizationLocators.NO_ACCOUNT_BUTTON).click()

        login = faker.text(15)  # Невалидный email
        password = faker.password()
        
        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.ERROR_TEXT))
        
        error_text = driver.find_element(*AuthorizationLocators.ERROR_TEXT).text
        assert error_text == 'Ошибка'
        
        assert driver.find_element(*AuthorizationLocators.EMAIL_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert driver.find_element(*AuthorizationLocators.PASSWORD_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'

    def test_register_existing_user_error(self, driver):
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.NO_ACCOUNT_BUTTON)
        )
        driver.find_element(*AuthorizationLocators.NO_ACCOUNT_BUTTON).click()
       
        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(data.EXISTING_USER['email'])
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(data.EXISTING_USER['password'])
        driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_FIELD).send_keys(data.EXISTING_USER['password'])
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.ERROR_TEXT)
        )
        
        error_text = driver.find_element(*AuthorizationLocators.ERROR_TEXT).text
        assert error_text == 'Ошибка'
        
        assert driver.find_element(*AuthorizationLocators.EMAIL_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert driver.find_element(*AuthorizationLocators.PASSWORD_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
        assert driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_CONTAINER).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'цвет ошибки поля'
