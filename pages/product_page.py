from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        product_link.click()
        self.solve_quiz_and_get_code()

    def should_be_the_same_name(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, 'div.product_main h1').text
        basket_name = self.browser.find_element(By.CSS_SELECTOR, 'div.alertinner strong').text
        assert product_name == basket_name, 'Product name and name in basket do not match'

    def should_be_the_same_price(self):
        product_price = self.browser.find_element(By.CSS_SELECTOR, 'div.product_main p.price_color').text
        basket_price = self.browser.find_element(By.CSS_SELECTOR, 'div.alertinner p strong').text
        assert product_price == basket_price, 'Product price and price in basket do not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

