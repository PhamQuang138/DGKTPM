# CHƯƠNG 4: THIẾT KẾ CÁC BỘ CA KIỂM THỬ CHỨC NĂNG CHI TIẾT (FUNCTIONAL TEST CASES)

Chương này trình bày chi tiết toàn bộ các bộ ca kiểm thử chức năng (Functional Test Cases) được thiết kế có hệ thống cho từng phân hệ nghiệp vụ của nền tảng Mioto.vn. Mỗi ca kiểm thử được chuẩn hóa với các trường thông tin: Mã Test Case (ID), Tên ca kiểm thử, Điều kiện tiên quyết (Preconditions), Dữ liệu kiểm thử (Test Data), Các bước thực hiện (Test Steps), Kết quả kỳ vọng (Expected Result), Kỹ thuật kiểm thử áp dụng (EP, BVA, Decision Table, State Transition).

---

## 4.1. Phân hệ 1: Xác thực, Đăng nhập & Định danh KYC Giấy phép lái xe (GPLX)

### 4.1.1. Bảng phân tích Phân vùng tương đương (EP) và Giá trị biên (BVA) cho Form Xác thực:
- **Trường Số điện thoại (SĐT):**
  - Vùng hợp lệ (Valid EP): SĐT Việt Nam 10 chữ số, bắt đầu bằng các đầu số viễn thông hợp lệ (03, 05, 07, 08, 09), ví dụ: `0912345678`.
  - Vùng không hợp lệ (Invalid EP 1): Chứa chữ cái hoặc ký tự đặc biệt, ví dụ: `09123abcde`, `090@#$$123`.
  - Vùng không hợp lệ (Invalid EP 2): Số lượng chữ số không đúng 10 số:
    * Biên BVA: 9 chữ số (ví dụ: `091234567` - Thiếu số).
    * Biên BVA: 11 chữ số (ví dụ: `09123456789` - Thừa số).
    * Biên BVA: Chuỗi rỗng (`""`).
  - Vùng không hợp lệ (Invalid EP 3): Bắt đầu bằng đầu số không hợp lệ tại Việt Nam (ví dụ: `0123456789`, `0012345678`).
- **Trường Mã OTP:**
  - Vùng hợp lệ: Chuỗi đúng 6 chữ số (`123456`), nhập trong vòng 60 giây.
  - Vùng không hợp lệ: Chuỗi < 6 chữ số, chuỗi > 6 chữ số, chuỗi ký tự chữ cái, mã OTP đã hết hạn (>60 giây), mã OTP sai giá trị.
- **Trường Giấy phép lái xe (GPLX):**
  - Vùng hợp lệ: Số GPLX gồm 12 chữ số theo quy chuẩn quốc gia, hạng bằng B1, B2, C, D, E. Ngày cấp trong quá khứ, còn thời hạn hiệu lực (> 30 ngày tính đến ngày thuê). Ảnh chụp 2 mặt rõ nét, không bị lóa hoặc mất góc.
  - Vùng không hợp lệ: Số GPLX rỗng, không đủ 12 chữ số, hạng bằng lái không đủ điều kiện lái ô tô (A1, A2 xe máy), bằng lái đã hết hạn sử dụng, ảnh chụp tải lên mờ, bị che khuất hoặc file sai định dạng (.exe, .pdf > 10MB).

