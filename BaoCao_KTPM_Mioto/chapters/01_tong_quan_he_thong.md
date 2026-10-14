# BÁO CÁO BÀI TẬP LỚN MÔN ĐẢM BẢO CHẤT LƯỢNG VÀ KIỂM THỬ PHẦN MỀM
# ĐỀ TÀI: ĐÁNH GIÁ CHẤT LƯỢNG VÀ KIỂM THỬ CHỨC NĂNG HỆ THỐNG ĐẶT XE TRỰC TUYẾN MIOTO (MIOTO.VN)

**Sinh viên thực hiện:** Phạm Duy Quang  
**Mã số sinh viên (MSSV):** 23017167  
**Lớp:** Công nghệ Thông tin - K68  
**Giảng viên hướng dẫn:** Bộ môn Công nghệ Phần mềm / Đảm bảo Chất lượng & Kiểm thử Phần mềm  

---

## LỜI NÓI ĐẦU & CAM ĐOAN

Trong thời đại chuyển đổi số và sự bùng nổ của nền kinh tế chia sẻ (Sharing Economy), các dịch vụ kết nối ngang hàng (Peer-to-Peer - P2P) đang ngày càng định hình lại thói quen tiêu dùng của xã hội. Nổi bật trong lĩnh vực di chuyển thông minh tại Việt Nam là nền tảng cho thuê xe tự lái và có tài xế trực tuyến **Mioto (Mioto.vn)** thuộc Công ty Cổ phần Mioto Asia. Nền tảng này đóng vai trò cầu nối công nghệ tin cậy giữa hàng chục nghìn chủ sở hữu phương tiện nhàn rỗi và những khách hàng có nhu cầu thuê xe phục vụ công tác, du lịch hay gia đình.

Tuy nhiên, đặc thù của một hệ thống thương mại điện tử kết hợp logistics và tài chính như Mioto đòi hỏi tính chính xác, tính sẵn sàng và mức độ an toàn thông tin ở cấp độ rất cao:
1. **Tính phức tạp về nghiệp vụ:** Hệ thống phải quản lý tài sản giá trị cao (ô tô từ vài trăm triệu đến hàng tỷ đồng), quy trình xác thực định danh khách hàng nghiêm ngặt (KYC Giấy phép lái xe - GPLX, Căn cước công dân - CCCD), chính sách cọc, bồi thường thiệt hại, phụ phí xăng xe, vượt km, bảo hiểm vật chất chuyến đi (MIC, VNI) và giao nhận xe đa phương thức.
2. **Tính thời gian thực và giao dịch tài chính:** Hệ thống tích hợp đa cổng thanh toán (Alepay, Thẻ quốc tế Visa/MasterCard, Ví điện tử MoMo, VNPAY, Mioto Wallet) và đồng bộ lịch xe theo thời gian thực (Real-time Calendar) nhằm loại bỏ nguy cơ trùng lịch đặt xe (Double Booking).

Xuất phát từ tầm quan trọng sống còn của chất lượng phần mềm đối với uy tín thương hiệu và an toàn tài sản của người dùng, đề tài **"Đánh giá chất lượng và kiểm thử chức năng hệ thống đặt xe trực tuyến Mioto (Mioto.vn)"** được thực hiện nhằm áp dụng toàn diện các kiến thức, phương pháp luận và tiêu chuẩn quốc tế về Kiểm thử & Đảm bảo Chất lượng Phần mềm (Software Quality Assurance - SQA) vào một hệ sinh thái sản phẩm thực tế.

Em xin cam đoan toàn bộ các số liệu khảo sát, quy trình bóc tách mã nguồn, kiến trúc hệ thống, các bộ ca kiểm thử chức năng (Functional Test Cases), kịch bản kiểm thử tự động (Automation Test Suites với Postman và Selenium), phân tích dòng điều khiển (Control Flow Graph - CFG) và báo cáo đánh giá chất lượng theo chuẩn ISO/IEC 25010 trong tài liệu này đều do bản thân em trực tiếp nghiên cứu, thực nghiệm và xây dựng nghiêm túc.

---

## DANH MỤC THUẬT NGỮ VÀ CHỮ VIẾT TẮT

