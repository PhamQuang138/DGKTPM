# CHƯƠNG 9: KẾT LUẬN VÀ ĐỀ XUẤT CẢI TIẾN HỆ THỐNG

## 9.1. Đánh giá Tổng kết về Chất lượng và Độ hoàn thiện của Hệ thống Mioto.vn

Trải qua quá trình khảo sát, cào cấu trúc mạng, bóc tách các bundle mã nguồn client-side, phân tích vi dịch vụ backend, thiết kế các bộ ca kiểm thử chức năng chuyên sâu và thực thi đánh giá dựa trên tiêu chuẩn quốc tế ISO/IEC 25010, đề tài rút ra các nhận định tổng kết như sau:

1. **Về quy mô và kiến trúc hệ thống:**
   - Mioto.vn là một nền tảng thương mại điện tử kết nối cho thuê xe ô tô P2P có quy mô lớn, được đầu tư bài bản về mặt công nghệ. Kiến trúc phân tán hướng vi dịch vụ (Microservices) tách biệt rõ ràng giữa các chức năng nghiệp vụ độc lập (`m-car`, `m-wallet`, `payment`, `m-rtc`, `gift`, `m-blog`) mang lại khả năng chịu tải tốt và tính sẵn sàng cao (Availability SLA 99.9%).
2. **Về tính phù hợp chức năng và giải quyết bài toán thực tế:**
   - Hệ thống giải quyết trọn vẹn và thông minh các nút thắt lớn nhất của mô hình thuê xe ngang hàng tại Việt Nam: xác thực bằng lái xe tự động, phòng chống gian lận thế chấp bằng căn cước công dân gắn chip, minh bạch hóa hiện trạng xe trước và sau chuyến đi bằng quy trình Check-in/Check-out qua ảnh chụp 4 góc xe và đồng hồ xăng/ODO, loại bỏ gần như tuyệt đối các xung đột, tranh chấp tài chính giữa khách thuê và chủ xe.
3. **Về tính đúng đắn trong các quy tắc nghiệp vụ:**
   - Các thuật toán tính toán giá cước, phụ phí ngày nghỉ, phụ phí giao xe tận nhà, phí bảo hiểm MIC/VNI và chính sách bồi cọc khi hủy chuyến đều được kiểm chứng hoạt động nhất quán, chính xác theo cả phương pháp Bảng quyết định hộp đen và Đồ thị dòng điều khiển (CFG) hộp trắng.

---

## 9.2. Những Ưu điểm Nổi bật của Nền tảng Mioto.vn
- **Trải nghiệm người dùng (UX) trực quan và hiện đại:** Giao diện đặt xe 3 bước tinh gọn, khả năng xem bản đồ trực tiếp (Map View) giúp khách hàng dễ dàng tìm kiếm chiếc xe gần vị trí đỗ nhất.
- **Tích hợp thanh toán đa dạng và bảo mật cao:** Hỗ trợ đầy đủ các kênh thanh toán nội địa và quốc tế (Visa, MasterCard qua Alepay, Ví MoMo, VNPay, Mioto Wallet) mà không trực tiếp lưu trữ thông tin thẻ nhạy cảm của người dùng (tuân thủ PCI-DSS).
- **Hệ thống bảo vệ quyền lợi hai chiều:** Hợp tác cùng các tập đoàn bảo hiểm lớn (MIC, VNI) cung cấp bảo hiểm vật chất chuyến đi với mức khấu trừ rõ ràng, tạo sự an tâm tối đa cho cả chủ phương tiện và người thuê xe.

---

## 9.3. Các Rủi ro, Hạn chế còn Tồn đọng và Đề xuất Giải pháp Cải tiến

Mặc dù đạt tổng điểm chất lượng xuất sắc (9.00/10 theo ISO/IEC 25010), quá trình kiểm thử vẫn chỉ ra một số điểm hạn chế mà hệ thống Mioto.vn cần xem xét cải tiến:

1. **Khắc phục lỗi làm tròn số thực trong hiển thị phụ phí (Khắc phục `BUG-MIOTO-001`):**
   - *Hạn chế:* Các phép tính phụ phí với số km thập phân đôi khi xuất hiện lỗi biểu diễn số chấm động của JavaScript (ví dụ: `36900.00000000001 VNĐ`).
   - *Đề xuất:* Áp dụng thư viện xử lý số học chính xác cho tài chính (như `decimal.js` hoặc `BigNumber.js`) và chuẩn hóa hàm format tiền tệ phía Client bằng `Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' })` trước khi render lên giao diện.
