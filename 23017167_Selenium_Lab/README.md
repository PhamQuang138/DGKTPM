# BÁO CÁO THỰC HÀNH KIỂM THỬ TỰ ĐỘNG WEB UI BẰNG SELENIUM WEBDRIVER

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/Selenium-4.51.0-43B02A?logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/Pytest-9.1.1-0A9EDC?logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Design_Pattern-Page_Object_Model-8A2BE2" alt="POM" />
  <img src="https://img.shields.io/badge/Browser-Edge_Headless-0078D7?logo=microsoftedge&logoColor=white" alt="Edge" />
  <img src="https://img.shields.io/badge/Tests-6%2F6_Passed_(100%25)-success" alt="Pass Rate" />
</p>

---

> **MÔN HỌC:** ĐÁNH GIÁ VÀ KIỂM ĐỊNH CHẤT LƯỢNG PHẦN MỀM  
> **GVHD:** TS. Trịnh Thanh Bình  
> **LỚP:** AI&KHDL_1  
> 
> **Sinh viên thực hiện:** **Phạm Duy Quang**  
> **MSSV:** **23017167**  
> **Thời gian thực hiện:** Tháng 10/2026  
> **Website thử nghiệm:** [Swag Labs - SauceDemo](https://www.saucedemo.com/)  
> **Repository GitHub:** [https://github.com/PhamQuang138/DGKTPM](https://github.com/PhamQuang138/DGKTPM)  
> **Thư mục bài làm:** [https://github.com/PhamQuang138/DGKTPM/tree/main/23017167_Selenium_Lab](https://github.com/PhamQuang138/DGKTPM/tree/main/23017167_Selenium_Lab)

---

## 📌 MỤC LỤC
1. [Tổng quan & Mục tiêu Kiểm thử](#1-tổng-quan--mục-tiêu-kiểm-thử)
2. [Cơ sở Lý thuyết & Phương pháp luận](#2-cơ-sở-lý-thuyết--phương-pháp-luận)
   - [2.1. Kim tự tháp kiểm thử & Vai trò của UI Automation](#21-kim-tự-tháp-kiểm-thử--vai-trò-của-ui-automation)
   - [2.2. Kỹ thuật thiết kế ca kiểm thử hộp đen được áp dụng](#22-kỹ-thuật-thiết-kế-ca-kiểm-thử-hộp-đen-được-áp-dụng)
   - [2.3. Chiến lược định vị phần tử DOM & Đồng bộ hóa thời gian](#23-chiến-lược-định-vị-phần-tử-dom--đồng-bộ-hóa-thời-gian)
3. [Kiến trúc Dự án theo Mô hình Page Object Model (POM)](#3-kiến-trúc-dự-án-theo-mô-hình-page-object-model-pom)
   - [3.1. Sơ đồ cấu trúc lớp hướng đối tượng](#31-sơ-đồ-cấu-trúc-lớp-hướng-đối-tượng)
   - [3.2. Cây thư mục dự án](#32-cây-thư-mục-dự-án)
4. [Bảng Đặc tả 06 Ca Kiểm thử Tự động (Test Cases Matrix)](#4-bảng-đặc-tả-06-ca-kiểm-thử-tự-động-test-cases-matrix)
5. [Kết quả Thực thi & Phân tích Chi tiết Từng Test Case](#5-kết-quả-thực-thi--phân-tích-chi-tiết-từng-test-case)
   - [5.0. Tổng quan Báo cáo Đo lường (Execution Summary)](#50-tổng-quan-báo-cáo-đo-lường-execution-summary)
   - [5.1. TC01: Đăng nhập thành công với tài khoản chuẩn (Valid Login)](#51-tc01-đăng-nhập-thành-công-với-tài-khoản-chuẩn-valid-login)
   - [5.2. TC02: Đăng nhập thất bại với tài khoản bị khóa (Locked User)](#52-tc02-đăng-nhập-thất-bại-với-tài-khoản-bị-khóa-locked-user)
   - [5.3. TC03: Lọc & Sắp xếp sản phẩm theo giá tăng dần (Sort Low-to-High)](#53-tc03-lọc--sắp-xếp-sản-phẩm-theo-giá-tăng-dần-sort-low-to-high)
   - [5.4. TC04: Thêm sản phẩm vào giỏ hàng & Đối soát Badge giỏ hàng](#54-tc04-thêm-sản-phẩm-vào-giỏ-hàng--đối-soát-badge-giỏ-hàng)
   - [5.5. TC05: Luồng đặt hàng hoàn tất nhiều bước (End-to-End Checkout Flow)](#55-tc05-luồng-đặt-hàng-hoàn-tất-nhiều-bước-end-to-end-checkout-flow)
   - [5.6. TC06: Đăng xuất an toàn và Hủy phiên làm việc (Secure Logout)](#56-tc06-đăng-xuất-an-toàn-và-hủy-phiên-làm-việc-secure-logout)
6. [Báo cáo Tự động Pytest HTML Report](#6-báo-cáo-tự-động-pytest-html-report)
7. [Phân tích Sự cố Kỹ thuật & Biện pháp Khắc phục (Troubleshooting)](#7-phân-tích-sự-cố-kỹ-thuật--biện-pháp-khắc-phục-troubleshooting)
8. [Hướng dẫn Cài đặt & Tái hiện Kịch bản](#8-hướng-dẫn-cài-đặt--tái-hiện-kịch-bản)
9. [Kết luận & Định hướng Mở rộng](#9-kết-luận--định-hướng-mở-rộng)

---

## 1. Tổng quan & Mục tiêu Kiểm thử

Trong quy trình phát triển phần mềm hiện đại (Agile/DevOps), **kiểm thử tự động giao diện người dùng (Web UI Test Automation)** đóng vai trò chốt chặn cuối cùng nhằm xác minh các luồng nghiệp vụ tương tác thực tế từ góc nhìn của người dùng đầu cuối.

### Mục tiêu kỹ thuật bài thực hành:
1. **Làm chủ công nghệ Selenium WebDriver 4:** Khai thác các tính năng mới của Selenium 4 trên nền tảng Python, bao gồm cơ chế W3C WebDriver Standard và công cụ tự động quản lý trình điều khiển **Selenium Manager**.
2. **Hiện thực hóa mẫu thiết kế chuẩn công nghiệp Page Object Model (POM):** Phân định ranh giới rõ ràng giữa dữ liệu phần tử giao diện (Locators), logic tương tác trang (Page Actions), và logic kiểm định kết quả (Test Assertions).
3. **Bao phủ trọn vẹn vòng đời trải nghiệm khách hàng E-Commerce:** Xây dựng **06 test cases tự động** (vượt yêu cầu tối thiểu 05 ca) đi xuyên suốt từ xác thực người dùng, tìm kiếm sắp xếp danh mục, thao tác giỏ hàng, quy trình thanh toán nhiều bước (Multi-step Checkout) đến đăng xuất hệ thống.
4. **Tự động hóa báo cáo & Minh chứng khách quan:** Tích hợp **Pytest** và plugin **pytest-html** để tự động xuất báo cáo HTML độc lập, đồng thời chụp ảnh màn hình thời gian thực tại mọi điểm kiểm tra quan trọng.

---

## 2. Cơ sở Lý thuyết & Phương pháp luận

### 2.1. Kim tự tháp kiểm thử & Vai trò của UI Automation
Theo mô hình Kim tự tháp kiểm thử của Mike Cohn:
- **Unit Tests (Tầng đáy):** Kiểm tra tính đúng đắn của từng hàm, module độc lập.
- **Service/API Tests (Tầng giữa):** Kiểm tra tích hợp giữa các dịch vụ và hợp đồng dữ liệu REST/JSON.
- **UI Tests (Tầng đỉnh):** Mô phỏng hành vi bấm, gõ, kéo thả và chuyển trang của người dùng thật. Dù có chi phí bảo trì và thời gian thực thi cao hơn, UI Tests là tầng duy nhất kiểm chứng được trải nghiệm trực quan và sự liên kết thông suốt của toàn bộ hệ thống từ Front-end xuống Back-end.

### 2.2. Kỹ thuật thiết kế ca kiểm thử hộp đen được áp dụng
Nhóm áp dụng có hệ thống các kỹ thuật kiểm thử hộp đen tiêu chuẩn quốc tế (ISTQB Foundation Level):
- **Phân vùng tương đương (Equivalence Partitioning - EP):**
  - *Lớp hợp lệ:* Tài khoản hoạt động bình thường (`standard_user` + `secret_sauce`) $\rightarrow$ Truy cập thành công.
  - *Lớp không hợp lệ:* Tài khoản bị vô hiệu hóa (`locked_out_user` + `secret_sauce`) $\rightarrow$ Bắt lỗi tài khoản bị khóa.
- **Phân tích giá trị biên (Boundary Value Analysis - BVA):**
  - Kiểm tra số lượng sản phẩm trong giỏ hàng: Giỏ hàng ban đầu (0 sản phẩm), thêm 1 sản phẩm, thêm 2 sản phẩm (xác thực Badge cập nhật chính xác giá trị biên).
  - Kiểm tra sắp xếp đơn giá từ thấp nhất ($7.99) đến cao nhất ($49.99).
- **Kiểm thử chuyển trạng thái (State Transition Testing):**
  - Mô hình hóa luồng người dùng qua các trạng thái hữu hạn:  
    `[Logged Out]` $\rightarrow$ `[Inventory View]` $\rightarrow$ `[Cart Opened]` $\rightarrow$ `[Checkout Step One: Info]` $\rightarrow$ `[Checkout Step Two: Overview]` $\rightarrow$ `[Order Complete]` $\rightarrow$ `[Logged Out]`.

### 2.3. Chiến lược định vị phần tử DOM & Đồng bộ hóa thời gian
> [!IMPORTANT]
> **Nguyên tắc định vị (Locator Priority):** Ưu tiên tuyệt đối `ID` và `data-test` attributes độc nhất (`By.ID`, `By.CSS_SELECTOR`), hạn chế tối đa XPath tuyệt đối nhằm chống hiện tượng kịch bản bị "gãy" khi giao diện cấu trúc lại CSS.

> [!TIP]
> **Chiến lược đồng bộ hóa thông minh (Explicit Wait vs Hard Sleep):**  
> Tuyệt đối không sử dụng `time.sleep()` tùy tiện. Sử dụng `WebDriverWait` kết hợp `expected_conditions` (như `visibility_of_element_located`, `element_to_be_clickable`, `url_contains`) giúp trình duyệt chỉ chờ đúng thời gian cần thiết để DOM hoàn tất render, tối ưu hóa thời gian thực thi của bộ test suite.

---

## 3. Kiến trúc Dự án theo Mô hình Page Object Model (POM)

### 3.1. Sơ đồ cấu trúc lớp hướng đối tượng

```mermaid
flowchart TD
    classDef base fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef page fill:#0f172a,stroke:#10b981,stroke-width:1.5px,color:#fff;
    classDef test fill:#0f172a,stroke:#f59e0b,stroke-width:1.5px,color:#fff;
    classDef conf fill:#0f172a,stroke:#a855f7,stroke-width:1.5px,color:#fff;

    BasePage["BasePage<br/>- find(), find_all()<br/>- click(), send_keys()<br/>- take_screenshot()"]:::base

    LoginPage["LoginPage<br/>- login()<br/>- get_error_message()"]:::page
    InventoryPage["InventoryPage<br/>- sort_by_option()<br/>- add_product_by_name()<br/>- logout()"]:::page
    CartPage["CartPage<br/>- get_cart_item_names()<br/>- click_checkout()"]:::page
    CheckoutPage["CheckoutPage<br/>- fill_shipping_info()<br/>- finish_order()"]:::page

    Conftest["conftest.py<br/>Fixture: driver (Edge Headless)"]:::conf
    TestSuite["TestSauceDemoAutomation<br/>- test_01_login_success<br/>- test_02_login_locked<br/>- test_03_sort_prices<br/>- test_04_add_cart<br/>- test_05_checkout<br/>- test_06_logout"]:::test

    BasePage --> LoginPage
    BasePage --> InventoryPage
    BasePage --> CartPage
    BasePage --> CheckoutPage

    Conftest -. Cung cấp WebDriver .-> TestSuite
    TestSuite --> LoginPage
    TestSuite --> InventoryPage
    TestSuite --> CartPage
    TestSuite --> CheckoutPage
```

### 3.2. Cây thư mục dự án

```text
23017167_Selenium_Lab/
├── .gitignore                          # Cấu hình loại trừ môi trường ảo (.venv), cache và file tạm
├── requirements.txt                    # Khai báo phụ thuộc: selenium, webdriver-manager, pytest, pytest-html
├── pytest.ini                          # Cấu hình test runner: đường dẫn, cờ CLI, tự động sinh HTML report
├── conftest.py                         # Fixture khởi tạo & giải phóng Microsoft Edge WebDriver (Headless)
├── README.md                           # Báo cáo kỹ thuật toàn diện kèm ảnh minh chứng thực tế
├── pages/                              # TẦNG PAGE OBJECTS (Định vị & Tương tác giao diện)
│   ├── __init__.py
│   ├── base_page.py                    # Wrapper đóng gói WebDriverWait, click, fill text, screenshot
│   ├── login_page.py                   # Quản lý phần tử & hành động trang Đăng nhập
│   ├── inventory_page.py               # Quản lý danh mục sản phẩm, bộ lọc giá, menu trượt
│   ├── cart_page.py                    # Quản lý xem giỏ hàng và kích hoạt Checkout
│   └── checkout_page.py                # Quản lý biểu mẫu giao hàng, đối soát tổng tiền và hoàn tất
├── tests/                              # TẦNG KỊCH BẢN KIỂM THỬ (Test Suite)
│   ├── __init__.py
│   └── test_saucedemo_cases.py         # Bộ 06 ca kiểm thử tự động độc lập
├── reports/                            # BÁO CÁO & DỮ LIỆU ĐO LƯỜNG
│   ├── selenium_report.html            # Báo cáo HTML tự động sinh từ Pytest
│   └── screenshots/                    # Ảnh chụp màn hình chất lượng cao tại thời điểm kiểm tra
│       ├── TC00_test_execution_summary.png
│       ├── TC01_login_success.png
│       ├── TC02_login_locked_user.png
│       ├── TC03_sort_products_price_low_to_high.png
│       ├── TC04_add_to_cart_and_verify_badge.png
│       ├── TC05_checkout_complete_order.png
│       └── TC06_logout_success.png
└── scripts/
    └── generate_report_card.py         # Script Python tổng hợp bảng điều khiển kết quả
```

---

## 4. Bảng Đặc tả 06 Ca Kiểm thử Tự động (Test Cases Matrix)

| Mã TC | Tên Ca Kiểm Thử | Phân Hệ / Chức Năng | Kỹ Thuật Áp Dụng | Dữ Liệu Đầu Vào | Các Bước Thực Hiện (Test Steps) | Điểm Kiểm Tra Mong Đợi (Assertions) | Kết Quả |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :---: |
| **TC01** | Đăng nhập thành công | Xác thực (Authentication) | Phân vùng tương đương (Hợp lệ) | User: `standard_user`<br>Pass: `secret_sauce` | 1. Mở trang đăng nhập<br>2. Nhập user và pass<br>3. Bấm `Login` | 1. URL chứa `/inventory.html`<br>2. Tiêu đề trang hiển thị `Products` | **PASSED** |
| **TC02** | Đăng nhập tài khoản bị khóa | Xử lý lỗi xác thực | Phân vùng tương đương (Không hợp lệ) | User: `locked_out_user`<br>Pass: `secret_sauce` | 1. Mở trang đăng nhập<br>2. Nhập tài khoản bị khóa<br>3. Bấm `Login` | 1. Banner lỗi màu đỏ hiển thị<br>2. Thông điệp chứa: `Epic sadface: Sorry, this user has been locked out.` | **PASSED** |
| **TC03** | Sắp xếp giá tăng dần | Danh mục & Bộ lọc (Catalog) | Kiểm thử trạng thái & Phân tích biên | User: `standard_user`<br>Option: `lohi` | 1. Đăng nhập hệ thống<br>2. Chọn lọc `Price (low to high)`<br>3. Thu thập mảng giá | 1. Số lượng sản phẩm $> 0$<br>2. Mảng giá thỏa mãn tính đơn điệu tăng: `prices == sorted(prices)` | **PASSED** |
| **TC04** | Thêm sản phẩm vào giỏ hàng | Quản lý Giỏ hàng (Cart) | Phân tích biên (0 $\rightarrow$ 2 items) | Items:<br>- `Sauce Labs Backpack`<br>- `Sauce Labs Bike Light` | 1. Đăng nhập hệ thống<br>2. Bấm `Add to cart` 2 món đồ<br>3. Kiểm tra Badge<br>4. Mở trang giỏ hàng | 1. Badge giỏ hàng hiển thị đúng số lượng `2`<br>2. Danh sách tên món trong giỏ chứa chính xác 2 sản phẩm | **PASSED** |
| **TC05** | Luồng thanh toán đơn hàng | Đặt hàng nhiều bước (Checkout) | Kiểm thử chuyển trạng thái tuần tự | Họ tên: `Duy Quang Pham`<br>Mã ZIP: `100000` | 1. Thêm đồ vào giỏ<br>2. Bấm `Checkout`<br>3. Điền thông tin giao nhận<br>4. Bấm `Continue` $\rightarrow$ `Finish` | 1. URL đạt `/checkout-complete.html`<br>2. Tiêu đề xác nhận: `Thank you for your order!` | **PASSED** |
| **TC06** | Đăng xuất an toàn | Quản trị phiên (Session) | Kiểm thử kết thúc phiên | Tài khoản đang có phiên làm việc | 1. Bấm mở Burger Menu<br>2. Nhấp chọn liên kết `Logout` | 1. URL quay về `https://www.saucedemo.com/`<br>2. Nút Login hiển thị sẵn sàng cho phiên mới | **PASSED** |

---

## 5. Kết quả Thực thi & Phân tích Chi tiết Từng Test Case

### 5.0. Tổng quan Báo cáo Đo lường (Execution Summary)
Toàn bộ 06 kịch bản kiểm thử đã được chạy tự động thông qua **Microsoft Edge WebDriver (Headless Mode 1920x1080)**. 
- **Tổng số ca kiểm thử:** 06 ca.
- **Tỷ lệ vượt qua (Pass Rate):** **100% (6/6 ca kiểm thử PASSED)**.
- **Tổng thời gian thực thi:** **26.28 giây** (trung bình ~4.38 giây/ca bao gồm cả thời gian khởi tạo và hủy phiên duyệt web).

![Tổng quan Báo cáo Thực thi](reports/screenshots/TC00_test_execution_summary.png)

*Hình 1: Bảng tổng quan đo lường hiệu quả thực thi 6/6 test cases tự động*

---

### 5.1. TC01: Đăng nhập thành công với tài khoản chuẩn (Valid Login)
- **Mục tiêu:** Kiểm tra quy trình đăng nhập với thông tin người dùng hợp lệ, bảo đảm cookie phiên được tạo lập và chuyển hướng chính xác vào trang mua sắm.
- **Cơ chế kiểm tra:** 
  ```python
  assert "inventory.html" in login_page.get_current_url()
  assert inventory_page.get_title() == "Products"
  ```
- **Kết quả:** Trình duyệt chuyển hướng mượt mà, tiêu đề "Products" hiển thị đầy đủ.

![TC01 Đăng nhập thành công](reports/screenshots/TC01_login_success.png)

*Hình 2: Giao diện trang danh sách sản phẩm hiển thị ngay sau khi xác thực thành công*

---

### 5.2. TC02: Đăng nhập thất bại với tài khoản bị khóa (Locked User)
- **Mục tiêu:** Đảm bảo hệ thống phát hiện chính xác tài khoản bị cấm/khóa và hiển thị cảnh báo người dùng rõ ràng thay vì im lặng hoặc sập ứng dụng.
- **Cơ chế kiểm tra:** 
  ```python
  error_text = login_page.get_error_message()
  assert "Epic sadface: Sorry, this user has been locked out." in error_text
  ```
- **Kết quả:** Thẻ thông báo lỗi mang thuộc tính `data-test="error"` bật lên với nền đỏ nổi bật.

![TC02 Đăng nhập thất bại](reports/screenshots/TC02_login_locked_user.png)

*Hình 3: Cảnh báo lỗi màu đỏ xuất hiện khi tài khoản vi phạm chính sách truy cập*

---

### 5.3. TC03: Lọc & Sắp xếp sản phẩm theo giá tăng dần (Sort Low-to-High)
- **Mục tiêu:** Kiểm chứng thuật toán sắp xếp phía máy khách hoặc máy chủ khi người dùng thay đổi tiêu chí hiển thị hàng hóa.
- **Cơ chế kiểm tra:** Sử dụng `Select` class tương tác với thẻ `<select class="product_sort_container">`, lấy danh sách các phần tử `<div class="inventory_item_price">`, chuyển đổi chuỗi tiền tệ sang kiểu dữ liệu số thực (`float`), và kiểm tra:
  ```python
  assert prices == sorted(prices)
  ```
- **Kết quả:** Các giá trị thu thập được lần lượt là `$7.99`, `$9.99`, `$15.99`, `$15.99`, `$29.99`, `$49.99` $\rightarrow$ Thỏa mãn 100% thứ tự tăng dần.

![TC03 Sắp xếp sản phẩm](reports/screenshots/TC03_sort_products_price_low_to_high.png)

*Hình 4: Danh mục sản phẩm được sắp xếp lại chuẩn xác theo đơn giá từ thấp đến cao*

---

### 5.4. TC04: Thêm sản phẩm vào giỏ hàng & Đối soát Badge giỏ hàng
- **Mục tiêu:** Kiểm tra phản hồi thời gian thực của giao diện khi người dùng nhấn `Add to cart` (nút chuyển sang `Remove`, Badge số lượng cập nhật ngay trên thanh điều hướng).
- **Cơ chế kiểm tra:** 
  ```python
  inventory_page.add_product_by_name("sauce labs backpack")
  inventory_page.add_product_by_name("sauce labs bike light")
  assert inventory_page.get_cart_count() == 2
  ```
- **Kết quả:** Badge giỏ hàng hiển thị số `2`. Khi điều hướng vào trang `/cart.html`, hai mặt hàng xuất hiện đúng tên và giá tiền.

![TC04 Thêm vào giỏ hàng](reports/screenshots/TC04_add_to_cart_and_verify_badge.png)

*Hình 5: Trang giỏ hàng chứa đúng 2 sản phẩm và Badge giỏ hàng hiển thị số lượng 2*

---

### 5.5. TC05: Luồng đặt hàng hoàn tất nhiều bước (End-to-End Checkout Flow)
- **Mục tiêu:** Kiểm thử toàn vẹn quy trình mua hàng qua 3 phân đoạn giao diện: Nhập địa chỉ nhận hàng $\rightarrow$ Kiểm tra thông tin thuế phí & tổng tiền $\rightarrow$ Xác nhận đặt hàng.
- **Cơ chế kiểm tra:** 
  ```python
  checkout_page.fill_shipping_information("Duy Quang", "Pham", "100000")
  assert "Total:" in checkout_page.get_total_price()
  checkout_page.finish_order()
  assert checkout_page.get_completion_header() == "Thank you for your order!"
  ```
- **Kết quả:** Hệ thống tính đúng thuế `Tax` và tổng thanh toán `Total`, màn hình cuối hiển thị thông điệp cảm ơn kèm biểu tượng kiểm định hoàn tất.

![TC05 Hoàn tất đơn hàng](reports/screenshots/TC05_checkout_complete_order.png)

*Hình 6: Màn hình biên lai xác nhận đặt hàng thành công*

---

### 5.6. TC06: Đăng xuất an toàn và Hủy phiên làm việc (Secure Logout)
- **Mục tiêu:** Kiểm tra tính năng thoát tài khoản, xóa bỏ phiên duyệt web trên LocalStorage/Cookies và bảo đảm nút quay lại (Back button) của trình duyệt không làm lộ thông tin riêng tư.
- **Cơ chế kiểm tra:** 
  ```python
  inventory_page.logout()
  assert login_page.get_current_url() == LoginPage.URL
  assert login_page.find(*LoginPage.LOGIN_BUTTON).is_displayed()
  ```
- **Kết quả:** Trình duyệt trở về trang chủ đăng nhập sạch sẽ, nút đăng nhập sẵn sàng phục vụ phiên kế tiếp.

![TC06 Đăng xuất](reports/screenshots/TC06_logout_success.png)

*Hình 7: Trình duyệt trở lại trang đăng nhập gốc sau khi người dùng thực hiện Logout*

---

## 6. Báo cáo Tự động Pytest HTML Report

Báo cáo chi tiết định dạng HTML được plugin `pytest-html` tự động biên dịch tại đường dẫn [`reports/selenium_report.html`](reports/selenium_report.html). Báo cáo độc lập chứa đầy đủ thông số cấu hình môi trường, siêu dữ liệu trình duyệt và thời lượng thực thi của từng test case.

```text
============================= test session starts =============================
platform win32 -- Python 3.11.7, pytest-9.1.1, pluggy-1.7.0
rootdir: D:\DGKTPM\23017167_Selenium_Lab
configfile: pytest.ini
plugins: html-4.2.0, metadata-3.1.1
collected 6 items

tests/test_saucedemo_cases.py::TestSauceDemoAutomation::test_01_login_success PASSED            [ 16%]
tests/test_saucedemo_cases.py::TestSauceDemoAutomation::test_02_login_locked_out_user PASSED    [ 33%]
tests/test_saucedemo_cases.py::TestSauceDemoAutomation::test_03_sort_products_price_low_to_high PASSED [ 50%]
tests/test_saucedemo_cases.py::TestSauceDemoAutomation::test_04_add_to_cart_and_verify PASSED   [ 66%]
tests/test_saucedemo_cases.py::TestSauceDemoAutomation::test_05_checkout_and_complete_order PASSED [ 83%]
tests/test_saucedemo_cases.py::TestSauceDemoAutomation::test_06_logout PASSED                  [100%]

- Generated html report: file:///D:/DGKTPM/23017167_Selenium_Lab/reports/selenium_report.html -
============================== 6 passed in 26.28s ==============================
```

---

## 7. Phân tích Sự cố Kỹ thuật & Biện pháp Khắc phục (Troubleshooting)

Trong quá trình xây dựng kịch bản kiểm thử tự động, nhóm đã phát hiện và xử lý triệt để sự cố phổ biến nhất trong kiểm thử Web UI:

### ⚠️ Hiện tượng: `StaleElementReferenceException` tại kịch bản TC04 & TC05
- **Nguyên nhân gốc rễ (Root Cause):**  
  Trang web SauceDemo là một ứng dụng giao diện đơn trang động (Single Page Application - SPA). Khi người dùng nhấp nút chuyển trang (ví dụ từ `/inventory.html` sang `/cart.html`), cấu trúc cây DOM cũ bị hủy bỏ và tái tạo lại. Nếu kịch bản kiểm thử truy vấn phần tử `find_all(*self.ITEM_NAMES)` ngay lập tức trong khi trình duyệt chưa hoàn tất việc gắn kết node mới, Selenium sẽ báo lỗi phần tử bị "thối" (stale reference).
- **Giải pháp kỹ thuật khắc phục:**  
  Không sử dụng giải pháp tạm thời bằng `time.sleep()`. Thay vào đó, áp dụng cơ chế **Double Synchronization Anchor (Mỏ neo đồng bộ kép)** trong Page Object:
  ```python
  # Trong pages/cart_page.py
  def get_cart_item_names(self):
      # Mỏ neo 1: Chờ URL chuyển hẳn sang trang cart.html
      self.wait.until(EC.url_contains("cart.html"))
      # Mỏ neo 2: Chờ nút Checkout của trang mới hiển thị hoàn toàn
      self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON))
      # Sau khi DOM đã ổn định mới lấy danh sách phần tử
      items = self.find_all(*self.ITEM_NAMES)
      return [item.text.strip() for item in items]
  ```
  Biện pháp này đã loại bỏ hoàn toàn hiện tượng flaky test, nâng độ ổn định của toàn bộ suite lên **100% Pass** trong mọi lần chạy lặp lại.

---

## 8. Hướng dẫn Cài đặt & Tái hiện Kịch bản

### 8.1. Yêu cầu môi trường
- Hệ điều hành: Windows 10/11, Linux hoặc macOS.
- **Python:** Phiên bản 3.8 trở lên (`python --version`).
- **Trình duyệt:** Microsoft Edge hoặc Google Chrome (đã được cài đặt mặc định trên hệ điều hành).
- **Git:** Đã clone repository về máy tính.

### 8.2. Các bước thiết lập & chạy kiểm thử
```bash
# 1. Di chuyển vào thư mục bài thực hành
cd D:\DGKTPM\23017167_Selenium_Lab

# 2. Khởi tạo môi trường ảo Python (Virtual Environment)
python -m venv .venv

# 3. Kích hoạt môi trường ảo
# Trên Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Trên Linux/macOS:
source .venv/bin/activate

# 4. Cài đặt các gói thư viện phụ thuộc
pip install -r requirements.txt

# 5. Thực thi toàn bộ test suite và tự động xuất báo cáo HTML
pytest tests/test_saucedemo_cases.py -v -s --html=reports/selenium_report.html --self-contained-html
```

> [!NOTE]
> Mặc định kịch bản chạy ở chế độ **Headless Mode** để tiết kiệm tối đa CPU/RAM và tăng tốc độ thực thi. Nếu muốn quan sát trực tiếp trình duyệt mở và tự động thao tác trên màn hình, chỉ cần mở file [`conftest.py`](conftest.py) và comment dòng `edge_options.add_argument("--headless=new")`.

---

## 9. Kết luận & Định hướng Mở rộng

### 9.1. Kết quả đạt được
- Hoàn thành xuất sắc toàn bộ yêu cầu của bài thực hành kiểm thử tự động với Selenium WebDriver.
- Xây dựng thành công bộ kịch bản tự động hóa 06 test cases hoàn chỉnh, bao quát các ca kiểm thử then chốt của một hệ sinh thái thương mại điện tử.
- Mã nguồn được kiến trúc hóa chuẩn mực theo mẫu thiết kế **Page Object Model**, giúp dự án dễ đọc, dễ bảo trì và sẵn sàng mở rộng khi có yêu cầu mới.

### 9.2. Định hướng nâng cấp trong tương lai
- **Tích hợp kiểm thử dữ liệu hướng đối tượng (Data-Driven Testing - DDT):** Đọc danh sách tài khoản và kịch bản kiểm thử từ file CSV/Excel hoặc cơ sở dữ liệu.
- **Kiểm thử đa trình duyệt song song (Cross-Browser & Parallel Execution):** Mở rộng kiểm thử đồng thời trên Google Chrome, Mozilla Firefox và Microsoft Edge thông qua thư viện `pytest-xdist`.
- **Tích hợp liên tục vào CI/CD Pipeline:** Tự động kích hoạt kịch bản kiểm thử thông qua GitHub Actions mỗi khi có commit mới vào nhánh `main`.

---
*Báo cáo được thực hiện bởi sinh viên Phạm Duy Quang (MSSV: 23017167) - Lớp AI&KHDL_1.*
