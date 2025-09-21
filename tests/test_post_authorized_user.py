from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import AuthorizationLocators
import data

faker = Faker()

class TestPostUIAuthorizedUser:

    def test_authorized_user_can_create_ad(self, driver, create_user):
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.EMAIL_FIELD))
        
        driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(create_user[0])
        driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(create_user[1])
        driver.find_element(*AuthorizationLocators.MAIN_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.USER_TEXT))

        driver.find_element(*AuthorizationLocators.CREATE_AD_BUTTON).click()

        new_name = faker.text(15)
        driver.find_element(*AuthorizationLocators.AD_NAME_FIELD).send_keys(new_name)

        new_discr = faker.text(45)
        driver.find_element(*AuthorizationLocators.AD_DESCRIPTION_FIELD).send_keys(new_discr)

        driver.find_element(*AuthorizationLocators.AD_PRICE_FIELD).send_keys("23456")
        driver.find_element(*AuthorizationLocators.CATEGORY_DROPDOWN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.CATEGORY_OPTION))
        driver.find_element(*AuthorizationLocators.CATEGORY_OPTION).click()

        driver.find_element(*AuthorizationLocators.CONDITION_RADIO).click()
        driver.find_element(*AuthorizationLocators.CITY_DROPDOWN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.CITY_OPTION))
        driver.find_element(*AuthorizationLocators.CITY_OPTION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.PUBLISH_BUTTON))
        driver.find_element(*AuthorizationLocators.PUBLISH_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.INPUT_SEARCH))

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.USER_PROFILE_BUTTON))
        driver.find_element(*AuthorizationLocators.USER_PROFILE_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            AuthorizationLocators.MY_ADS_SECTION))

        actual_ad_name = driver.find_element(*AuthorizationLocators.AD_ITEM).get_attribute('alt')
        assert actual_ad_name == new_name, f"Expected: {new_name}, but got: {actual_ad_name}"