| Viết tắt | Tên tiếng Anh đầy đủ | Ý nghĩa tiếng Việt |
| :--- | :--- | :--- |
| **SQA** | Software Quality Assurance | Đảm bảo chất lượng phần mềm |
| **STLC** | Software Testing Life Cycle | Vòng đời kiểm thử phần mềm |
| **SRS** | Software Requirements Specification | Tài liệu đặc tả yêu cầu phần mềm |
| **EP** | Equivalence Partitioning | Kỹ thuật phân vùng tương đương |
| **BVA** | Boundary Value Analysis | Kỹ thuật phân tích giá trị biên |
| **CFG** | Control Flow Graph | Đồ thị dòng điều khiển |
| **RTM** | Requirements Traceability Matrix | Ma trận truy xuất nguồn gốc yêu cầu |
| **ISO/IEC 25010** | Systems and software engineering — SQuaRE | Tiêu chuẩn quốc tế về mô hình chất lượng phần mềm |
| **IEEE 829** | Standard for Software Test Documentation | Tiêu chuẩn tài liệu kiểm thử phần mềm IEEE |
| **GPLX** | Giấy phép lái xe | Bằng lái xe cơ giới đường bộ (B1, B2, C) |
| **CCCD** | Căn cước công dân | Giấy tờ tùy thân định danh công dân |
| **OTP** | One-Time Password | Mật khẩu dùng một lần (xác thực SMS/Email) |
| **P2P** | Peer-to-Peer | Mô hình kinh tế chia sẻ ngang hàng |
| **KYC** | Know Your Customer | Quy trình định danh và xác minh khách hàng |
| **ODO** | Odometer | Chỉ số đồng hồ quãng đường lăn bánh của xe ô tô |
| **API** | Application Programming Interface | Giao diện lập trình ứng dụng |
| **REST** | Representational State Transfer | Kiến trúc dịch vụ web không lưu trạng thái |
| **JWT** | JSON Web Token | Chuỗi mã hóa phục vụ xác thực người dùng |
| **PCI-DSS** | Payment Card Industry Data Security Standard | Tiêu chuẩn an ninh dữ liệu thẻ thanh toán |
| **E2E** | End-to-End Testing | Kiểm thử toàn trình từ đầu đến cuối hệ thống |
| **CI/CD** | Continuous Integration / Continuous Deployment | Tích hợp và Triển khai phần mềm liên tục |

---

# CHƯƠNG 1: TỔNG QUAN HỆ THỐNG ĐẶT XE TRỰC TUYẾN MIOTO.VN VÀ PHẠM VI ĐỀ TÀI

## 1.1. Bối cảnh thị trường cho thuê xe ô tô và mô hình kinh tế chia sẻ (P2P Car Rental)
Trong những năm gần đây, xu hướng du lịch tự túc, các chuyến công tác linh hoạt và nhu cầu trải nghiệm lái xe cá nhân tại các đô thị lớn ở Việt Nam (Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Nha Trang, Đà Lạt, Phú Quốc,...) tăng trưởng vượt bậc. Việc sở hữu một chiếc ô tô cá nhân đối mặt với nhiều chi phí cố định cao: khấu hao xe, phí đăng kiểm, bảo hiểm bắt buộc và tự nguyện, phí bảo dưỡng định kỳ, phí bến bãi đỗ xe và thuế phí liên quan. Ngược lại, nhiều chủ xe chỉ sử dụng phương tiện vào dịp cuối tuần hoặc một vài ngày trong tháng, dẫn đến tình trạng tài sản nhàn rỗi gây lãng phí.

Mô hình cho thuê xe ngang hàng (Peer-to-Peer Car Rental), tương tự như mô hình Turo hay Getaround trên thế giới, cho phép chủ xe (Car Owner) chia sẻ quyền sử dụng chiếc xe nhàn rỗi của mình cho khách có nhu cầu thuê (Renter) thông qua một nền tảng công nghệ trung gian. Khách thuê xe được hưởng mức giá tối ưu hơn từ 20% - 30% so với các công ty thuê xe truyền thống, được chủ động lựa chọn chính xác đời xe, màu sắc, tính năng, và địa điểm giao nhận xe thuận tiện. Đồng thời, chủ xe có thêm nguồn thu nhập thụ động đáng kể để trang trải chi phí nuôi xe.

## 1.2. Giới thiệu tổng quan về Nền tảng Mioto (Mioto.vn)
Mioto là một trong những ứng dụng tiên phong và dẫn đầu thị trường cho thuê xe ô tô tự lái và có tài xế tại Việt Nam, vận hành bởi Công ty Cổ phần Mioto Asia. Ra mắt từ năm 2017, Mioto đã nhanh chóng phát triển mạng lưới bao phủ hơn 25 tỉnh thành lớn với hàng nghìn dòng xe đa dạng: từ các mẫu xe phổ thông đô thị (Hyundai Grand i10, Kia Morning, Toyota Vios, Honda City), SUV gầm cao gia đình (Mitsubishi Xpander, Toyota Fortuner, Ford Everest, Hyundai SantaFe) đến các dòng xe hạng sang (Mercedes-Benz, BMW, VinFast VF8, VF9).

