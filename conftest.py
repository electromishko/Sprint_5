import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AuthorizationLocators
import data

faker = Faker()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def create_user(driver):
    def _create_user(login=None, password=None):
        if not login:
            login = faker.email()
        if not password:
            password = faker.password()
        
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.NO_ACCOUNT_BUTTON)
        )
        driver.find_element(*AuthorizationLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()

        return [login, password]
    return _create_user

@pytest.fixture
def login_user(driver, create_user):
    user_credentials = create_user()

    driver.get(data.web_link)
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.EMAIL_FIELD))

    driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(user_credentials[0])
    driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(user_credentials[1])
    driver.find_element(*AuthorizationLocators.MAIN_LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.USER_TEXT)
    )

    return user_credentials
