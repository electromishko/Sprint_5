from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthorizationLocators
import data

class TestPostUINotAuthorizedUser:

    def test_unauthorized_user_cannot_create_ad(self, driver):
        driver.get(data.web_link)
        driver.find_element(*AuthorizationLocators.CREATE_AD_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(AuthorizationLocators.AUTH_REQUIRED_TEXT)
        )

        auth_required_text = driver.find_element(*AuthorizationLocators.AUTH_REQUIRED_TEXT).text
        assert auth_required_text == 'Чтобы разместить объявление, авторизуйтесь'
