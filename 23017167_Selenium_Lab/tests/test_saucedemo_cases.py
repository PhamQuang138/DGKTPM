import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestSauceDemoAutomation:
    """
    Bộ kiểm thử tự động Selenium WebDriver cho hệ thống thương mại điện tử Swag Labs (SauceDemo).
    Bao gồm tối thiểu 05 test cases: Đăng nhập, Sắp xếp/Tìm kiếm, Thêm giỏ hàng, Thanh toán, Đăng xuất.
    """

    def test_01_login_success(self, driver):
        """TC01: Đăng nhập thành công với tài khoản chuẩn và chuyển đến Inventory page"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in login_page.get_current_url(), "URL sau đăng nhập không chính xác"
        assert inventory_page.get_title() == "Products", "Tiêu đề trang sản phẩm không đúng"
        
        # Chụp ảnh minh họa kết quả
        login_page.take_screenshot("TC01_login_success.png")

    def test_02_login_locked_out_user(self, driver):
        """TC02: Đăng nhập thất bại với tài khoản bị khóa và hiển thị lỗi"""
        login_page = LoginPage(driver)

        login_page.open_page()
        login_page.login("locked_out_user", "secret_sauce")

        error_text = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_text, "Thông báo lỗi tài khoản bị khóa không xuất hiện"
        
        login_page.take_screenshot("TC02_login_locked_user.png")

    def test_03_sort_products_price_low_to_high(self, driver):
        """TC03: Lọc và sắp xếp sản phẩm theo giá tăng dần (Price: low to high)"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        # Sắp xếp theo giá từ thấp đến cao (lohi)
        inventory_page.sort_by_option("lohi")
        prices = inventory_page.get_all_prices()

        assert len(prices) > 0, "Không tìm thấy danh sách giá sản phẩm"
        assert prices == sorted(prices), f"Danh sách giá chưa được sắp xếp tăng dần: {prices}"
        
        inventory_page.take_screenshot("TC03_sort_products_price_low_to_high.png")

    def test_04_add_to_cart_and_verify(self, driver):
        """TC04: Thêm sản phẩm vào giỏ hàng và kiểm tra số lượng trên Cart Badge"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        # Thêm 2 sản phẩm vào giỏ hàng
        inventory_page.add_product_by_name("sauce labs backpack")
        inventory_page.add_product_by_name("sauce labs bike light")

        # Kiểm tra Cart Badge tăng lên 2
        assert inventory_page.get_cart_count() == 2, "Số lượng hiển thị trên icon giỏ hàng không đúng"

        # Mở giỏ hàng kiểm tra danh sách sản phẩm
        inventory_page.open_cart()
        cart_items = cart_page.get_cart_item_names()

        assert "Sauce Labs Backpack" in cart_items, "Sauce Labs Backpack không có trong giỏ hàng"
        assert "Sauce Labs Bike Light" in cart_items, "Sauce Labs Bike Light không có trong giỏ hàng"
        
        cart_page.take_screenshot("TC04_add_to_cart_and_verify_badge.png")

    def test_05_checkout_and_complete_order(self, driver):
        """TC05: Thực hiện quy trình Checkout điền thông tin và hoàn tất đơn hàng"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_product_by_name("sauce labs backpack")
        inventory_page.open_cart()

        # Bắt đầu Checkout
        cart_page.click_checkout()

        # Điền thông tin giao hàng
        checkout_page.fill_shipping_information("Duy Quang", "Pham", "100000")

        # Xác nhận tổng tiền hiển thị
        total_text = checkout_page.get_total_price()
        assert "Total:" in total_text, "Không tìm thấy tổng tiền đơn hàng"

        # Hoàn tất đặt hàng
        checkout_page.finish_order()

        complete_header = checkout_page.get_completion_header()
        assert complete_header == "Thank you for your order!", "Không nhận được thông báo đặt hàng thành công"
        
        checkout_page.take_screenshot("TC05_checkout_complete_order.png")

    def test_06_logout(self, driver):
        """TC06: Đăng xuất khỏi hệ thống và quay trở lại màn hình Đăng nhập"""
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        # Thực hiện Logout
        inventory_page.logout()

        # Kiểm tra đã quay về trang đăng nhập
        assert login_page.get_current_url() == LoginPage.URL, "Chưa quay về trang đăng nhập sau khi Logout"
        assert login_page.find(*LoginPage.LOGIN_BUTTON).is_displayed(), "Nút đăng nhập không hiển thị sau Logout"
        
        login_page.take_screenshot("TC06_logout_success.png")

