# -*- coding: utf-8 -*-
with open('bao_cao_bai_tap_lon_mioto.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace excessive bolding in body paragraphs
text = text.replace(r'\textbf{68 ca test chức năng \& 7 ca test hộp trắng}', '68 ca test chức năng và 7 ca test hộp trắng')
text = text.replace(r'\textbf{73 / 75 ca (97.33\%)}', '73 / 75 ca (97.33%)')
text = text.replace(r'\textbf{2 / 75 ca (2.67\%)}', '2 / 75 ca (2.67%)')
text = text.replace(r'\textbf{100\%}', '100%')
text = text.replace(r'\textbf{XẾP LOẠI XUẤT SẮC (GRADE A)}', 'Xếp loại Xuất sắc (Grade A)')
text = text.replace(r'\textbf{TỔNG ĐIỂM CHẤT LƯỢNG TOÀN DIỆN}', 'Tổng điểm chất lượng toàn diện')

# Replace in conclusion
text = text.replace(r'\textbf{Khảo sát và bóc tách thực tế (Reverse-Engineering):}', r'\textit{Khảo sát và bóc tách thực tế (Reverse-Engineering):}')
text = text.replace(r'\textbf{Lập tài liệu kiểm thử chuẩn hóa IEEE 829:}', r'\textit{Lập tài liệu kiểm thử chuẩn hóa IEEE 829:}')
text = text.replace(r'\textbf{Thiết kế và thực thi kiểm thử chức năng hộp đen đa phương pháp:}', r'\textit{Thiết kế và thực thi kiểm thử chức năng hộp đen đa phương pháp:}')
text = text.replace(r'\textbf{Kiểm thử hộp trắng chuyên sâu (White-Box Testing):}', r'\textit{Kiểm thử hộp trắng chuyên sâu (White-Box Testing):}')
text = text.replace(r'\textbf{Đánh giá chất lượng toàn diện theo tiêu chuẩn ISO/IEC 25010:}', r'\textit{Đánh giá chất lượng toàn diện theo tiêu chuẩn ISO/IEC 25010:}')
text = text.replace(r'\textbf{Tự động hóa kiểm thử (Test Automation):}', r'\textit{Tự động hóa kiểm thử (Test Automation):}')
text = text.replace(r'\textbf{Ma trận truy xuất nguồn gốc RTM \& Báo cáo lỗi:}', r'\textit{Ma trận truy xuất nguồn gốc RTM \& Báo cáo lỗi:}')

with open('bao_cao_bai_tap_lon_mioto.tex', 'w', encoding='utf-8') as f:
    f.write(text)
print('Successfully cleaned excessive bolding and casing!')
