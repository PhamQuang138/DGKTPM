with open('BaoCao_KTPM_Mioto/bao_cao_bai_tap_lon_mioto.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Tab 4.1 (decision_pricing)
old_p = r"""\begin{table}[ht]
  \centering\small
  \begin{tabularx}{\textwidth}{lcccccc}
    \toprule
    \textbf{Điều kiện / Hành động} & \textbf{R1} & \textbf{R2} & \textbf{R3} & \textbf{R4} & \textbf{R5} & \textbf{R6} \\
    \midrule
    \textbf{C1: Ngày thuê} & Ngày thường & Cuối tuần & Ngày Lễ/Tết & Ngày thường & Cuối tuần & Ngày thường \\
    \textbf{C2: Khoảng cách ($d$)} & Tại bãi ($d=0$) & $\le 5$km & $> 5$km & Tại bãi ($d=0$) & $> 5$km & $> 5$km \\
    \textbf{C3: Mã Voucher} & Không & Không & Không & Giảm 10\% & Giảm 100k & Hết hạn \\
    \midrule
    \textbf{A1: Phụ phí ngày} & 0đ & +15\% & +30\% & 0đ & +15\% & 0đ \\
    \textbf{A2: Phí giao xe} & 0đ & 0đ & $(d-5)\times 15k$ & 0đ & $(d-5)\times 15k$ & $(d-5)\times 15k$ \\
    \textbf{A3: Bảo hiểm MIC} & 10\% tiền thuê & 10\% tiền thuê & 10\% tiền thuê & 10\% tiền thuê & 10\% tiền thuê & 10\% tiền thuê \\
    \textbf{A4: Giảm Voucher} & 0đ & 0đ & 0đ & -10\% giá gốc & -100.000đ & 0đ (Báo lỗi) \\
    \textbf{A5: Tiền cọc 30\%} & $30\% \times \text{Tổng}$ & $30\% \times \text{Tổng}$ & $30\% \times \text{Tổng}$ & $30\% \times \text{Tổng}$ & $30\% \times \text{Tổng}$ & $30\% \times \text{Tổng}$ \\
    \bottomrule
  \end{tabularx}
  \caption{Bảng quyết định kiểm thử tính toán chi phí thuê xe Mioto}
  \label{tab:decision_pricing}
\end{table}"""

new_p = r"""\begin{table}[ht]
  \centering\footnotesize
  \begin{tabularx}{\textwidth}{Xcccccc}
    \toprule
    \textbf{Điều kiện / Hành động} & \textbf{R1} & \textbf{R2} & \textbf{R3} & \textbf{R4} & \textbf{R5} & \textbf{R6} \\
    \midrule
    \textbf{C1: Loại ngày thuê} & Ngày thường & Cuối tuần & Lễ/Tết & Ngày thường & Cuối tuần & Ngày thường \\
    \textbf{C2: Khoảng cách ($d$)} & Tại bãi & $\le 5$km & $> 5$km & Tại bãi & $> 5$km & $> 5$km \\
    \textbf{C3: Mã Voucher} & Không & Không & Không & Giảm 10\% & Giảm 100k & Hết hạn \\
    \midrule
    \textbf{A1: Phụ phí ngày} & 0đ & +15\% & +30\% & 0đ & +15\% & 0đ \\
    \textbf{A2: Phí giao xe} & 0đ & 0đ & $(d-5)\times 15$k & 0đ & $(d-5)\times 15$k & $(d-5)\times 15$k \\
    \textbf{A3: Bảo hiểm MIC} & 10\% thuê & 10\% thuê & 10\% thuê & 10\% thuê & 10\% thuê & 10\% thuê \\
    \textbf{A4: Mức giảm Voucher} & 0đ & 0đ & 0đ & -10\% gốc & -100.000đ & 0đ \\
    \textbf{A5: Tiền đặt cọc (30\%)} & $30\% \times \text{T}$ & $30\% \times \text{T}$ & $30\% \times \text{T}$ & $30\% \times \text{T}$ & $30\% \times \text{T}$ & $30\% \times \text{T}$ \\
    \bottomrule
  \end{tabularx}
  \caption{Bảng quyết định kiểm thử tính toán chi phí thuê xe Mioto}
  \label{tab:decision_pricing}
\end{table}"""

# Replace Tab 5.1 (basis_paths)
old_bp = r"""\section{Tập 7 Đường đi Cơ sở Độc lập (Basis Paths) và Kết quả Thực thi}
\begin{table}[ht]
  \centering\small
  \begin{tabularx}{\textwidth}{clXcc}
    \toprule
    \textbf{ID} & \textbf{Đường đi trên CFG} & \textbf{Tổ hợp điều kiện \& Test Data} & \textbf{Kỳ vọng} & \textbf{Kết quả} \\
    \midrule
    \textbf{P1} & $1 \to 2 \to 5 \to 6 \to 7 \to 9 \to 10 \to 11 \to 14 \to 15 \to 17$ & Lễ, $d=10$km ($>5$), Voucher 10\% (Rate 1tr, 2 ngày) & 2.675.000đ & \textbf{PASS} \\
    \textbf{P2} & $1 \to 3 \to 4a \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13a \to \dots$ & Cuối tuần, $d=4$km ($\le 5$), VC cố định 100k & 2.430.000đ & \textbf{PASS} \\
    \textbf{P3} & $1 \to 3 \to 4b \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13b \to \dots$ & Ngày thường, $d=0$km, Không áp dụng Voucher & 1.100.000đ & \textbf{PASS} \\
    \textbf{P4} & $1 \to 3 \to 4b \to 5 \to 6 \to 7 \to 9 \to 10 \to 11 \to 14 \to 15 \to 16 \to 17$ & Ngày thường, $d=6$km, VC 200\% $\to$ Final $<0 \to 0$đ & 0đ & \textbf{PASS} \\
    \textbf{P5} & $1 \to 3 \to 4a \to 5 \to 6 \to 7 \to 9 \to 10 \to 12 \to 13b \to \dots$ & Cuối tuần, $d=8$km, Mã Voucher không hợp lệ & 2.069.000đ & \textbf{PASS} \\
    \textbf{P6} & $1 \to 2 \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13a \to \dots$ & Lễ, $d=5$km (Biên), Voucher cố định 500k & 5.935.000đ & \textbf{PASS} \\
    \textbf{P7} & $1 \to 3 \to 4b \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13a \to 14 \to 15 \to 16 \to 17$ & Ngày thường, $d=2$km, Voucher 1 triệu $\to 0$đ & 0đ & \textbf{PASS} \\
    \bottomrule
  \end{tabularx}
  \caption{Tập ca kiểm thử bao phủ 100\% Basis Paths cho thuật toán tính giá}
  \label{tab:basis_paths}
\end{table}"""

new_bp = r"""\section{Tập 7 Đường đi Cơ sở Độc lập (Basis Paths) và Kết quả Thực thi}
\begin{table}[ht]
  \centering\footnotesize
  \begin{tabularx}{\textwidth}{p{0.8cm}p{4.2cm}Xcc}
    \toprule
    \textbf{ID} & \textbf{Đường đi trên CFG} & \textbf{Tổ hợp điều kiện \& Dữ liệu kiểm thử} & \textbf{Kỳ vọng} & \textbf{Kết quả} \\
    \midrule
    \textbf{P1} & $1 \to 2 \to 5 \to 6 \to 7 \to 9 \to 10 \to 11 \to 14 \to 15 \to 17$ & Lễ, $d=10$km ($>5$), Voucher 10\% (Rate 1tr, 2 ngày) & 2.675.000đ & \textbf{PASS} \\
    \textbf{P2} & $1 \to 3 \to 4a \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13a \to \dots$ & Cuối tuần, $d=4$km ($\le 5$), VC cố định 100k & 2.430.000đ & \textbf{PASS} \\
    \textbf{P3} & $1 \to 3 \to 4b \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13b \to \dots$ & Ngày thường, $d=0$km, Không dùng Voucher & 1.100.000đ & \textbf{PASS} \\
    \textbf{P4} & $1 \to 3 \to 4b \to 5 \to 6 \to 7 \to 9 \to 10 \to 11 \to 14 \to 15 \to 16 \to 17$ & Ngày thường, $d=6$km, VC 200\% $\to$ Final $<0 \to 0$đ & 0đ & \textbf{PASS} \\
    \textbf{P5} & $1 \to 3 \to 4a \to 5 \to 6 \to 7 \to 9 \to 10 \to 12 \to 13b \to \dots$ & Cuối tuần, $d=8$km, Mã Voucher không hợp lệ & 2.069.000đ & \textbf{PASS} \\
    \textbf{P6} & $1 \to 2 \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13a \to \dots$ & Lễ, $d=5$km (Biên), Voucher cố định 500k & 5.935.000đ & \textbf{PASS} \\
    \textbf{P7} & $1 \to 3 \to 4b \to 5 \to 6 \to 8 \to 9 \to 10 \to 12 \to 13a \to 14 \to 15 \to 16 \to 17$ & Ngày thường, $d=2$km, Voucher 1.000.000đ $\to 0$đ & 0đ & \textbf{PASS} \\
    \bottomrule
  \end{tabularx}
  \caption{Tập ca kiểm thử bao phủ 100\% Basis Paths cho thuật toán tính giá}
  \label{tab:basis_paths}
\end{table}"""

# Replace Tab 6.1 (iso_quality_score)
old_iso = r"""\begin{table}[ht]
  \centering\small
  \begin{tabularx}{\textwidth}{clccX}
    \toprule
    \textbf{STT} & \textbf{Đặc tính chất lượng} & \textbf{Trọng số} & \textbf{Điểm (/10)} & \textbf{Nhận xét đánh giá chi tiết} \\
    \midrule
    1 & \textbf{Tính phù hợp chức năng} & 25\% & \textbf{9.3} & Đầy đủ 100\% nghiệp vụ P2P; Tính toán cước \& KYC chính xác. \\
    2 & \textbf{Hiệu năng \& Tối ưu tải} & 15\% & \textbf{8.5} & FCP 1.4s, LCP 2.2s (Google Web Vitals); API latency $\sim 450$ms. \\
    3 & \textbf{Khả năng tương thích} & 10\% & \textbf{9.5} & Chạy hoàn hảo trên Chrome, Safari, Edge, Firefox, Mobile. \\
    4 & \textbf{Khả năng sử dụng (UX)} & 15\% & \textbf{9.0} & Đặt xe 3 bước trực quan; Minh bạch chi phí; Bản đồ số Map View. \\
    5 & \textbf{Độ tin cậy (Reliability)} & 10\% & \textbf{9.0} & SLA 99.9\%; Chịu lỗi phân tán; Lưu nháp đơn khi mất mạng. \\
    6 & \textbf{Tính an toàn bảo mật} & 15\% & \textbf{9.0} & HTTPS/TLS 1.3, Tokenization thẻ PCI-DSS, Pre-signed URL GPLX. \\
    7 & \textbf{Khả năng bảo trì} & 5\% & \textbf{8.5} & Kiến trúc Microservices phân tách độc lập; Tách nhỏ chunks JS. \\
    8 & \textbf{Tính khả chuyển} & 5\% & \textbf{8.5} & Đóng gói Container Docker/Kubernetes đa nền tảng Cloud. \\
    \midrule
    \multicolumn{2}{l}{\textbf{TỔNG ĐIỂM CHẤT LƯỢNG TOÀN DIỆN}} & \textbf{100\%} & \textbf{9.00 / 10.0} & \textbf{XẾP LOẠI XUẤT SẮC (GRADE A)} \\
    \bottomrule
  \end{tabularx}
  \caption{Bảng điểm đánh giá chất lượng toàn diện hệ thống Mioto.vn theo ISO/IEC 25010}
  \label{tab:iso_quality_score}
\end{table}"""

new_iso = r"""\begin{table}[ht]
  \centering\footnotesize
  \begin{tabularx}{\textwidth}{cp{4.2cm}ccX}
    \toprule
    \textbf{STT} & \textbf{Đặc tính chất lượng (ISO 25010)} & \textbf{Trọng số} & \textbf{Điểm (/10)} & \textbf{Nhận xét đánh giá chi tiết} \\
    \midrule
    1 & \textbf{Tính phù hợp chức năng} & 25\% & \textbf{9.3} & Đầy đủ 100\% nghiệp vụ P2P; Tính toán cước \& KYC chính xác. \\
    2 & \textbf{Hiệu năng \& Tối ưu tải} & 15\% & \textbf{8.5} & FCP 1.4s, LCP 2.2s (Google Web Vitals); API latency $\sim 450$ms. \\
    3 & \textbf{Khả năng tương thích} & 10\% & \textbf{9.5} & Chạy hoàn hảo trên Chrome, Safari, Edge, Firefox, Mobile. \\
    4 & \textbf{Khả năng sử dụng (UX)} & 15\% & \textbf{9.0} & Đặt xe 3 bước trực quan; Minh bạch chi phí; Bản đồ số Map View. \\
    5 & \textbf{Độ tin cậy (Reliability)} & 10\% & \textbf{9.0} & SLA 99.9\%; Chịu lỗi phân tán; Lưu nháp đơn khi mất mạng. \\
    6 & \textbf{Tính an toàn bảo mật} & 15\% & \textbf{9.0} & HTTPS/TLS 1.3, Tokenization thẻ PCI-DSS, Pre-signed URL GPLX. \\
    7 & \textbf{Khả năng bảo trì} & 5\% & \textbf{8.5} & Kiến trúc Microservices phân tách độc lập; Tách nhỏ chunks JS. \\
    8 & \textbf{Tính khả chuyển} & 5\% & \textbf{8.5} & Đóng gói Container Docker/Kubernetes đa nền tảng Cloud. \\
    \midrule
    \multicolumn{2}{l}{\textbf{TỔNG ĐIỂM CHẤT LƯỢNG TOÀN DIỆN}} & \textbf{100\%} & \textbf{9.00 / 10.0} & \textbf{XẾP LOẠI XUẤT SẮC (GRADE A)} \\
    \bottomrule
  \end{tabularx}
  \caption{Bảng điểm đánh giá chất lượng toàn diện hệ thống Mioto.vn theo ISO/IEC 25010}
  \label{tab:iso_quality_score}
\end{table}"""

assert old_p in text, "old_p not found"
text = text.replace(old_p, new_p)

assert old_bp in text, "old_bp not found"
text = text.replace(old_bp, new_bp)

assert old_iso in text, "old_iso not found"
text = text.replace(old_iso, new_iso)

with open('BaoCao_KTPM_Mioto/bao_cao_bai_tap_lon_mioto.tex', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced all 3 wide tables successfully!")

