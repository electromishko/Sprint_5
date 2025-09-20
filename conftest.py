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
def create_user(driver, login=None, password=None):
    if not login:
        login = faker.email()
    if not password:
        password = faker.password()
    
    driver.get(data.web_link)
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.NO_ACCOUNT_BUTTON)
    )
    driver.find_element(*AuthorizationLocators.NO_ACCOUNT_BUTTON).click()
    
    driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(login)
    driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*AuthorizationLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*AuthorizationLocators.CREATE_ACCOUNT_BUTTON).click()
    
    return [login, password]

@pytest.fixture
def create_ad(driver, create_user):
    driver.get(data.web_link)
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.EMAIL_FIELD)
    )
    
    driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(create_user[0])
    driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(create_user[1])
    driver.find_element(*AuthorizationLocators.MAIN_LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.USER_TEXT)
    )
    
    driver.find_element(*AuthorizationLocators.CREATE_AD_BUTTON).click()
    
    ad_name = faker.text(15)
    driver.find_element(*AuthorizationLocators.AD_NAME_FIELD).send_keys(ad_name)
    
    ad_description = faker.text(45)
    driver.find_element(*AuthorizationLocators.AD_DESCRIPTION_FIELD).send_keys(ad_description)
    driver.find_element(*AuthorizationLocators.AD_PRICE_FIELD).send_keys("11111.11")
    
    driver.find_element(*AuthorizationLocators.CATEGORY_DROPDOWN).click()
    
    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.CATEGORY_OPTION)
    )
    driver.find_element(*AuthorizationLocators.CATEGORY_OPTION).click()
    driver.find_element(*AuthorizationLocators.CONDITION_RADIO).click()
    driver.find_element(*AuthorizationLocators.CITY_DROPDOWN).click()

    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.CITY_OPTION)
    )
    driver.find_element(*AuthorizationLocators.CITY_OPTION).click()

    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.PUBLISH_BUTTON)
    )
    driver.find_element(*AuthorizationLocators.PUBLISH_BUTTON).click()

    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.USER_PROFILE_BUTTON)
    )
    driver.find_element(*AuthorizationLocators.USER_PROFILE_BUTTON).click()

    WebDriverWait(driver, 11).until(
        expected_conditions.visibility_of_element_located(AuthorizationLocators.MY_ADS_SECTION)
    )

    actual_ad_name = driver.find_element(*AuthorizationLocators.AD_ITEM).get_attribute('alt')
    return [actual_ad_name, ad_name]