### 4.1.2. Danh sách Ca kiểm thử chi tiết Phân hệ Xác thực & KYC:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-AUTH-01** | Đăng ký tài khoản với SĐT hợp lệ | Người dùng chưa từng đăng ký tài khoản Mioto | SĐT: `0987654321` | 1. Truy cập trang Đăng ký.<br/>2. Nhập SĐT hợp lệ.<br/>3. Bấm nút "Tiếp tục". | Hệ thống thông báo gửi mã OTP thành công, chuyển sang màn hình nhập OTP, hiển thị đồng hồ đếm ngược 60 giây. | EP (Valid) |
| **TC-AUTH-02** | Đăng ký với SĐT chứa ký tự chữ cái | Ở màn hình Đăng ký | SĐT: `0987abc321` | 1. Nhập SĐT chứa chữ cái.<br/>2. Bấm "Tiếp tục". | Nút "Tiếp tục" bị vô hiệu hóa hoặc báo lỗi: "Số điện thoại không đúng định dạng". | EP (Invalid) |
| **TC-AUTH-03** | Đăng ký với SĐT thiếu ký tự (9 chữ số) | Ở màn hình Đăng ký | SĐT: `098765432` (9 số) | 1. Nhập SĐT 9 số.<br/>2. Bấm "Tiếp tục". | Báo lỗi: "Số điện thoại phải bao gồm đúng 10 chữ số". Không gửi OTP. | BVA (Biên dưới) |
| **TC-AUTH-04** | Đăng ký với SĐT thừa ký tự (11 chữ số) | Ở màn hình Đăng ký | SĐT: `09876543210` (11 số) | 1. Nhập SĐT 11 số.<br/>2. Bấm "Tiếp tục". | Hệ thống tự động cắt ở ký tự thứ 10 hoặc báo lỗi không hợp lệ. | BVA (Biên trên) |
| **TC-AUTH-05** | Đăng ký với SĐT đã tồn tại trên hệ thống | Đã có tài khoản Mioto gắn với SĐT này | SĐT: `0912345678` (Đã tồn tại) | 1. Nhập SĐT đã có tài khoản.<br/>2. Bấm "Tiếp tục". | Thông báo lỗi: "Số điện thoại này đã được đăng ký. Vui lòng đăng nhập hoặc chọn Quên mật khẩu". | Nghiệp vụ (Uniqueness) |
| **TC-AUTH-06** | Nhập đúng mã OTP trong thời hạn hiệu lực | Đã nhận mã OTP về SĐT | OTP: `654321` (Còn trong 60s) | 1. Nhập chính xác 6 chữ số OTP.<br/>2. Bấm "Xác nhận". | Hệ thống xác thực thành công, chuyển sang bước "Thiết lập mật khẩu". | EP (Valid) |
| **TC-AUTH-07** | Nhập sai mã OTP | Đang ở bước nhập OTP | OTP nhập: `111111` (Sai) | 1. Nhập mã OTP không khớp.<br/>2. Bấm "Xác nhận". | Báo lỗi: "Mã xác thực không chính xác. Vui lòng thử lại (Còn 4 lần thử)". | EP (Invalid) |
| **TC-AUTH-08** | Nhập mã OTP khi đã hết hạn (>60 giây) | Đã hết thời gian 60 giây | OTP đúng nhưng nhập ở giây thứ 65 | 1. Chờ đồng hồ về 00:00.<br/>2. Nhập mã OTP.<br/>3. Bấm "Xác nhận". | Báo lỗi: "Mã OTP đã hết hiệu lực. Vui lòng bấm 'Gửi lại mã'". | BVA (Thời gian) |
| **TC-AUTH-09** | Nhập sai mã OTP liên tiếp 5 lần | Đang ở bước nhập OTP | Nhập sai 5 lần các mã khác nhau | 1. Nhập mã sai 5 lần liên tiếp. | Hệ thống khóa gửi/xác thực OTP trên SĐT này trong vòng 15 phút để chống Brute-force. | Bảo mật (Rate limit) |
| **TC-AUTH-10** | Thiết lập mật khẩu thỏa mãn chính sách bảo mật | Vừa xác thực OTP thành công | Mật khẩu: `Mioto@2026` | 1. Nhập mật khẩu đủ 8 ký tự, có hoa, thường, số, ký tự đặc biệt.<br/>2. Nhập lại mật khẩu khớp.<br/>3. Bấm "Hoàn tất". | Hệ thống thông báo đăng ký thành công, tự động đăng nhập và chuyển về Trang chủ. | EP (Valid) |
| **TC-AUTH-11** | Thiết lập mật khẩu quá ngắn (< 8 ký tự) | Ở màn hình tạo mật khẩu | Mật khẩu: `Abc1@` (5 ký tự) | 1. Nhập mật khẩu 5 ký tự.<br/>2. Bấm "Hoàn tất". | Báo lỗi: "Mật khẩu phải chứa ít nhất 8 ký tự". Nút bấm bị vô hiệu hóa. | BVA (Biên dưới) |
| **TC-AUTH-12** | Đăng nhập với SĐT và Mật khẩu chính xác | Tài khoản đã kích hoạt | SĐT: `0987654321`, MK: `Mioto@2026` | 1. Truy cập trang Đăng nhập.<br/>2. Nhập SĐT và mật khẩu đúng.<br/>3. Bấm "Đăng nhập". | Đăng nhập thành công, thanh tiêu đề hiển thị tên người dùng và ảnh đại diện, lưu JWT an toàn. | EP (Valid) |
| **TC-AUTH-13** | Đăng nhập sai mật khẩu liên tiếp 5 lần | Tài khoản tồn tại | Nhập sai mật khẩu 5 lần | 1. Nhập sai mật khẩu liên tiếp 5 lần. | Hệ thống tạm khóa tài khoản trong 30 phút hoặc yêu cầu giải mã CAPTCHA để chống tấn công từ điển. | Bảo mật (Anti-brute force) |
| **TC-AUTH-14** | Đăng nhập nhanh qua Google OAuth 2.0 | Người dùng có tài khoản Gmail | Email Google hợp lệ | 1. Bấm nút "Đăng nhập với Google".<br/>2. Chọn tài khoản Google trong popup.<br/>3. Cho phép quyền truy cập cơ bản. | Đăng nhập thành công, hệ thống tự động liên kết email và chuyển về trang trước đó. | Tích hợp bên thứ 3 |
| **TC-AUTH-15** | Tải lên ảnh GPLX hợp lệ và gửi duyệt KYC | Đã đăng nhập tài khoản | Ảnh mặt trước + mặt sau GPLX B2, Số GPLX: `790123456789`, Hạng B2 | 1. Vào mục "Hồ sơ của tôi" -> "Giấy phép lái xe".<br/>2. Tải 2 ảnh GPLX chuẩn.<br/>3. Nhập số và ngày cấp.<br/>4. Bấm "Gửi duyệt". | Hệ thống báo: "Hồ sơ GPLX của bạn đã được gửi thành công và đang chờ xét duyệt trong vòng 24h". Trạng thái đổi thành "Chờ duyệt". | EP (Valid) |
| **TC-AUTH-16** | Tải lên ảnh bằng lái xe máy (Hạng A1/A2) | Đã đăng nhập | Ảnh bằng lái xe máy A1 | 1. Tải ảnh bằng lái xe máy A1.<br/>2. Chọn hạng A1.<br/>3. Bấm "Gửi duyệt". | Báo lỗi: "Chỉ chấp nhận Giấy phép lái xe ô tô hạng B1, B2, C, D, E, FC. Bằng lái xe máy không đủ điều kiện thuê ô tô". | Nghiệp vụ (Business Rule) |
| **TC-AUTH-17** | Nhập số GPLX đã hết hạn sử dụng | Đã đăng nhập | Ngày hết hạn: ngày trong quá khứ | 1. Nhập thông tin bằng lái đã hết hạn.<br/>2. Bấm "Gửi duyệt". | Báo lỗi: "Giấy phép lái xe đã hết hạn sử dụng. Vui lòng cập nhật GPLX còn hiệu lực để tiếp tục". | BVA (Ngày hiệu lực) |

---

## 4.2. Phân hệ 2: Tìm kiếm, Bộ lọc nâng cao & Bản đồ xe (Search & Filter Engine)

### 4.2.1. Phân tích ma trận tìm kiếm & lọc xe:
- **Địa điểm:** Tỉnh/Thành phố lớn (TP.HCM, Hà Nội, Đà Nẵng, Bình Dương, Lâm Đồng,...), Địa điểm cụ thể (Quận 1, Sân bay Tân Sơn Nhất, Sân bay Nội Bài), Bán kính xung quanh tọa độ hiện tại.
- **Thời gian thuê xe:**
  - Thời gian nhận xe: Phải cách thời điểm hiện tại tối thiểu 2 giờ.
  - Thời gian thuê tối thiểu: 24 giờ (1 ngày đối với xe tự lái). Nếu chọn dưới 24h, hệ thống tự động làm tròn thành 1 ngày hoặc báo lỗi.
- **Bộ lọc đa tiêu chí (Multi-filter):**
  - Hãng xe: Toyota, Honda, Hyundai, Kia, Mazda, Ford, VinFast, Mercedes,...
  - Hộp số: Tự động (Automatic), Số sàn (Manual).
  - Nhiên liệu: Xăng (Gasoline), Dầu (Diesel), Điện (EV).
  - Mức giá thuê: Slider lọc giá từ 500.000đ đến 5.000.000đ/ngày.
  - Tiện ích đặc biệt: Giao xe tận nơi, Đặt xe nhanh, Miễn thế chấp.

