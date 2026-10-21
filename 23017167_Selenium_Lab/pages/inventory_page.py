import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_title(self):
        return self.get_text(*self.TITLE)

    def sort_by_option(self, option_value):
        select_elem = Select(self.find(*self.SORT_SELECT))
        select_elem.select_by_value(option_value)
        time.sleep(0.5)

    def get_all_prices(self):
        price_elems = self.find_all(*self.ITEM_PRICES)
        return [float(p.text.replace("$", "")) for p in price_elems]

    def add_product_by_name(self, product_name):
        # Format name for saucedemo button ID
        formatted_name = product_name.lower().replace(" ", "-")
        add_button_id = f"add-to-cart-{formatted_name}"
        self.click(By.ID, add_button_id)

    def get_cart_count(self):
        try:
            return int(self.get_text(*self.CART_BADGE))
        except Exception:
            return 0

    def open_cart(self):
        self.click(*self.CART_LINK)

    def logout(self):
        self.click(*self.BURGER_BUTTON)
        time.sleep(0.5)
        self.click(*self.LOGOUT_LINK)
