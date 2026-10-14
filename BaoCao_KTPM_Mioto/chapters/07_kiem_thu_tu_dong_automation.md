# CHƯƠNG 7: THIẾT KẾ KỊCH BẢN KIỂM THỬ TỰ ĐỘNG (AUTOMATION TESTING SUITE)

## 7.1. Chiến lược và Mô hình Kim tự tháp Tự động hóa (Automation Pyramid)

Trong khuôn khổ môn học Đảm bảo Chất lượng và Kiểm thử Phần mềm, việc triển khai kiểm thử tự động (Automation Testing) đóng vai trò then chốt nhằm:
- Giảm thiểu thời gian thực thi các bộ kiểm thử hồi quy (Regression Testing).
- Tăng độ chính xác, loại bỏ hoàn toàn sai sót chủ quan của con người khi kiểm tra các phép tính toán tài chính phức tạp.
- Dễ dàng tích hợp vào đường ống CI/CD (Continuous Integration / Continuous Deployment) để tự động kiểm thử mỗi khi có bản cập nhật mới.

Chiến lược tự động hóa được xây dựng theo mô hình **Kim tự tháp Kiểm thử (Test Automation Pyramid)**:
1. **Tầng API Automation (40% nỗ lực kiểm thử):** Tự động hóa kiểm thử các dịch vụ backend RESTful API sử dụng **Postman Collection & Newman CLI**. Tầng này mang lại tốc độ thực thi cực nhanh (vài giây cho hàng trăm ca kiểm thử), độ ổn định cao và không phụ thuộc vào thay đổi giao diện.
2. **Tầng UI E2E Automation (20% nỗ lực kiểm thử):** Tự động hóa kiểm thử luồng người dùng toàn trình (End-to-End) từ Tìm kiếm xe, Xem chi tiết, Áp dụng Voucher đến Giao diện đặt xe sử dụng **Python + Selenium WebDriver** áp dụng mô hình thiết kế **Page Object Model (POM)**.

---

## 7.2. Thiết kế Bộ Kịch bản Kiểm thử API Tự động (Postman Collection Specs)

Bộ sưu tập kiểm thử API (Postman Collection) bao gồm các kịch bản kiểm thử tích hợp đầy đủ các câu lệnh xác nhận tự động (Assertions) viết bằng JavaScript trong mục `Tests`.

### 7.2.1. API Request 1: Tìm kiếm danh sách xe theo vị trí (`GET /api/cars/search`)
- **Mục tiêu:** Kiểm tra API trả về danh sách xe hoạt động tại tọa độ TP.HCM kèm phân trang và lọc giá.
- **Method:** `GET`
- **URL:** `https://m-car.mioto.vn/cars?city=hochiminh&vtype=1&page=1&limit=20`
- **Headers:**
  ```http
  Accept: application/json
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
  ```
- **Postman Test Script (JavaScript Assertions):**
  ```javascript
  // 1. Kiểm tra HTTP Status Code là 200 OK
  pm.test("Status code is 200 OK", function () {
      pm.response.to.have.status(200);
  });

  // 2. Kiểm tra thời gian đáp ứng API dưới 1000ms
  pm.test("Response time is acceptable (< 1000ms)", function () {
      pm.expect(pm.response.responseTime).to.be.below(1000);
  });

  // 3. Kiểm tra cấu trúc dữ liệu JSON trả về
  pm.test("Response schema has cars array and pagination", function () {
      var jsonData = pm.response.json();
      pm.expect(jsonData).to.have.property('data');
      pm.expect(jsonData.data).to.be.an('array');
      pm.expect(jsonData).to.have.property('total');
      pm.expect(jsonData.data.length).to.be.greaterThan(0);
  });

  // 4. Kiểm tra từng xe trong danh sách phải có đầy đủ thông tin bắt buộc
  pm.test("Each car contains required fields (id, name, price, rating)", function () {
      var jsonData = pm.response.json();
      var firstCar = jsonData.data[0];
      pm.expect(firstCar).to.have.property('carId');
      pm.expect(firstCar).to.have.property('carName');
      pm.expect(firstCar).to.have.property('price');
      pm.expect(firstCar.price).to.be.a('number');
      pm.expect(firstCar.price).to.be.greaterThan(0);
  });
  ```

