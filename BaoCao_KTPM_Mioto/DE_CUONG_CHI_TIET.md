# ĐỀ CƯƠNG CHI TIẾT BÁO CÁO BÀI TẬP LỚN
## MÔN: ĐẢM BẢO CHẤT LƯỢNG VÀ KIỂM THỬ PHẦN MỀM (SQA)
**ĐỀ TÀI: ĐÁNH GIÁ CHẤT LƯỢNG VÀ KIỂM THỬ CHỨC NĂNG HỆ THỐNG ĐẶT XE TRỰC TUYẾN MIOTO (MIOTO.VN)**

- **Sinh viên thực hiện:** Phạm Duy Quang
- **Mã số sinh viên (MSSV):** 23017167
- **Lớp / Khóa:** Công nghệ Thông tin - K68
- **Đối tượng khảo sát & kiểm thử:** Nền tảng cho thuê xe tự lái và có tài xế trực tuyến Mioto (Website: https://www.mioto.vn, App iOS/Android, Backend Microservices: m-car, m-wallet, payment, m-rtc, gift, m-blog)

---

### MỤC LỤC TỔNG THỂ DỰ KIẾN (BÁO CÁO QUY MÔ 100+ TRANG)

#### PHẦN MỞ ĐẦU
- Lời cam đoan
- Lời cảm ơn
- Danh mục thuật ngữ và chữ viết tắt (Glossary & Acronyms: SQA, BVA, EP, CFG, RTM, ISO 25010, GPLX, OTP, VNI, MIC, P2P,...)
- Danh mục bảng biểu và sơ đồ hình vẽ

#### CHƯƠNG 1: TỔNG QUAN HỆ THỐNG ĐẶT XE TRỰC TUYẾN MIOTO.VN & PHẠM VI ĐỀ TÀI
1.1. Bối cảnh thị trường cho thuê xe tự lái và mô hình kinh tế chia sẻ (P2P Car Rental) tại Việt Nam.
1.2. Giới thiệu tổng quan về Công ty Cổ phần Mioto Asia và nền tảng Mioto.vn.
1.3. Mô hình hoạt động và đối tượng người dùng (Khách thuê xe - Renter, Chủ xe cá nhân/Doanh nghiệp - Car Owner, Quản trị viên hệ thống - Admin).
1.4. Mục tiêu và ý nghĩa thực tiễn của đề tài kiểm định chất lượng phần mềm đối với hệ thống Mioto.vn.
1.5. Phạm vi nghiên cứu và kiểm thử (In-scope và Out-of-scope).
1.6. Phương pháp luận nghiên cứu và quy trình kiểm thử áp dụng (V-Model, Agile Testing, Chuẩn IEEE 829, Chuẩn ISO/IEC/IEEE 29119, Chuẩn ISO/IEC 25010).

#### CHƯƠNG 2: PHÂN TÍCH YÊU CẦU NGHIỆP VỤ VÀ KIẾN TRÚC HỆ THỐNG MIOTO.VN
2.1. Kiến trúc hệ thống tổng thể (System Architecture & Microservices: React Frontend, Backend Services: m-car, payment, m-wallet, m-rtc, WebSocket, 3rd Integrations: Alepay, MoMo, VNPay, Here Maps, Google Maps, Định danh GPLX Cục CSGT/Bộ Công An, Bảo hiểm MIC/VNI).
2.2. Đặc tả yêu cầu chức năng (Software Requirement Specification - SRS) theo phân hệ:
   - Module 1: Xác thực & Quản lý hồ sơ người dùng (Auth, KYC GPLX, CCCD/Passport).
   - Module 2: Tìm kiếm, Bộ lọc & Định vị xe (Location, Thời gian, Hãng xe, Truyền động, Nhiên liệu, Tính năng, Giao xe tận nơi/sân bay).
   - Module 3: Chi tiết xe, Tính toán giá cước & Khuyến mãi (Đơn giá, Phụ phí cuối tuần/lễ tết, Phí bảo hiểm chuyến đi, Phí vượt km, Phí lưu đêm, Phụ phí vệ sinh/khử mùi, Voucher/Coupon).
   - Module 4: Quy trình đặt xe, Phê duyệt, Đặt cọc & Thanh toán (Giữ chỗ, Chủ xe duyệt tự động/thủ công, Đặt cọc 30%, Thanh toán qua thẻ/ví/chuyển khoản).
   - Module 5: Bàn giao xe, Quản lý chuyến đi & Trả xe (Biên bản bàn giao ảnh xe trước/sau, Ghi nhận ODO, Kiểm tra bình xăng/pin, Ký điện tử).
   - Module 6: Hủy chuyến, Bồi cọc & Hoàn tiền theo chính sách Mioto.
   - Module 7: Đánh giá, Phản hồi & Xếp hạng (Rating & Review 1-5 sao).
   - Module 8: Quản lý dành cho Chủ xe (Đăng ký xe, Lịch bận, Thiết lập giá, Báo cáo doanh thu, Rút tiền ví).
2.3. Sơ đồ Ca sử dụng tổng quát (Use Case Diagram) & Đặc tả chi tiết các Use Case trọng yếu.
2.4. Sơ đồ Luồng hoạt động (Activity Diagrams) và Sơ đồ Trạng thái đơn hàng (State Machine Diagram của Trip: Đặt xe -> Chờ duyệt -> Đã cọc -> Đang đi -> Đã trả xe -> Hoàn tất/Hủy).
2.5. Đặc tả yêu cầu phi chức năng (Non-Functional Requirements - NFR: Thời gian phản hồi, Tải đồng thời, Tính bảo mật dữ liệu thẻ PCI-DSS, Tính sẵn sàng 99.9%).

#### CHƯƠNG 3: KẾ HOẠCH KIỂM THỬ PHẦN MỀM (TEST PLAN THEO CHUẨN IEEE 829)
3.1. Định danh kế hoạch kiểm thử (Test Plan Identifier).
3.2. Giới thiệu và mục tiêu kiểm thử (Test Objectives & Quality Goals).
3.3. Các hạng mục kiểm thử (Test Items / Deliverables).
3.4. Các tính năng cần kiểm thử và không kiểm thử (Features to be tested / not tested).
3.5. Chiến lược và phương pháp tiếp cận kiểm thử (Testing Strategy: Functional, Usability, Performance, Security, Compatibility, Regression).
3.6. Tiêu chí bắt đầu, tạm dừng, phục hồi và kết thúc kiểm thử (Entry, Suspension, Resumption, Exit Criteria).
3.7. Môi trường kiểm thử (Test Environment: Hardware, OS, Browser Matrix, Test Data, Staging Server).
3.8. Phân công nhân sự, vai trò và trách nhiệm (Roles & Responsibilities).
3.9. Lịch trình và mốc thời gian thực hiện (Schedule & Milestones).
3.10. Quản lý rủi ro kiểm thử và kế hoạch dự phòng (Risk Assessment & Mitigation Matrix).

#### CHƯƠNG 4: THIẾT KẾ CÁC BỘ CA KIỂM THỬ CHỨC NĂNG CHI TIẾT (FUNCTIONAL TEST CASES)
*(Triển khai chuyên sâu với hàng trăm Test Cases theo bảng chuẩn: Test Case ID, Description, Preconditions, Test Steps, Test Data, Expected Result, Test Technique)*
4.1. Phân hệ Xác thực & Quản lý Tài khoản (Auth & Profile):
   - Đăng ký tài khoản bằng SĐT (Xác thực OTP SMS, Giới hạn retry OTP, Chống spam OTP).
   - Đăng nhập (Mật khẩu, OTP, Social Login Google/Facebook/Apple).
   - Xác thực Giấy phép lái xe (GPLX) & Căn cước công dân (Kiểm thử BVA/EP với số GPLX, ngày cấp, hạng bằng B1/B2/C, nhận diện OCR ảnh bằng lái).
   - Quản lý đổi mật khẩu, Cập nhật thông tin cá nhân, Yêu cầu xóa tài khoản.
4.2. Phân hệ Tìm kiếm & Bộ lọc xe (Search & Filter Engine):
   - Tìm kiếm theo địa điểm (Tỉnh/Thành phố, Quận/Huyện, Sân bay, Tọa độ GPS).
   - Tìm kiếm theo khoảng thời gian thuê (Giờ nhận - Giờ trả, Ràng buộc tối thiểu 24h, Thuê qua đêm, Thuê dịp lễ tết).
   - Bộ lọc nâng cao: Hãng xe, Loại xe (Sedan, SUV, Hatchback, MPV, Bán tải), Truyền động (Số sàn, Số tự động), Nhiên liệu (Xăng, Dầu, Điện), Tính năng an toàn (Camera lùi, Cảm biến lốp, Apple CarPlay, Cửa sổ trời,...).
   - Bộ lọc tiện ích: Giao xe tận nơi, Đặt xe nhanh (Instant Booking), Miễn thế chấp tiền mặt.
4.3. Phân hệ Chi tiết xe, Bảng giá & Áp dụng Mã giảm giá (Pricing & Promotion Engine):
   - Kiểm thử tính toán giá thuê theo Bảng quyết định (Decision Table Testing): Đơn giá gốc + Phụ phí cuối tuần (T7, CN) + Phụ phí lễ tết + Phí giao xe theo km (0-5km miễn phí, >5km tính theo bậc thang).
   - Phí bảo hiểm chuyến đi (Bảo hiểm vật chất xe MIC/VNI: 10% - 15% đơn giá hoặc mức cố định).
   - Áp dụng Voucher / Mã khuyến mãi: Mã giảm theo %, Mã giảm số tiền cố định, Mã có điều kiện giá trị đơn hàng tối thiểu, Mã quá hạn, Mã hết lượt, Mã dùng lại (Security/Concurrency test).
4.4. Phân hệ Đặt xe, Phê duyệt & Đặt cọc (Booking & Deposit Flow):
   - Tạo yêu cầu đặt xe (Gửi lời nhắn cho chủ xe, Chọn hình thức thanh toán cọc).
   - Luồng đặt xe nhanh (Instant Booking - Tự động xác nhận).
   - Luồng phê duyệt thông thường (Chủ xe có 60 phút để phản hồi: Chấp nhận / Từ chối / Hết thời gian tự hủy).
   - Thanh toán tiền đặt cọc (Deposit 30% giá trị chuyến đi):
     * Cổng thanh toán Thẻ ATM Nội địa / Napas.
     * Cổng Thẻ tín dụng Quốc tế (Visa / MasterCard / JCB) qua Alepay.
     * Ví điện tử MoMo / ZaloPay / ShopeePay / VNPay QR.
     * Ví điện tử Mioto (Mioto Wallet).
     * Xử lý ngoại lệ thanh toán: Timeout, Thẻ hết hạn, Số dư không đủ, Người dùng hủy giao dịch, Webhook phản hồi trễ.
4.5. Phân hệ Quản lý Chuyến đi & Bàn giao nhận xe (Trip Management & Check-in/Check-out):
   - Chờ nhận xe: Thông tin liên lạc chủ xe/khách thuê, Vị trí xe thời gian thực.
   - Thủ tục Check-in (Nhận xe): Chụp tối thiểu 4 góc xe, Chụp đồng hồ xăng/ODO, Ghi nhận vết xước cũ, Ký hợp đồng điện tử.
   - Thủ tục Check-out (Trả xe): Chụp ảnh hiện trạng xe, Kiểm tra mức nhiên liệu (Tính phí bù xăng theo giá thị trường), Kiểm tra số km vượt hạn mức (Ví dụ: Giới hạn 300km/ngày, vượt tính 3.000đ - 5.000đ/km), Phụ phí vệ sinh (nếu xe bẩn), Phụ phí khử mùi (nếu hút thuốc).
4.6. Phân hệ Hủy chuyến & Bồi thường cọc (Cancellation & Compensation Policy):
   - Kiểm thử Bảng quyết định cho Chính sách hủy chuyến:
     * Khách hủy trước > 7 ngày: Hoàn 100% cọc.
     * Khách hủy trong vòng 7 ngày đến trước 24h: Mất 30% - 50% cọc (bồi thường chủ xe).
     * Khách hủy trong vòng 24h: Mất 100% cọc.
     * Chủ xe hủy chuyến: Bồi thường 100% cọc cho khách + Mioto phạt chủ xe theo quy chế.
4.7. Phân hệ Đánh giá & Xếp hạng (Review & Rating System):
   - Đánh giá sao (1 - 5 sao) và nhận xét text + upload ảnh.
   - Ràng buộc: Chỉ người đã hoàn tất chuyến mới được đánh giá, Mỗi chuyến chỉ được đánh giá 1 lần trong vòng 7 ngày.
   - Tính toán điểm trung bình sao của xe và chủ xe.
4.8. Phân hệ Dành cho Chủ xe (Owner Portal):
   - Đăng tải thông tin xe (Cavet xe, Đăng kiểm, Bảo hiểm TNDS, Bảo hiểm 2 chiều, Thiết lập lịch bận và bảng giá theo ngày).
   - Quản lý ví chủ xe (Doanh thu ròng sau khi trừ chiết khấu Mioto 12% - 15%, Yêu cầu rút tiền về tài khoản ngân hàng).

#### CHƯƠNG 5: THIẾT KẾ KIỂM THỬ HỘP TRẮNG VÀ KIỂM THỬ DÒNG ĐIỀU KHIỂN (WHITE-BOX TESTING)
5.1. Giới thiệu kỹ thuật kiểm thử hộp trắng trong kiểm thử phần mềm.
5.2. Lựa chọn module trọng tâm: Thuật toán tính toán chi phí thuê xe và phụ phí (Pricing & Surcharge Calculator Algorithm).
5.3. Mã nguồn mô phỏng thuật toán tính cước (Python/C++ implementation của module tính giá Mioto).
5.4. Xây dựng Đồ thị Dòng điều khiển (Control Flow Graph - CFG):
   - Đánh số nút (Nodes) và cung (Edges).
   - Xác định các nút rẽ nhánh (Predicate Nodes).
5.5. Tính độ phức tạp Cyclomatic (Cyclomatic Complexity - $V(G)$):
   - Phương pháp 1: $V(G) = E - N + 2P$
   - Phương pháp 2: $V(G) = P + 1$ (Số nút điều kiện + 1)
   - Phương pháp 3: Số vùng khép kín (Enclosed Regions + 1)
5.6. Xác định Tập đường đi cơ sở độc lập (Basis Paths Set).
5.7. Thiết kế Bộ ca kiểm thử đảm bảo độ bao phủ đường đi cơ sở (Basis Path Test Suite), bao phủ nhánh (Branch Coverage), và bao phủ câu lệnh (Statement Coverage).

#### CHƯƠNG 6: ĐÁNH GIÁ CHẤT LƯỢNG PHẦN MỀM THEO TIÊU CHUẨN QUỐC TẾ ISO/IEC 25010
6.1. Tổng quan mô hình chất lượng phần mềm ISO/IEC 25010 (SQuaRE - Software Product Quality).
6.2. Đánh giá Tính phù hợp chức năng (Functional Suitability):
   - Tính đầy đủ của chức năng (Functional Completeness).
   - Tính đúng đắn của chức năng (Functional Correctness).
   - Tính thích hợp của chức năng (Functional Appropriateness).
6.3. Đánh giá Hiệu năng & Tải hệ thống (Performance Efficiency):
   - Phân tích thời gian phản hồi (Response Time / Latency) của các trang và API.
   - Đánh giá khả năng chịu tải và thông lượng (Throughput / Requests per second) sử dụng kịch bản JMeter/K6.
   - Mức độ sử dụng tài nguyên (Resource Utilization).
6.4. Đánh giá Khả năng sử dụng và Trải nghiệm người dùng (Usability):
   - Khả năng nhận biết và học hỏi (Learnability).
   - Tính thẩm mỹ và mức độ thuận tiện trong luồng đặt xe (User Interface Aesthetics & Accessibility WCAG 2.1).
   - Bảo vệ người dùng khỏi lỗi thao tác (User Error Protection).
6.5. Đánh giá Độ tin cậy (Reliability):
   - Tính sẵn sàng (Availability: SLA 99.9%).
   - Khả năng chịu lỗi (Fault Tolerance: Xử lý khi cổng thanh toán sập, mất kết nối mạng di động).
   - Khả năng phục hồi (Recoverability: Lưu nháp đơn đặt xe, session hồi phục sau crash).
6.6. Đánh giá Tính bảo mật (Security):
   - Bảo mật thông tin danh tính người dùng và Giấy phép lái xe (GPLX).
   - Tuân thủ an toàn thanh toán trực tuyến (PCI-DSS, mã hóa SSL/TLS, Tokenization thẻ tín dụng).
   - Phòng chống các lỗ hổng OWASP Top 10 (SQL Injection, XSS, Broken Object Level Authorization - BOLA/IDOR, Rate Limiting chống Brute-force OTP).
6.7. Đánh giá Tính tương thích (Compatibility):
   - Tương thích đa trình duyệt (Chrome, Safari, Firefox, Edge).
   - Tương thích đa nền tảng và thiết bị di động (Responsive Web, iOS, Android).
6.8. Tổng hợp Bảng điểm đánh giá chất lượng toàn diện hệ thống Mioto.vn.

#### CHƯƠNG 7: THIẾT KẾ KỊCH BẢN KIỂM THỬ TỰ ĐỘNG (AUTOMATION TESTING SUITE)
7.1. Chiến lược và Kim tự tháp kiểm thử tự động (Automation Pyramid: Unit -> API -> E2E UI).
7.2. Thiết kế Kịch bản Kiểm thử API Tự động (API Test Collection với Postman / Newman):
   - API Collection đặc tả đầy đủ Request, Header, Auth Token, Body và Test Scripts (JavaScript Assertions).
   - Test Suite 1: Authentication & User Profile APIs.
   - Test Suite 2: Car Search & Listing Filter APIs (`/api/cars`, query parameters).
   - Test Suite 3: Booking Creation, Calculation & Payment Webhooks.
   - Test Suite 4: Owner Dashboard & Wallet Balance APIs.
   - Môi trường thực thi CI/CD và báo cáo Newman HTML Report.
7.3. Thiết kế Kịch bản Kiểm thử Giao diện Người dùng Tự động (UI E2E Automation với Selenium WebDriver / Playwright Python):
   - Áp dụng mô hình thiết kế Page Object Model (POM).
   - Kịch bản E2E 1: Luồng Tìm kiếm xe -> Xem chi tiết -> Nhập mã giảm giá -> Kiểm tra bảng giá cước.
   - Kịch bản E2E 2: Luồng Xác thực form đăng ký & Bắt lỗi các trường bắt buộc (GPLX, SĐT).
   - Mã nguồn tự động hóa chi tiết bằng Python (`test_mioto_search.py`, `test_mioto_booking.py`).

#### CHƯƠNG 8: QUẢN LÝ LỖI, BÁO CÁO KẾT QUẢ KIỂM THỬ & MA TRẬN TRUY XUẤT (RTM)
8.1. Quy trình quản lý vòng đời lỗi phần mềm (Defect Life Cycle: New -> Open -> Fixed -> Retest -> Closed).
8.2. Hệ thống phân loại mức độ nghiêm trọng (Severity: Blocker, Critical, Major, Minor) và mức độ ưu tiên (Priority: P1, P2, P3, P4).
8.3. Báo cáo các lỗi điển hình phát hiện trong quá trình kiểm thử (Bug Reports chi tiết với Steps to Reproduce, Expected vs Actual, Screenshots/Logs).
8.4. Ma trận truy xuất nguồn gốc yêu cầu (Requirements Traceability Matrix - RTM) đối chiếu 100% Use Case với Test Case ID.
8.5. Thống kê và Phân tích kết quả kiểm thử (Test Execution Metrics: Tỷ lệ Pass/Fail, Mật độ lỗi Defect Density, Độ bao phủ kiểm thử Test Coverage).

#### CHƯƠNG 9: KẾT LUẬN VÀ ĐỀ XUẤT CẢI TIẾN HỆ THỐNG
9.1. Đánh giá tổng kết về chất lượng và độ hoàn thiện của hệ thống Mioto.vn.
9.2. Những điểm mạnh và ưu điểm nổi bật của nền tảng.
9.3. Những rủi ro, hạn chế còn tồn đọng và đề xuất cải tiến (Kiến trúc, Nghiệp vụ, Trải nghiệm UX, Bảo mật dữ liệu cá nhân).
9.4. Bài học kinh nghiệm thu nhận được sau quá trình thực hiện bài tập lớn môn SQA.

#### TÀI LIỆU THAM KHẢO & PHỤ LỤC
- Danh mục tài liệu tham khảo (Tiêu chuẩn ISO/IEC 25010, Giáo trình SQA, ISTQB Foundation Syllabus, Tài liệu đặc tả kỹ thuật Mioto.vn).
- Phụ lục A: Chi tiết 120+ Test Cases chức năng dạng bảng đầy đủ.
- Phụ lục B: Kịch bản kiểm thử API Postman Collection JSON.
- Phụ lục C: Mã nguồn kiểm thử tự động Python/Selenium.

