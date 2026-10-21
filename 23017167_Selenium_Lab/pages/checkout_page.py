import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_information(self, first_name, last_name, postal_code):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.send_keys(*self.FIRST_NAME_INPUT, first_name)
        self.send_keys(*self.LAST_NAME_INPUT, last_name)
        self.send_keys(*self.POSTAL_CODE_INPUT, postal_code)
        self.click(*self.CONTINUE_BUTTON)

    def get_total_price(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        return self.get_text(*self.SUMMARY_TOTAL)

    def finish_order(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        self.click(*self.FINISH_BUTTON)

    def get_completion_header(self):
        self.wait.until(EC.url_contains("checkout-complete.html"))
        return self.get_text(*self.COMPLETE_HEADER)