### 4.2.2. Danh sách Ca kiểm thử chi tiết Phân hệ Tìm kiếm & Lọc xe:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-SRCH-01** | Tìm kiếm xe theo Tỉnh/Thành phố hợp lệ | Đang ở Trang chủ | Địa điểm: "Hồ Chí Minh" | 1. Nhập "Hồ Chí Minh" vào ô tìm kiếm.<br/>2. Chọn gợi ý "Thành phố Hồ Chí Minh, Việt Nam" từ danh sách autocomplete.<br/>3. Bấm "Tìm xe". | Chuyển đến trang danh sách xe `/city/hochiminh` hoặc `/find/filter`, hiển thị toàn bộ xe đang hoạt động tại khu vực TP.HCM. | EP (Valid) |
| **TC-SRCH-02** | Tìm kiếm xe với địa điểm không có trong danh mục | Ở Trang chủ | Địa điểm: "Địa danh không có thật 12345xyz" | 1. Nhập địa danh không tồn tại.<br/>2. Bấm "Tìm xe". | Danh sách gợi ý autocomplete rỗng, hiển thị thông báo: "Không tìm thấy địa điểm phù hợp". | EP (Invalid) |
| **TC-SRCH-03** | Chọn thời gian nhận xe trong quá khứ | Ở bộ chọn thời gian | Ngày nhận: Ngày hôm qua | 1. Mở lịch chọn ngày nhận.<br/>2. Cố gắng chọn ngày trong quá khứ. | Các ngày trong quá khứ bị làm mờ (disabled) và không thể bấm chọn. | BVA (Biên thời gian) |
| **TC-SRCH-04** | Chọn thời gian nhận xe cách hiện tại dưới 2 giờ | Ở bộ chọn thời gian | Hiện tại là 10:00, chọn nhận lúc 10:30 cùng ngày | 1. Chọn ngày hôm nay.<br/>2. Chọn khung giờ 10:30.<br/>3. Bấm "Tìm xe". | Báo lỗi hoặc tự động điều chỉnh: "Thời gian bắt đầu nhận xe phải sau thời điểm hiện tại ít nhất 2 giờ (tối thiểu 12:00)". | BVA (Biên dưới 2h) |
| **TC-SRCH-05** | Chọn thời gian thuê tròn 24 giờ (Hợp lệ) | Ở bộ chọn thời gian | Nhận: 08:00 ngày 20/10<br/>Trả: 08:00 ngày 21/10 | 1. Chọn đúng khoảng cách 24h.<br/>2. Bấm "Tìm xe". | Tìm kiếm thành công, hệ thống tính số ngày thuê là: 1 ngày. | BVA (Biên 24h) |
| **TC-SRCH-06** | Chọn thời gian trả xe trước thời gian nhận xe | Ở bộ chọn thời gian | Nhận: 08:00 ngày 22/10<br/>Trả: 08:00 ngày 20/10 | 1. Chọn ngày trả trước ngày nhận.<br/>2. Bấm xác nhận. | Hệ thống ngăn chặn việc chọn, tự động đẩy ngày trả về sau ngày nhận ít nhất 1 ngày. | Ràng buộc logic |
| **TC-SRCH-07** | Lọc xe theo loại hộp số: Tự động (Automatic) | Đang ở trang danh sách kết quả tìm kiếm | Bộ lọc Hộp số: "Số tự động" | 1. Tích chọn checkbox "Số tự động".<br/>2. Quan sát danh sách xe. | 100% các xe hiển thị trong danh sách đều có thông số hộp số là "Số tự động". Không có xe số sàn nào xuất hiện. | EP (Filter) |
| **TC-SRCH-08** | Lọc kết hợp đa tiêu chí (Hãng xe + Hộp số + Nhiên liệu) | Đang ở trang danh sách xe | Hãng: "VinFast", Hộp số: "Tự động", Nhiên liệu: "Điện" | 1. Tích chọn hãng "VinFast".<br/>2. Tích chọn "Số tự động".<br/>3. Tích chọn nhiên liệu "Điện". | Danh sách chỉ trả về các dòng xe điện VinFast (VF e34, VF8, VF9, VF5). Số lượng xe khớp hiển thị chính xác trên tiêu đề. | Tổ hợp điều kiện |
| **TC-SRCH-09** | Lọc xe theo khoảng giá (Slider min - max) | Đang ở trang danh sách xe | Giá từ: 800.000đ đến 1.200.000đ/ngày | 1. Kéo thanh slider giá min lên 800k, max xuống 1tr2.<br/>2. Kiểm tra đơn giá các xe hiển thị. | Tất cả xe trả về đều có đơn giá nằm nghiêm ngặt trong khoảng từ 800.000đ đến 1.200.000đ/ngày. | BVA (Khoảng giá) |
| **TC-SRCH-10** | Lọc xe có tính năng "Đặt xe nhanh" (Instant Booking) | Đang ở trang danh sách xe | Tích chọn "Đặt xe nhanh" | 1. Kích hoạt bộ lọc "Đặt xe nhanh". | Toàn bộ xe hiển thị đều có biểu tượng tia sét màu xanh (Instant Booking - Không cần chủ xe phê duyệt thủ công). | EP (Tính năng) |
| **TC-SRCH-11** | Lọc xe có tiện ích "Miễn thế chấp tiền mặt / xe máy" | Đang ở trang danh sách xe | Tích chọn "Miễn thế chấp" | 1. Bật bộ lọc "Miễn thế chấp". | Danh sách chỉ hiển thị các xe có chính sách chấp nhận CCCD gắn chip thay thế cho việc giữ xe máy hoặc cọc 15 triệu tiền mặt. | Nghiệp vụ P2P |
| **TC-SRCH-12** | Đổi chế độ xem Danh sách sang Bản đồ số (Map View) | Đang ở trang tìm kiếm | Chuyển tab "Bản đồ" | 1. Bấm vào nút chuyển đổi "Xem bản đồ". | Giao diện hiển thị bản đồ HERE Maps với các pin đánh dấu vị trí và giá thuê của từng xe tại tọa độ tương ứng. Khi di chuột/bấm vào pin sẽ hiển thị popup tóm tắt xe. | Giao diện & Tương thích |

