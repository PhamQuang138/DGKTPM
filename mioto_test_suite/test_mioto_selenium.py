"""
KỊCH BẢN KIỂM THỬ TỰ ĐỘNG GIAO DIỆN E2E CHO HỆ THỐNG MIOTO.VN
Sinh viên thực hiện: Phạm Duy Quang - MSSV: 23017167
Môn: Đảm bảo Chất lượng và Kiểm thử Phần mềm
Công nghệ: Python 3 + Selenium WebDriver
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MiotoE2ETestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.base_url = "https://www.mioto.vn"

    def test_01_verify_homepage_title(self):
        """TC-UI-01: Kiểm tra tiêu đề Trang chủ Mioto"""
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Mioto", driver.title)
        print("\n[PASSED] TC-UI-01: Trang chủ tải thành công, Title hợp lệ.")

    def test_02_search_city_direct(self):
        """TC-UI-02: Điều hướng đến trang danh sách xe TP. Hồ Chí Minh"""
        driver = self.driver
        driver.get(f"{self.base_url}/city/hochiminh")
        self.assertIn("hochiminh", driver.current_url)
        print("[PASSED] TC-UI-02: Điều hướng trực tiếp tới trang xe TP.HCM thành công.")

    def test_03_verify_car_listings_rendered(self):
        """TC-UI-03: Kiểm tra các phần tử danh sách xe được hiển thị trên giao diện"""
        driver = self.driver
        driver.get(f"{self.base_url}/city/hochiminh")
        time.sleep(3)
        car_items = driver.find_elements(By.CSS_SELECTOR, ".item-car, .car-item, div[class*='item-car']")
        self.assertGreater(len(car_items), 0, "Danh sách xe không được rỗng")
        print(f"[PASSED] TC-UI-03: Danh sách xe hiển thị thành công ({len(car_items)} xe).")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("\n[INFO] Đã hoàn thành thực thi toàn bộ kịch bản kiểm thử tự động UI.")

if __name__ == "__main__":
    unittest.main()