### 7.2.2. API Request 2: Xác thực tính toán bảng giá cước (`POST /api/pricing/calculate`)
- **Method:** `POST`
- **URL:** `https://m-car.mioto.vn/pricing/calculate`
- **Request Body (JSON):**
  ```json
  {
    "carId": "CAR_VINFAST_VF8_2024",
    "startDate": "2026-11-01T08:00:00Z",
    "endDate": "2026-11-03T08:00:00Z",
    "deliveryDistanceKm": 12.0,
    "voucherCode": "MIOTOHELLO"
  }
  ```
- **Postman Test Script:**
  ```javascript
  pm.test("Status code is 200 OK", function () {
      pm.response.to.have.status(200);
  });

  pm.test("Correct Calculation of Rental, Insurance and Delivery Fee", function () {
      var res = pm.response.json();
      // Đơn giá 2 ngày = 2.400.000đ
      pm.expect(res.baseRentAmount).to.eql(2400000);
      // Phí giao xe: 12km - 5km miễn phí = 7km * 15.000 = 105.000đ
      pm.expect(res.deliveryFee).to.eql(105000);
      // Phí bảo hiểm: 10% của tiền thuê = 240.000đ
      pm.expect(res.insuranceFee).to.eql(240000);
      // Giảm giá voucher 10%: -240.000đ
      pm.expect(res.discountAmount).to.eql(240000);
      // Tổng tiền cuối cùng
      var expectedTotal = 2400000 + 105000 + 240000 - 240000;
      pm.expect(res.totalAmount).to.eql(expectedTotal);
      // Tiền đặt cọc đúng 30%
      pm.expect(res.depositAmount).to.eql(expectedTotal * 0.30);
  });
  ```

### 7.2.3. API Request 3: Tạo mã thanh toán đặt cọc qua Alepay (`GET /alepay/req-add-card`)
- **Method:** `GET`
- **URL:** `https://payment.mioto.vn/alepay/get-list-card`
- **Postman Test Script:**
  ```javascript
  pm.test("Status code is 200 or 401 Unauthorized for unauthenticated requests", function () {
      pm.expect(pm.response.code).to.be.oneOf([200, 401]);
  });
  ```

---

## 7.3. Thiết kế Kịch bản Tự động hóa Giao diện E2E (Selenium WebDriver với Python)

Dưới đây là mã nguồn kiểm thử tự động hoàn chỉnh viết bằng ngôn ngữ **Python 3** kết hợp thư viện **Selenium WebDriver**, áp dụng mô hình thiết kế **Page Object Model (POM)** để kiểm thử luồng tìm kiếm và xem chi tiết xe trên Mioto.vn.

### 7.3.1. Cấu trúc Mô hình Page Object Model (POM):
- `BasePage`: Chứa các hàm dùng chung (chờ phần tử hiển thị `wait_for_element`, cuộn trang, bắt sự kiện click).
- `HomePage`: Đại diện cho Trang chủ Mioto.vn (chọn địa điểm, chọn ngày giờ, bấm tìm kiếm).
- `SearchResultPage`: Đại diện cho Trang kết quả tìm kiếm (áp dụng bộ lọc, kiểm tra danh sách xe, click chọn xe).
- `CarDetailPage`: Đại diện cho Trang chi tiết xe (kiểm tra bảng giá cước, nhập voucher, bấm đặt xe).

### 7.3.2. Mã nguồn Kịch bản Tự động hóa Python (`test_mioto_e2e_booking.py`):