---

## 4.3. Phân hệ 3: Chi tiết xe, Bảng giá cước & Khuyến mãi (Pricing & Promotion Engine)

### 4.3.1. Bảng Quyết định (Decision Table) cho Thuật toán Tính toán Bảng giá cước:
Thuật toán tính toán tổng tiền thuê xe $T$ của Mioto dựa trên các điều kiện sau:
- **C1: Loại ngày thuê:** Ngày thường (Thứ 2 - Thứ 6) hay Ngày cuối tuần (T7, CN) hay Ngày Lễ/Tết.
- **C2: Giao xe tận nơi:** Khách tự đến nhận tại bãi xe ($d = 0$) hay Giao tận nơi trong phạm vi $\le 5$km hay Giao tận nơi $> 5$km.
- **C3: Mã giảm giá (Voucher):** Không áp dụng / Áp dụng mã hợp lệ / Áp dụng mã không đủ điều kiện.
- **C4: Bảo hiểm chuyến đi:** Tự động áp dụng gói bảo hiểm MIC/VNI (tỷ lệ 10% đơn giá thuê).

**Bảng Quyết định Tính giá:**

| Điều kiện / Hành động | Quy tắc 1 (R1) | Quy tắc 2 (R2) | Quy tắc 3 (R3) | Quy tắc 4 (R4) | Quy tắc 5 (R5) | Quy tắc 6 (R6) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **C1: Loại ngày thuê** | Ngày thường | Cuối tuần | Ngày Lễ/Tết | Ngày thường | Cuối tuần | Ngày thường |
| **C2: Giao xe tận nơi** | Nhận tại bãi ($d=0$) | Trong bán kính $\le 5$km | Khoảng cách $d > 5$km | Nhận tại bãi ($d=0$) | Khoảng cách $d > 5$km | Khoảng cách $d > 5$km |
| **C3: Mã voucher** | Không dùng | Không dùng | Không dùng | Dùng mã -10% | Dùng mã -100k | Dùng mã hết hạn |
| **A1: Phụ phí ngày thuê** | 0đ | +15% đơn giá | +30% đơn giá | 0đ | +15% đơn giá | 0đ |
| **A2: Phí giao xe** | 0đ | 0đ (Miễn phí) | $(d - 5) \times 15.000$đ | 0đ | $(d - 5) \times 15.000$đ | $(d - 5) \times 15.000$đ |
| **A3: Phí bảo hiểm** | 10% đơn giá | 10% đơn giá | 10% đơn giá | 10% đơn giá | 10% đơn giá | 10% đơn giá |
| **A4: Mức giảm voucher** | 0đ | 0đ | 0đ | Giảm 10% giá gốc | Giảm 100.000đ | 0đ (Báo lỗi mã) |
| **A5: Tính tiền cọc (30%)** | $30\% \times \text{Tổng}$ | $30\% \times \text{Tổng}$ | $30\% \times \text{Tổng}$ | $30\% \times \text{Tổng}$ | $30\% \times \text{Tổng}$ | $30\% \times \text{Tổng}$ |

### 4.3.2. Danh sách Ca kiểm thử chi tiết Phân hệ Tính giá & Khuyến mãi:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-PRIC-01** | Tính giá ngày thường, nhận tại bãi, không voucher (Quy tắc R1) | Chọn xe có giá niêm yết 1.000.000đ/ngày | Thuê 2 ngày thường (Thứ 3 - Thứ 5). Giao nhận tại chỗ ($d=0$). Không voucher. | 1. Chọn xe giá 1.000.000đ.<br/>2. Chọn thuê từ T3 đến T5 (2 ngày).<br/>3. Xem bảng kê chi phí. | - Tiền thuê gốc: 2.000.000đ.<br/>- Phí bảo hiểm chuyến đi (10%): 200.000đ.<br/>- Phí giao xe: 0đ.<br/>- Tổng cộng: 2.200.000đ.<br/>- Tiền cọc 30%: 660.000đ. | Decision Table (R1) |
| **TC-PRIC-02** | Tính giá ngày cuối tuần có phụ phí 15% (Quy tắc R2) | Chọn xe giá 1.000.000đ/ngày thường, cấu hình cuối tuần +15% | Thuê 2 ngày cuối tuần (T7, CN). Giao xe tại nhà cách bãi 4 km ($\le 5$km). | 1. Chọn thuê trọn T7 và CN.<br/>2. Chọn điểm giao xe cách 4km.<br/>3. Kiểm tra chi tiết giá. | - Tiền thuê: $2 \times 1.150.000 = 2.300.000$đ.<br/>- Phí bảo hiểm (10%): 230.000đ.<br/>- Phí giao nhận xe: 0đ (miễn phí $\le 5$km).<br/>- Tổng tiền: 2.530.000đ.<br/>- Tiền cọc 30%: 759.000đ. | Decision Table (R2) / BVA biên 4km |
| **TC-PRIC-03** | Tính phí giao xe vượt mốc 5km (Quy tắc R3) | Chọn xe giá 1.000.000đ/ngày | Khoảng cách giao xe: 12 km ($> 5$km). Đơn giá vượt: 15.000đ/km. Thuê 1 ngày thường. | 1. Nhập địa chỉ giao xe cách 12km.<br/>2. Quan sát dòng "Phí giao nhận xe". | Phí giao xe tính chuẩn: $(12 - 5) \times 15.000 = 105.000$đ.<br/>Tổng tiền = 1.000.000đ (thuê) + 100.000đ (bảo hiểm) + 105.000đ (giao xe) = 1.205.000đ. | Decision Table (R3) / BVA |
| **TC-PRIC-04** | Kiểm tra giá trị biên khoảng cách giao xe: Đúng 5.0 km | Chọn xe có giao tận nơi | Khoảng cách chính xác 5.0 km | 1. Chọn điểm giao xe đúng 5.0km. | Phí giao nhận xe hiển thị: 0đ (Miễn phí trong 5km). | BVA (Biên trên miễn phí) |
| **TC-PRIC-05** | Kiểm tra giá trị biên khoảng cách giao xe: 5.1 km | Chọn xe có giao tận nơi | Khoảng cách chính xác 5.1 km | 1. Chọn điểm giao xe 5.1km. | Phí giao nhận xe tính cho phần vượt: $(5.1 - 5) \times 15.000 = 1.500$đ (hoặc làm tròn theo block 1km tùy cấu hình chủ xe). | BVA (Biên ngoài) |
| **TC-PRIC-06** | Áp dụng mã giảm giá phần trăm hợp lệ (Quy tắc R4) | Chọn xe giá 2.000.000đ cho 2 ngày | Mã voucher: `MIOTOHELLO` (Giảm 10% tối đa 300.000đ) | 1. Nhập mã `MIOTOHELLO`.<br/>2. Bấm "Áp dụng". | Hiển thị thông báo "Áp dụng mã thành công". Dòng khuyến mãi ghi nhận: -200.000đ (10% của 2tr). Tổng tiền giảm trừ chính xác 200.000đ. | Decision Table (R4) |
| **TC-PRIC-07** | Áp dụng mã giảm giá cố định (Quy tắc R5) | Chọn xe bất kỳ | Mã voucher: `BANMOI100` (Giảm trực tiếp 100.000đ) | 1. Nhập mã `BANMOI100`.<br/>2. Bấm "Áp dụng". | Giảm trừ trực tiếp 100.000đ vào tổng thanh toán. Tiền đặt cọc 30% tính lại theo tổng tiền mới. | Decision Table (R5) |
| **TC-PRIC-08** | Áp dụng mã giảm giá đã hết hạn sử dụng (Quy tắc R6) | Có mã voucher đã hết hạn | Mã voucher: `TET2025` (Hết hạn từ 01/03/2025) | 1. Nhập mã đã quá hạn.<br/>2. Bấm "Áp dụng". | Báo lỗi: "Mã khuyến mãi này đã hết hạn sử dụng". Không giảm trừ tiền. | Decision Table (R6) |
| **TC-PRIC-09** | Áp dụng mã giảm giá khi đơn hàng chưa đạt giá trị tối thiểu | Chọn đơn thuê nửa ngày hoặc xe giá thấp 600.000đ | Mã voucher `VIP500` (Yêu cầu đơn hàng tối thiểu 1.500.000đ) | 1. Nhập mã `VIP500`.<br/>2. Bấm "Áp dụng". | Báo lỗi: "Đơn hàng chưa đạt giá trị tối thiểu 1.500.000đ để sử dụng mã này". | Ràng buộc điều kiện (Precondition) |
| **TC-PRIC-10** | Áp dụng đồng thời 2 mã giảm giá trên một đơn hàng | Đã áp dụng thành công mã thứ nhất | Nhập tiếp mã thứ hai | 1. Sau khi áp dụng mã 1, cố gắng nhập tiếp mã 2. | Hệ thống thông báo: "Mỗi chuyến đi chỉ được áp dụng tối đa 1 mã khuyến mãi. Mã mới sẽ thay thế mã cũ". | Nghiệp vụ (Constraint) |

