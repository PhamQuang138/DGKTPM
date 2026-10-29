# BỘ KỊCH BẢN KIỂM THỬ TỰ ĐỘNG HỆ THỐNG MIOTO.VN (MIOTO AUTOMATION TEST SUITE)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/Postman-API_Collection-FF6C37?logo=postman&logoColor=white" alt="Postman" />
  <img src="https://img.shields.io/badge/WhiteBox-100%25_Basis_Paths-brightgreen" alt="Basis Path Coverage" />
  <img src="https://img.shields.io/badge/Target-Mioto.vn-orange" alt="Mioto.vn" />
</p>

---

## 📌 1. Giới thiệu Tổng quan
Thư mục này chứa toàn bộ mã nguồn kịch bản kiểm thử tự động (Automation Testing Suites) được xây dựng và áp dụng cho hệ thống nền tảng chia sẻ xe ô tô tự lái **Mioto.vn**, bao gồm:
1. **Kiểm thử hộp trắng (White-box Testing):** Kiểm thử độ bao phủ 100% đường đi cơ sở (Basis Path Testing) theo đồ thị dòng điều khiển (CFG) cho thuật toán cốt lõi tính toán giá thuê và tiền cọc.
2. **Kiểm thử tự động Web UI (Selenium WebDriver):** Kịch bản E2E kiểm tra tải trang chủ, điều hướng theo địa điểm và xác thực render danh sách xe thời gian thực.
3. **Kiểm thử tự động API (Postman / Newman):** Bộ sưu tập API tests kiểm tra hợp đồng API (RESTful Contract), thời gian đáp ứng và nghiệp vụ tính toán phụ phí.

---

## 📁 2. Cấu trúc Thư mục

```text
mioto_test_suite/
├── test_whitebox_basis_paths.py     # Unit test 7 đường đi cơ sở thuật toán tính giá Mioto
├── test_mioto_selenium.py          # Selenium WebDriver E2E test cho Web UI Mioto.vn
├── Mioto_Postman_Collection.json   # Bộ sưu tập Postman Collection kiểm thử tự động API
├── generate_postman_collection.py  # Script Python khởi tạo và cập nhật Postman Collection
├── requirements.txt                # Thư viện Python phụ thuộc
└── README.md                       # Hướng dẫn chi tiết cài đặt và thực thi
```

---

## ⚙️ 3. Cài đặt Môi trường

Yêu cầu:
- Python 3.10+
- Trình duyệt Google Chrome hoặc Microsoft Edge kèm WebDriver tương ứng.
- Node.js & Newman (nếu chạy kiểm thử tự động API qua dòng lệnh).

Cài đặt các gói phụ thuộc Python:
```bash
pip install -r requirements.txt
```

---

## 🚀 4. Hướng dẫn Chạy Kiểm thử

### 4.1. Chạy Kiểm thử Hộp trắng (Basis Path Testing)
Kiểm tra toàn bộ $V(G) = 7$ đường đi cơ sở độc lập trong thuật toán `calculate_rental_price`:

```bash
# Chạy trực tiếp bằng Python unittest
python test_whitebox_basis_paths.py

# Hoặc chạy thông qua pytest với hiển thị chi tiết (verbose)
pytest test_whitebox_basis_paths.py -v
```

**Kết quả kỳ vọng:**
```text
.......
Ran 7 tests in 0.001s
OK (100% 7/7 Basis Paths Passed)
```

---

### 4.2. Chạy Kiểm thử Giao diện Web UI (Selenium WebDriver)
Tự động khởi chạy trình duyệt Chrome, tương tác với hệ thống Mioto.vn và đối soát DOM:

```bash
python test_mioto_selenium.py
```

**Kịch bản kiểm tra:**
- `test_01_verify_homepage_title`: Tải trang chủ `https://www.mioto.vn`, xác thực Title chứa từ khóa `Mioto`.
- `test_02_search_city_direct`: Điều hướng trực tiếp tới trang danh sách xe khu vực TP.HCM (`/city/hochiminh`).
- `test_03_verify_car_listings_rendered`: Chờ phần tử DOM xe ô tô xuất hiện, đếm số lượng xe hiển thị và xác thực không rỗng.

---

### 4.3. Chạy Kiểm thử Tự động API (Postman & Newman)
Sử dụng Newman để chạy tự động bộ sưu tập API test:

```bash
# Cài đặt Newman (nếu chưa có)
npm install -g newman

# Thực thi bộ kiểm thử API
newman run Mioto_Postman_Collection.json
```

**Các ca kiểm thử tự động API:**
- `GET /cars?city=hochiminh`: Xác thực HTTP 200/404, thời gian phản hồi $< 1500\text{ ms}$, cấu trúc dữ liệu JSON.
- `POST /pricing/calculate`: Kiểm tra tự động các tham số tính tiền thuê, cọc 30%, phụ phí giao xe quá 5km và giảm giá voucher.