### Các điểm nhấn cốt lõi của Mioto:
- **Đa dạng phương thức thuê:** Cho thuê xe tự lái (Self-drive) và Cho thuê xe có tài xế (With driver), cho thuê theo ngày hoặc theo gói dài hạn (Car Subscription).
- **Quy trình số hóa 100%:** Từ khâu tìm kiếm, lọc xe theo bán kính bản đồ, đặt cọc trực tuyến, chụp ảnh hiện trạng xe khi nhận/trả xe (Photo Check-in/Check-out) đến ký xác nhận hợp đồng điện tử.
- **Bảo hiểm vật chất chuyến đi:** Hợp tác cùng các tập đoàn bảo hiểm lớn (Bảo hiểm Quân Đội MIC, Tổng công ty Cổ phần Bảo hiểm Hàng không VNI) cung cấp gói bảo hiểm bảo vệ toàn diện cho cả chủ xe và khách thuê trong suốt thời gian diễn ra chuyến đi.
- **Minh bạch tài chính:** Bảng kê chi phí công khai, rõ ràng về đơn giá ngày, phụ phí cuối tuần/lễ tết, phí vượt giới hạn quãng đường (Over-mileage fee), phụ phí trả xe trễ hạn (Over-time fee), phí rửa xe và phụ phí khử mùi (Smell removal fee).

## 1.3. Mô hình hoạt động và Các tác nhân người dùng (Actors)
Hệ thống Mioto.vn vận hành xoay quanh 3 nhóm tác nhân chính:

1. **Khách thuê xe (Renter):**
   - Tìm kiếm xe theo vị trí địa lý, thời gian, mức giá, thương hiệu, loại xe và các tiện ích đi kèm.
   - Quản lý hồ sơ cá nhân: Cập nhật và gửi duyệt Giấy phép lái xe (GPLX hạng B1/B2 trở lên), Căn cước công dân (CCCD).
   - Gửi yêu cầu đặt xe, áp dụng mã voucher khuyến mãi, chọn gói bảo hiểm chuyến đi.
   - Thực hiện thanh toán tiền cọc (thông thường là 30% giá trị hợp đồng thuê xe).
   - Tiến hành nhận xe (Check-in), kiểm tra tình trạng thân vỏ nội ngoại thất và đồng hồ nhiên liệu/ODO.
   - Hoàn tất chuyến đi (Check-out), thanh toán các khoản phụ phí phát sinh (nếu có) và đánh giá dịch vụ (Rating & Review).

2. **Chủ sở hữu phương tiện (Car Owner):**
   - Đăng ký hồ sơ xe: Tải lên hình ảnh xe thực tế, giấy tờ đăng kiểm, bảo hiểm TNDS, bảo hiểm thân vỏ.
   - Thiết lập biểu phí cho thuê theo ngày thường, ngày cuối tuần (Thứ Bảy, Chủ Nhật) và các ngày lễ tết quốc gia.
   - Cấu hình các điều khoản thuê xe: Yêu cầu thế chấp (Xe máy + Cà vẹt gốc hoặc tiền mặt 15.000.000đ), giới hạn số km tối đa trong ngày (ví dụ: 300 - 400 km/ngày), phụ phí giao nhận xe tận nơi.
   - Tiếp nhận, phê duyệt hoặc từ chối các yêu cầu đặt xe từ khách thuê trong thời hạn quy định (60 phút).
   - Bàn giao chìa khóa xe, đối soát biên bản giao nhận trên ứng dụng, nhận lại xe và quyết toán phụ phí.
   - Theo dõi doanh thu, lịch sử giao dịch và gửi lệnh rút tiền từ Ví Mioto về tài khoản ngân hàng liên kết.

3. **Quản trị viên hệ thống & Đội ngũ CSKH (System Administrator & Support Operator):**
   - Kiểm duyệt hồ sơ giấy tờ xe mới và phê duyệt tài khoản GPLX của khách thuê.
   - Quản lý cấu hình khuyến mãi, phát hành mã giảm giá (Vouchers/Promo Codes).
   - Xử lý tranh chấp, khiếu nại giữa chủ xe và khách thuê (hủy chuyến, đền bù hư hỏng, vi phạm hợp đồng, phạt nguội giao thông).
   - Đối soát giao dịch với các cổng thanh toán đối tác và công ty bảo hiểm.
   - Giám sát tình trạng vận hành, tải hệ thống và an ninh bảo mật.