---

## 4.4. Phân hệ 4: Quy trình Đặt xe, Phê duyệt & Đặt cọc (Booking & Deposit Flow)

### 4.4.1. Ma trận Chuyển trạng thái quy trình Đặt cọc:
- **Trạng thái 1: Khởi tạo (Pending Approval):** Khách gửi yêu cầu -> Chờ chủ xe phản hồi trong 60 phút.
  - Sự kiện E1: Chủ xe bấm Chấp nhận -> Chuyển sang Trạng thái 2 (Approved / Waiting Deposit).
  - Sự kiện E2: Chủ xe bấm Từ chối -> Chuyển sang Trạng thái Kết thúc (Rejected).
  - Sự kiện E3: Quá 60 phút không ai tương tác -> Chuyển sang Trạng thái Kết thúc (Expired).
- **Trạng thái 2: Chờ đặt cọc (Waiting Deposit):** Hệ thống cấp 60 phút để khách thanh toán 30% cọc.
  - Sự kiện E4: Khách thanh toán cọc thành công qua cổng thanh toán -> Chuyển sang Trạng thái 3 (Booked/Confirmed).
  - Sự kiện E5: Cổng thanh toán báo lỗi (thẻ hết hạn, không đủ số dư) -> Giữ nguyên trạng thái để khách chọn phương thức khác.
  - Sự kiện E6: Hết 60 phút khách không cọc -> Hủy yêu cầu (Deposit Timeout), giải phóng lịch xe.