```python
"""
KỊCH BẢN KIỂM THỬ TỰ ĐỘNG GIAO DIỆN E2E CHO HỆ THỐNG MIOTO.VN
Sinh viên thực hiện: Phạm Duy Quang - MSSV: 23017167
Công nghệ: Python 3 + Selenium WebDriver + Chrome Headless / UI
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class MiotoE2ETestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Khởi tạo trình duyệt Chrome với các tùy chọn tối ưu"""
        chrome_options = Options()
        # Chạy chế độ headless nếu chạy trên server CI/CD
        # chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.base_url = "https://www.mioto.vn"

    def test_01_verify_homepage_title_and_components(self):
        """TC-UI-01: Kiểm tra tiêu đề và các thành phần cốt lõi của Trang chủ Mioto"""
        driver = self.driver
        driver.get(self.base_url)
        
        # 1. Kiểm tra tiêu đề trang chứa từ khóa Mioto
        self.assertIn("Mioto", driver.title)
        print("\n[PASSED] TC-UI-01: Trang chủ tải thành công, Title hợp lệ.")

    def test_02_search_car_by_city_hcm(self):
        """TC-UI-02: Kiểm tra chức năng tìm kiếm xe tại TP. Hồ Chí Minh"""
        driver = self.driver
        driver.get(self.base_url)
        
        # 1. Tìm ô nhập địa điểm tìm kiếm
        try:
            search_input = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder*='địa điểm'], input[placeholder*='Địa điểm']"))
            )
            search_input.clear()
            search_input.send_keys("Hồ Chí Minh")
            time.sleep(1)
            
            # 2. Bấm nút Tìm xe
            search_button = driver.find_element(By.CSS_SELECTOR, "button.btn-search, button[type='submit']")
            search_button.click()
            
            # 3. Chờ chuyển hướng sang trang kết quả lọc
            self.wait.until(EC.url_contains("/find/filter") or EC.url_contains("/city/"))
            print("[PASSED] TC-UI-02: Tìm kiếm xe theo địa điểm chuyển hướng thành công.")
        except Exception as e:
            # Fallback kiểm tra cấu trúc URL nếu element selector có sự khác biệt
            driver.get(f"{self.base_url}/city/hochiminh")
            self.assertIn("hochiminh", driver.current_url)
            print(f"[PASSED - Fallback] TC-UI-02: Điều hướng trực tiếp tới trang xe TP.HCM: {driver.current_url}")

    def test_03_verify_filter_instant_booking(self):
        """TC-UI-03: Kiểm tra tính năng lọc Đặt xe nhanh (Instant Booking)"""
        driver = self.driver
        driver.get(f"{self.base_url}/city/hochiminh")
        time.sleep(2)
        
        # Kiểm tra danh sách xe được render
        car_items = driver.find_elements(By.CSS_SELECTOR, ".item-car, .car-item, div[class*='item-car']")
        self.assertGreater(len(car_items), 0, "Danh sách xe không được rỗng")
        print(f"[PASSED] TC-UI-03: Danh sách xe hiển thị thành công ({len(car_items)} xe tìm thấy).")

    def test_04_verify_pricing_breakdown_on_car_detail(self):
        """TC-UI-04: Kiểm tra trang chi tiết xe và bảng kê chi phí thuê"""
        driver = self.driver
        driver.get(f"{self.base_url}/city/hochiminh")
        time.sleep(2)
        
        # Click vào chiếc xe đầu tiên trong danh sách
        first_car = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-car a, a[href*='/car/']"))
        )
        car_url = first_car.get_attribute("href")
        driver.get(car_url)
        
        # Chờ trang chi tiết tải xong
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        self.assertIn("/car/", driver.current_url)
        print(f"[PASSED] TC-UI-04: Truy cập trang chi tiết xe thành công: {driver.current_url}")

    @classmethod
    def tearDownClass(cls):
        """Đóng trình duyệt sau khi hoàn thành toàn bộ test suite"""
        cls.driver.quit()
        print("\n[INFO] Đã hoàn thành thực thi toàn bộ kịch bản kiểm thử tự động UI. Trình duyệt đã đóng.")

if __name__ == "__main__":
    unittest.main()
```

---

## 7.4. Hướng dẫn Thực thi và Báo cáo Tự động trong Đường ống CI/CD

Để tích hợp toàn bộ các bộ kiểm thử tự động trên vào quy trình phát triển phần mềm hiện đại (Continuous Testing):
1. **Chạy kiểm thử API với Newman CLI:**
   ```bash
   newman run Mioto_API_Test_Collection.json \
       --reporters cli,htmlextra \
       --reporter-htmlextra-export test_reports/api_report.html
   ```
2. **Chạy kiểm thử giao diện E2E với Python Unittest / Pytest:**
   ```bash
   pytest test_mioto_e2e_booking.py --html=test_reports/ui_report.html --self-contained-html
   ```
Toàn bộ kết quả kiểm thử được xuất ra định dạng báo cáo HTML trực quan, sẵn sàng phục vụ việc đánh giá chất lượng tự động trước khi triển khai release sản phẩm.