2. **Siết chặt cơ chế kiểm soát gửi OTP SMS (Khắc phục `BUG-MIOTO-002`):**
   - *Hạn chế:* Người dùng có thể vô tình hoặc cố ý spam nút gửi lại OTP trước khi đồng hồ đếm ngược 60 giây kết thúc, gây lãng phí chi phí viễn thông và rủi ro bị kẻ xấu lợi dụng làm nghẽn cổng SMS Brandname.
   - *Đề xuất:* Khóa nút bấm `disabled` ở tầng Client và áp dụng middleware Rate Limiting ở tầng API Gateway (chỉ cho phép tối đa 1 yêu cầu OTP/phút trên một IP và một số điện thoại).
3. **Cải tiến tính năng tự động hóa OCR nhận diện Giấy phép lái xe:**
   - *Hạn chế:* Một số trường hợp ảnh chụp bằng lái bị chói sáng hoặc góc nghiêng vẫn phải chờ đội ngũ CSKH duyệt thủ công (mất từ 2 đến 12 giờ).
   - *Đề xuất:* Tích hợp thêm mô hình AI OCR nâng cao có khả năng tự động nắn thẳng ảnh và cảnh báo người dùng chụp lại ngay lập tức nếu ảnh bị mờ hoặc lóa, giúp rút ngắn thời gian phê duyệt xuống dưới 30 giây.
4. **Bổ sung tính năng định vị thời gian thực của xe trước giờ giao nhận:**
   - *Đề xuất:* Cho phép khách thuê xe xem vị trí GPS xe đang di chuyển đến điểm hẹn giao xe (tương tự tính năng theo dõi tài xế của Grab hay Be), giúp nâng cao hơn nữa sự tiện lợi và chủ động cho khách hàng.

---

## 9.4. Bài học Kinh nghiệm Thu nhận được sau Đề tài
Qua việc hoàn thành toàn bộ bài tập lớn môn Đảm bảo Chất lượng và Kiểm thử Phần mềm:
- Sinh viên đã làm chủ được quy trình kiểm thử phần mềm chuyên nghiệp (STLC) theo các tiêu chuẩn quốc tế IEEE 829 và ISO/IEC 25010.
- Nắm vững và vận dụng nhuần nhuyễn các kỹ thuật thiết kế ca kiểm thử hộp đen (Phân vùng tương đương, Phân tích giá trị biên, Bảng quyết định, Ma trận chuyển trạng thái) để xử lý các bài toán nghiệp vụ phức tạp.
- Vận dụng thành công kỹ thuật kiểm thử hộp trắng: vẽ đồ thị dòng điều khiển CFG, tính toán độ phức tạp Cyclomatic $V(G)$ và thiết kế bộ test case bao phủ 100% đường đi cơ sở.
- Nâng cao kỹ năng xây dựng kịch bản kiểm thử tự động (Automation Testing) với Postman ở tầng API và Selenium WebDriver với Python ở tầng UI E2E, sẵn sàng cho công việc thực tế của một Kỹ sư SQA/QC chuyên nghiệp trong tương lai.

---

## TÀI LIỆU THAM KHẢO

1. **Bộ tiêu chuẩn quốc tế ISO/IEC 25010:2011:** *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models.* International Organization for Standardization (ISO).
2. **Tiêu chuẩn IEEE 829-2008:** *IEEE Standard for Software and System Test Documentation.* IEEE Computer Society.
3. **Giáo trình Kiểm thử Phần mềm:** Bộ môn Công nghệ Phần mềm, Khoa Công nghệ Thông tin.
4. **Tài liệu chuẩn ISTQB:** *Certified Tester Foundation Level (CTFL) Syllabus v4.0.* International Software Testing Qualifications Board (ISTQB), 2023.
5. **Nền tảng dịch vụ Mioto:** *Quy chế hoạt động, Điều khoản sử dụng và Chính sách bảo hiểm của Công ty Cổ phần Mioto Asia.* Website: `https://www.mioto.vn`.
6. **Mã nguồn và công nghệ tham chiếu:** Thư viện Selenium WebDriver Documentation, Postman API Testing Guides.