### 4.4.2. Danh sách Ca kiểm thử chi tiết Phân hệ Đặt xe & Thanh toán:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-BOOK-01** | Tạo yêu cầu đặt xe thành công (Quy trình thông thường) | Tài khoản đã KYC GPLX hợp lệ, đã đăng nhập | Xe Mazda 3, thuê 3 ngày, tổng cọc 900.000đ | 1. Tại trang chi tiết xe, chọn ngày.<br/>2. Nhập ghi chú cho chủ xe: "Tôi đi công tác Vũng Tàu".<br/>3. Bấm "Gửi yêu cầu đặt xe". | - Tạo thành công bản ghi chuyến đi với trạng thái "Chờ chủ xe duyệt".<br/>- Hiển thị đồng hồ đếm ngược 60 phút.<br/>- Gửi thông báo Push Notification/SMS đến chủ xe. | State Transition (S1 -> S2) |
| **TC-BOOK-02** | Tạo yêu cầu đặt xe khi chưa được duyệt GPLX | Tài khoản mới, chưa tải lên GPLX hoặc GPLX bị từ chối | Chọn xe bất kỳ | 1. Bấm "Gửi yêu cầu đặt xe". | Hệ thống bật popup cảnh báo: "Bạn cần hoàn tất xác thực Giấy phép lái xe trước khi tiến hành đặt xe", kèm nút chuyển hướng đến trang KYC. | Nghiệp vụ (Precondition) |
| **TC-BOOK-03** | Chủ xe phê duyệt yêu cầu trong vòng 60 phút | Có đơn đang ở trạng thái "Chờ duyệt" | Tài khoản Chủ xe | 1. Chủ xe mở ứng dụng/web, vào danh sách yêu cầu.<br/>2. Bấm nút "Chấp nhận". | Đơn chuyển sang trạng thái "Đã duyệt - Chờ thanh toán cọc". Khách thuê nhận thông báo và link thanh toán cọc trong 60 phút. | State Transition (Approved) |
| **TC-BOOK-04** | Chủ xe từ chối yêu cầu đặt xe kèm lý do | Có đơn đang chờ duyệt | Lý do: "Xe bận bảo dưỡng định kỳ" | 1. Chủ xe bấm "Từ chối".<br/>2. Chọn lý do từ danh sách.<br/>3. Bấm xác nhận. | Đơn chuyển trạng thái "Bị từ chối". Gửi thông báo đến khách thuê kèm gợi ý các mẫu xe tương đương lân cận. Lịch xe được mở lại. | State Transition (Rejected) |
| **TC-BOOK-05** | Tự động hủy đơn khi chủ xe không phản hồi sau 60 phút | Đơn ở trạng thái chờ duyệt | Đã qua 60 phút 01 giây | 1. Giả lập thời gian trôi qua quá 60 phút không có thao tác từ chủ xe. | Hệ thống chạy background job chuyển trạng thái đơn sang "Hết hạn phản hồi" (Expired). Gửi thông báo xin lỗi khách hàng. | State Transition (Expired) |
| **TC-BOOK-06** | Luồng "Đặt xe nhanh" (Instant Booking) tự động duyệt | Xe có bật tính năng Instant Booking | Tài khoản khách đã xác thực đầy đủ | 1. Chọn xe có nhãn "Đặt xe nhanh".<br/>2. Bấm "Đặt xe nhanh". | Hệ thống bỏ qua bước chờ chủ xe duyệt, chuyển thẳng đến màn hình thanh toán tiền cọc. | Luồng nghiệp vụ tắt |
| **TC-BOOK-07** | Thanh toán cọc thành công qua Thẻ Quốc tế (Visa/MasterCard qua Alepay) | Đơn ở trạng thái "Chờ thanh toán cọc" | Thẻ Sandbox Visa hợp lệ, đủ số dư (Số thẻ: `4111...1111`) | 1. Chọn phương thức "Thẻ tín dụng/ghi nợ Quốc tế".<br/>2. Nhập thông tin thẻ và OTP 3D-Secure.<br/>3. Bấm xác nhận thanh toán. | Cổng thanh toán trả về mã giao dịch thành công. Đơn chuyển trạng thái "Đã đặt cọc" (Booked). Khóa lịch xe trên hệ thống. | Tích hợp Cổng thanh toán |
| **TC-BOOK-08** | Thanh toán cọc thất bại do Thẻ không đủ số dư | Đang ở cổng thanh toán | Thẻ Visa Sandbox giả lập lỗi `INSUFFICIENT_FUNDS` | 1. Nhập thông tin thẻ có số dư 0đ.<br/>2. Xác nhận thanh toán. | Cổng thanh toán báo lỗi: "Giao dịch không thành công do số dư thẻ không đủ". Hệ thống không trừ tiền, giữ nguyên trạng thái đơn để khách chọn thẻ khác. | Xử lý ngoại lệ thanh toán |
| **TC-BOOK-09** | Thanh toán cọc qua Ví điện tử MoMo | Đơn ở trạng thái chờ cọc | Số tiền cọc: 600.000đ | 1. Chọn thanh toán "Ví MoMo".<br/>2. Quét mã QR MoMo trên màn hình bằng App MoMo.<br/>3. Xác nhận trừ tiền. | Webhook MoMo IPN gửi tín hiệu thanh toán thành công. Màn hình tự động cập nhật sang trạng thái "Đã đặt cọc thành công". | Tích hợp Ví điện tử |
| **TC-BOOK-10** | Thanh toán cọc bằng Số dư Ví Mioto (Mioto Wallet) | Ví Mioto có số dư 1.500.000đ | Số tiền cọc: 800.000đ | 1. Chọn phương thức "Ví Mioto".<br/>2. Nhập mã PIN ví.<br/>3. Bấm "Thanh toán". | Khấu trừ 800.000đ trong ví Mioto, số dư mới còn 700.000đ. Đơn chuyển trạng thái "Đã đặt cọc" ngay lập tức mà không qua cổng trung gian. | Nghiệp vụ Ví nội bộ |
| **TC-BOOK-11** | Người dùng hủy ngang khi đang ở trang thanh toán cổng trung gian | Đang chuyển hướng sang Alepay | Khách bấm "Hủy giao dịch / Quay lại" | 1. Bấm nút hủy trên cổng Alepay. | Hệ thống nhận callback mã hủy, hiển thị thông báo: "Giao dịch chưa hoàn tất. Bạn vẫn còn 45 phút để hoàn thành việc đặt cọc". | Ngoại lệ người dùng hủy |

---

## 4.5. Phân hệ 5: Bàn giao xe, Quản lý Chuyến đi & Trả xe (Trip Lifecycle & Check-in/Check-out)