## 1.4. Mục tiêu và Ý nghĩa thực tiễn của đề tài
1. **Mục tiêu học thuật:**
   - Vận dụng các kiến thức cốt lõi của môn học Đảm bảo Chất lượng và Kiểm thử Phần mềm vào một ứng dụng thực tiễn quy mô lớn.
   - Làm chủ các kỹ thuật thiết kế ca kiểm thử hộp đen: Phân vùng tương đương (Equivalence Partitioning), Phân tích giá trị biên (Boundary Value Analysis), Bảng quyết định (Decision Table Testing), Kiểm thử chuyển trạng thái (State Transition Testing) và Use Case Testing.
   - Làm chủ kỹ thuật kiểm thử hộp trắng: Xây dựng Đồ thị dòng điều khiển (CFG), tính toán độ phức tạp Cyclomatic Complexity ($V(G)$) và xác định tập đường đi độc lập cơ sở (Basis Path Testing).
   - Triển khai kịch bản kiểm thử tự động (Automation Testing) cho tầng API (sử dụng Postman/Newman) và tầng giao diện người dùng E2E (sử dụng Python Selenium/Playwright).
   - Đánh giá toàn diện chất lượng sản phẩm phần mềm dựa trên khung tiêu chuẩn quốc tế ISO/IEC 25010 (SQuaRE).

2. **Ý nghĩa thực tiễn đối với hệ thống Mioto.vn:**
   - Phát hiện các khiếm khuyết tiềm ẩn (defects/bugs) về logic tính toán giá cước, phụ phí và bồi thường cọc.
   - Đánh giá tính an toàn bảo mật trong lưu trữ và truyền tải thông tin định danh cá nhân (GPLX, CCCD) và giao dịch tiền tệ.
   - Cung cấp các khuyến nghị cải tiến nâng cao trải nghiệm người dùng (UX) và tối ưu hóa hiệu năng hệ thống.

## 1.5. Phạm vi nghiên cứu và Kiểm thử (Scope of Testing)

### 1.5.1. Các phân hệ thuộc phạm vi kiểm thử (In-Scope):
1. **Phân hệ Quản lý Tài khoản & Xác thực (Authentication & Authorization):**
   - Đăng ký/Đăng nhập bằng số điện thoại di động thông qua mã OTP SMS.
   - Đăng nhập thông qua tài khoản mạng xã hội (Google, Facebook).
   - Quy trình cập nhật thông tin cá nhân và định danh KYC Giấy phép lái xe (GPLX).
   - Đổi mật khẩu, chức năng quên mật khẩu và chính sách khóa tài khoản khi nhập sai liên tiếp.
2. **Phân hệ Tìm kiếm, Định vị & Bộ lọc xe (Search & Filter Engine):**
   - Tìm kiếm xe theo Tỉnh/Thành phố, Quận/Huyện, Sân bay hoặc vị trí hiện tại của người dùng.
   - Tìm kiếm xe theo khoảng thời gian thuê (Ngày bắt đầu - Ngày kết thúc, Giờ nhận - Giờ trả xe).
   - Lọc xe theo các tiêu chí: Loại xe (4 chỗ, 7 chỗ), Hãng xe (Toyota, Mazda, Hyundai, Kia, Honda, Ford, VinFast,...), Kiểu dáng (Sedan, Hatchback, SUV, Crossover, MPV, Bán tải), Loại truyền động (Số tự động, Số sàn), Loại nhiên liệu (Xăng, Dầu Diesel, Điện).
   - Lọc theo các tính năng tiện ích đặc biệt: Xe có giao tận nơi, Đặt xe nhanh (Instant Booking), Miễn thế chấp xe máy/tiền mặt, Giảm giá đặc biệt.
3. **Phân hệ Bảng giá, Chi tiết xe & Khuyến mãi (Pricing & Promotion Engine):**
   - Kiểm tra tính đúng đắn của công thức tính giá: Đơn giá thuê cơ bản x Số ngày thuê.
   - Kiểm tra tính toán phụ phí: Phụ phí cuối tuần (T7, CN), Phụ phí ngày nghỉ Lễ/Tết theo quy định.
   - Phụ phí giao nhận xe tận nhà/sân bay theo số km thực tế.
   - Phí dịch vụ nền tảng Mioto và Phí bảo hiểm chuyến đi (MIC/VNI).
   - Logic áp dụng Mã giảm giá (Promo code/Voucher): kiểm tra mã hợp lệ, mã hết hạn, mã không đạt giá trị đơn hàng tối thiểu, mã giới hạn số lượt sử dụng.
