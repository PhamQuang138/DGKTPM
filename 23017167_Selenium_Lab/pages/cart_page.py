import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_item_names(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON))
        time.sleep(0.5)
        items = self.find_all(*self.ITEM_NAMES)
        return [item.text.strip() for item in items]

    def click_checkout(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.click(*self.CHECKOUT_BUTTON)