### 4.5.1. Danh sách Ca kiểm thử chi tiết Phân hệ Quản lý Chuyến đi:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-TRIP-01** | Thực hiện Check-in bàn giao xe thành công với đủ ảnh | Đơn ở trạng thái "Đã đặt cọc", đến giờ nhận xe | 4 ảnh góc thân xe, 1 ảnh đồng hồ ODO (ghi 25.000 km), 1 ảnh vạch xăng (100%) | 1. Hai bên gặp mặt, chủ xe/khách mở mục Check-in.<br/>2. Chụp đủ 4 góc ngoại thất và đồng hồ xe.<br/>3. Nhập số ODO ban đầu: 25000.<br/>4. Chọn mức nhiên liệu: Đầy bình.<br/>5. Hai bên ký xác nhận trên màn hình cảm ứng. | Hệ thống lưu trữ toàn bộ ảnh lên Cloud Storage, tạo biên bản bàn giao điện tử. Trạng thái chuyến đi đổi thành "Đang diễn ra" (In Progress). | Quy trình bàn giao nghiệp vụ |
| **TC-TRIP-02** | Check-in thiếu ảnh ngoại thất bắt buộc (< 4 ảnh) | Ở màn hình Check-in | Chỉ chụp 2 ảnh | 1. Chụp 2 ảnh.<br/>2. Cố gắng bấm nút "Ký xác nhận bàn giao". | Nút bấm bị mờ hoặc báo lỗi: "Vui lòng chụp đầy đủ ít nhất 4 góc xe (đầu, đuôi, sườn trái, sườn phải) để bảo vệ quyền lợi". | Ràng buộc dữ liệu đầu vào |
| **TC-TRIP-03** | Check-out trả xe đúng giờ, không vượt km, xăng hoàn trả đủ | Chuyến đi đang diễn ra, đến giờ trả | ODO trả xe: 25.500 km (Thuê 2 ngày, hạn mức 600km, đi 500km). Xăng: Đầy bình. | 1. Chụp ảnh xe lúc trả.<br/>2. Nhập ODO kết thúc: 25500.<br/>3. Xác nhận xăng đầy bình.<br/>4. Bấm "Hoàn thành chuyến đi". | Hệ thống ghi nhận số km di chuyển là 500km ($\le 600$km). Phụ phí vượt km: 0đ. Phụ phí bù xăng: 0đ. Khách thanh toán 70% tiền thuê còn lại. | Kịch bản lý tưởng (Happy Path) |
| **TC-TRIP-04** | Check-out có vượt hạn mức quãng đường (Over-mileage) | Thuê 1 ngày (hạn mức 300km/ngày), đơn giá vượt: 3.000đ/km | ODO nhận: 20.000 km. ODO trả: 20.450 km (Đi 450 km -> Vượt 150 km) | 1. Nhập ODO kết thúc: 20450.<br/>2. Hệ thống tự động tính chênh lệch. | Hệ thống tính toán chính xác phần vượt: $(450 - 300) \times 3.000 = 450.000$đ. Tự động thêm dòng "Phụ phí vượt quãng đường: 450.000đ" vào hóa đơn quyết toán. | Thuật toán phụ phí BVA |
| **TC-TRIP-05** | Check-out thiếu xăng so với mức ban đầu | Lúc nhận: Đầy bình (8/8 vạch). Lúc trả: Còn 4/8 vạch (thiếu 50% bình, tương đương 25 lít xăng) | Giá xăng niêm yết: 24.000đ/lít | 1. Chọn mức xăng khi trả: 4/8 vạch.<br/>2. Xác nhận tình trạng. | Hệ thống tính phụ phí bù nhiên liệu: $25 \times 24.000 = 600.000$đ cộng vào hóa đơn thanh toán cuối cùng. | Nghiệp vụ tính phụ phí |
| **TC-TRIP-06** | Check-out trả xe trễ hạn (Over-time surcharge) | Hẹn trả lúc 18:00, thực tế trả lúc 20:30 (Trễ 2.5 giờ) | Đơn giá thuê: 1.200.000đ/ngày. Đơn giá trễ: 100.000đ/giờ | 1. Bấm check-out lúc 20:30.<br/>2. Hệ thống so sánh với giờ hẹn trên hợp đồng. | Hệ thống phát hiện trễ 2.5 giờ, tự động tính phụ phí quá giờ: $2.5 \times 100.000 = 250.000$đ và hiển thị trên bảng kê quyết toán. | Ràng buộc thời gian |
| **TC-TRIP-07** | Áp dụng phụ phí vệ sinh xe và phụ phí khử mùi thuốc lá | Xe bị dính bùn đất nội thất và có mùi khói thuốc | Phí rửa xe: 100.000đ, Phí khử mùi: 300.000đ | 1. Chủ xe chọn tích vào "Xe cần vệ sinh" và "Xe có mùi thuốc lá".<br/>2. Tải ảnh minh chứng.<br/>3. Gửi yêu cầu phụ phí. | Hệ thống cộng thêm 400.000đ vào chi phí phát sinh và yêu cầu khách xác nhận thanh toán. | Phụ phí phát sinh |

---

## 4.6. Phân hệ 6: Chính sách Hủy chuyến & Bồi hoàn cọc (Cancellation & Compensation Policy)

### 4.6.1. Bảng Quyết định (Decision Table) cho Chính sách Hủy chuyến:
- **C1: Tác nhân hủy:** Khách thuê xe (Renter) hay Chủ sở hữu xe (Owner).
- **C2: Thời điểm hủy:**
  - Mốc 1: Trước giờ nhận xe $> 7$ ngày.
  - Mốc 2: Từ 7 ngày đến trước 24 giờ.
  - Mốc 3: Dưới 24 giờ trước giờ nhận xe.

**Bảng Quyết định Hủy chuyến:**

| Quy tắc | Tác nhân hủy | Thời điểm hủy chuyến | Tỷ lệ hoàn cọc cho Khách | Bồi thường cho Khách | Hình phạt đối với bên hủy |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **CR-01** | Khách thuê | $> 7$ ngày trước giờ khởi hành | **Hoàn 100% cọc** | Không có | Phí chuyển khoản ngân hàng (nếu có) |
| **CR-02** | Khách thuê | Từ 7 ngày đến $> 24$ giờ | **Hoàn 50% cọc** | Không có | Mất 50% tiền cọc (chuyển bồi thường cho chủ xe) |
| **CR-03** | Khách thuê | Dưới 24 giờ trước giờ nhận xe | **Hoàn 0% (Mất cọc)** | Không có | Mất 100% tiền cọc (bồi thường chủ xe và phí nền tảng) |
| **CR-04** | Chủ xe | Bất kỳ thời điểm nào sau khi đã nhận cọc | **Hoàn 100% cọc** | Nhận thêm tiền bồi thường bằng 30% giá trị cọc | Bị phạt 30% tiền cọc, trừ điểm uy tín, hạ thứ hạng hiển thị |