4. **Phân hệ Quy trình Đặt xe, Phê duyệt & Đặt cọc (Booking & Payment Workflow):**
   - Luồng đặt xe có phê duyệt của chủ xe (trong vòng 60 phút).
   - Luồng đặt xe nhanh (Instant Booking - xác nhận giữ xe tức thì).
   - Quy trình thanh toán tiền cọc giữ chỗ (30% tổng chi phí chuyến đi) qua các cổng: Thẻ ATM nội địa/Napas, Thẻ tín dụng quốc tế Visa/MasterCard, Ví điện tử (MoMo, ZaloPay, VNPay) và Ví Mioto.
   - Xử lý các tình huống biên và ngoại lệ thanh toán: Giao dịch thành công, Giao dịch thất bại do thẻ không đủ số dư, Timeout kết nối, Hủy giao dịch giữa chừng.
5. **Phân hệ Quản lý Chuyến đi, Giao nhận xe & Trả xe (Trip Lifecycle & Check-in/Check-out):**
   - Quy trình bàn giao xe (Check-in): Chụp ảnh hiện trạng 4 góc ngoại thất, chụp mặt đồng hồ ODO và mức nhiên liệu xăng/pin, xác nhận biên bản bàn giao điện tử.
   - Quy trình trả xe (Check-out): Đối soát số km đã di chuyển so với hạn mức (tính phí vượt km), đối soát mức nhiên liệu (tính phụ phí bù nhiên liệu), phụ phí trả xe muộn giờ, phụ phí vệ sinh/khử mùi.
6. **Phân hệ Chính sách Hủy chuyến & Bồi hoàn cọc (Cancellation Policy):**
   - Khách thuê hủy chuyến trước 7 ngày (hoàn 100% tiền cọc).
   - Khách thuê hủy chuyến từ 7 ngày đến trước 24 giờ (hoàn một phần, đền bù chủ xe).
   - Khách thuê hủy chuyến trong vòng 24 giờ trước giờ nhận xe (mất 100% tiền cọc).
   - Chủ xe hủy chuyến: Hoàn 100% tiền cọc cho khách thuê + Bồi thường tiền phạt cho khách thuê theo chính sách bảo vệ người dùng của Mioto.
7. **Phân hệ Đánh giá & Phản hồi (Rating & Review System):**
   - Đánh giá chấm điểm số sao (1 đến 5 sao) và viết nhận xét chi tiết sau khi hoàn thành chuyến đi.
   - Ràng buộc quyền đánh giá: chỉ khách hàng đã thực hiện xong chuyến đi mới được gửi đánh giá; mỗi chuyến đi chỉ được đánh giá duy nhất một lần.

### 1.5.2. Các phần nằm ngoài phạm vi kiểm thử (Out-of-Scope):
- Can thiệp trực tiếp vào cơ sở dữ liệu nội bộ tầng thấp của Mioto (do yêu cầu bảo mật thông tin doanh nghiệp).
- Thực thi các giao dịch trừ tiền thực tế trên môi trường Production với tài khoản ngân hàng thật (sử dụng môi trường Sandbox/Staging và các kịch bản mô phỏng giao dịch thanh toán).
- Kiểm tra tính bền cơ học phần cứng của thiết bị GPS gắn trên xe.

## 1.6. Phương pháp luận và Tiêu chuẩn kiểm thử áp dụng
1. **Mô hình V-Model trong vòng đời phát triển phần mềm:** Đối chiếu chặt chẽ giữa các pha phân tích yêu cầu, thiết kế kiến trúc, thiết kế chi tiết với các pha kiểm thử chấp nhận (UAT), kiểm thử hệ thống (System Testing), kiểm thử tích hợp (Integration Testing) và kiểm thử đơn vị (Unit Testing).
2. **Chuẩn IEEE 829 (Standard for Software Test Documentation):** Áp dụng để xây dựng tài liệu Kế hoạch kiểm thử (Test Plan), Thiết kế ca kiểm thử (Test Case Specification), Nhật ký thực thi kiểm thử (Test Log) và Báo cáo tổng kết kiểm thử (Test Summary Report).
3. **Chuẩn ISO/IEC 25010 (SQuaRE):** Đánh giá 8 đặc tính chất lượng của sản phẩm phần mềm: Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability.
4. **Quy trình quản lý lỗi (Defect Management):** Áp dụng quy chuẩn theo dõi trạng thái lỗi từ New -> Assigned -> Open -> Fixed -> Retest -> Closed / Reopen.