### 4.6.2. Danh sách Ca kiểm thử chi tiết Phân hệ Hủy chuyến:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-CANC-01** | Khách hủy chuyến trước > 7 ngày (Quy tắc CR-01) | Đã cọc 1.000.000đ, thời gian nhận xe là 10 ngày sau | Đơn đặt xe ID: `TRIP-1001` | 1. Khách vào chi tiết chuyến đi.<br/>2. Bấm "Hủy chuyến".<br/>3. Chọn lý do hủy.<br/>4. Xác nhận hủy. | - Trạng thái đổi thành "Đã hủy bởi khách".<br/>- Thông báo: "Bạn được hoàn lại 100% tiền cọc (1.000.000đ)".<br/>- Tiền được hoàn về Ví Mioto hoặc thẻ gốc trong 3-5 ngày làm việc.<br/>- Mở lại lịch trống cho xe. | Decision Table (CR-01) |
| **TC-CANC-02** | Khách hủy chuyến cách giờ nhận xe 3 ngày (Quy tắc CR-02) | Đã cọc 1.000.000đ, thời gian nhận xe là 3 ngày sau (thuộc khoảng 7 ngày - 24h) | Đơn đặt xe ID: `TRIP-1002` | 1. Bấm "Hủy chuyến".<br/>2. Xem chính sách bồi cọc hiển thị trên popup.<br/>3. Bấm xác nhận hủy. | - Trạng thái đổi thành "Đã hủy bởi khách".<br/>- Khách được hoàn 50% tiền cọc (500.000đ).<br/>- 500.000đ còn lại được chuyển vào ví chủ xe làm tiền bồi thường giữ lịch. | Decision Table (CR-02) |
| **TC-CANC-03** | Khách hủy chuyến gấp dưới 24 giờ trước giờ nhận xe (Quy tắc CR-03) | Đã cọc 1.000.000đ, giờ nhận xe là 6 giờ tới | Đơn đặt xe ID: `TRIP-1003` | 1. Bấm "Hủy chuyến".<br/>2. Xác nhận hủy gấp. | - Thông báo: "Theo chính sách, bạn sẽ mất 100% tiền cọc (1.000.000đ) do hủy chuyến trong vòng 24 giờ".<br/>- Không hoàn tiền cọc.<br/>- Chuyển tiền đền bù cho chủ xe. | Decision Table (CR-03) / BVA biên 24h |
| **TC-CANC-04** | Kiểm tra giá trị biên thời gian hủy: Đúng 24 giờ 00 phút | Đã cọc giữ chỗ | Thời gian nhận xe đúng 24h00m sau thời điểm bấm hủy | 1. Bấm hủy tại mốc đúng 24h00m. | Hệ thống áp dụng chính sách hoàn 50% cọc (thuộc biên trên của khung 7 ngày - 24h). | BVA (Biên 24 giờ) |
| **TC-CANC-05** | Chủ xe bấm hủy chuyến sau khi khách đã cọc (Quy tắc CR-04) | Khách đã đặt cọc 1.000.000đ thành công | Chủ xe hủy vì lý do cá nhân | 1. Chủ xe mở đơn, bấm "Hủy chuyến".<br/>2. Nhập lý do.<br/>3. Xác nhận. | - Khách được hoàn lại 100% tiền cọc (1.000.000đ).<br/>- Khách được tặng thêm voucher đền bù 300.000đ (30% cọc).<br/>- Chủ xe bị phạt 300.000đ khấu trừ vào ví và bị ghi nhận 1 lần hủy chuyến làm giảm tỷ lệ phản hồi. | Decision Table (CR-04) |

---

## 4.7. Phân hệ 7: Đánh giá, Phản hồi & Xếp hạng (Rating & Review System)

### 4.7.1. Danh sách Ca kiểm thử chi tiết Phân hệ Đánh giá:

| Test Case ID | Tên ca kiểm thử | Điều kiện tiên quyết | Dữ liệu kiểm thử (Test Data) | Các bước thực hiện (Test Steps) | Kết quả kỳ vọng (Expected Result) | Kỹ thuật áp dụng |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-RATE-01** | Gửi đánh giá 5 sao kèm bình luận và hình ảnh sau khi hoàn tất chuyến | Chuyến đi ở trạng thái "Đã hoàn thành" (Completed) | Điểm: 5 sao. Bình luận: "Xe chạy rất êm, sạch sẽ, chủ xe nhiệt tình!". Ảnh đính kèm: 2 ảnh | 1. Vào lịch sử chuyến đi, chọn chuyến vừa xong.<br/>2. Bấm "Đánh giá chuyến đi".<br/>3. Chấm 5 sao, nhập bình luận, đính kèm ảnh.<br/>4. Bấm "Gửi đánh giá". | Đánh giá được lưu thành công, hiển thị công khai trên trang chi tiết của xe. Điểm sao trung bình của xe được tính toán lại ngay lập tức. | Luồng thành công (Happy Path) |
| **TC-RATE-02** | Cố gắng gửi đánh giá khi chuyến đi chưa hoàn thành | Chuyến đi đang ở trạng thái "Đã đặt cọc" hoặc "Đang đi" | Chuyến chưa kết thúc | 1. Mở chi tiết đơn hàng.<br/>2. Tìm nút đánh giá. | Nút "Đánh giá" không xuất hiện hoặc bị vô hiệu hóa kèm chú thích: "Chức năng đánh giá chỉ mở sau khi bạn hoàn tất trả xe". | Ràng buộc trạng thái (State precondition) |
| **TC-RATE-03** | Đánh giá lại lần thứ hai cho cùng một chuyến đi | Đã gửi đánh giá thành công cho chuyến đi này | Cố gắng gửi tiếp đánh giá mới | 1. Mở lại chuyến đi đã được đánh giá.<br/>2. Thử bấm gửi đánh giá mới. | Nút đánh giá chuyển thành "Đã đánh giá" và không cho phép gửi thêm lượt đánh giá thứ hai (mỗi chuyến chỉ được đánh giá duy nhất 1 lần). | Tính toàn vẹn nghiệp vụ (Idempotency) |
| **TC-RATE-04** | Gửi đánh giá sau thời hạn 7 ngày kể từ khi kết thúc chuyến | Chuyến hoàn thành đã quá 8 ngày | Thời gian hoàn thành > 7 ngày | 1. Truy cập đơn hàng cũ.<br/>2. Kiểm tra quyền đánh giá. | Hệ thống đóng form đánh giá với thông báo: "Thời hạn gửi đánh giá cho chuyến đi này đã kết thúc (trong vòng 7 ngày kể từ khi trả xe)". | BVA (Biên thời gian 7 ngày) |
| **TC-RATE-05** | Nhập nội dung bình luận rỗng khi chỉ chấm sao | Đang ở form đánh giá | Chấm 4 sao, để trống ô bình luận text | 1. Chọn 4 sao.<br/>2. Không nhập text.<br/>3. Bấm "Gửi đánh giá". | Hệ thống vẫn cho phép gửi thành công (nội dung văn bản là tùy chọn, điểm sao là bắt buộc). | Ràng buộc tùy chọn |
| **TC-RATE-06** | Tính toán cập nhật điểm sao trung bình của xe | Xe hiện có 4 lượt đánh giá: 5, 5, 4, 4 sao (TB = 4.5 sao). Đánh giá mới: 5 sao | Điểm mới: 5 sao | 1. Gửi đánh giá 5 sao.<br/>2. Tải lại trang chi tiết xe. | Điểm trung bình mới được tính chính xác: $(5 + 5 + 4 + 4 + 5) / 5 = 4.6$ sao. Số lượt đánh giá tăng lên 5 lượt. | Kiểm tra giải thuật tính toán |

