import re

def escape_tex(text):
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('_', '\\_')
    text = text.replace('#', '\\#')
    return text

with open('BaoCao_KTPM_Mioto/chapters/04_bo_ca_kiem_thu_chuc_nang.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

tables = []
current_section = ""
in_table = False
table_rows = []

for line in lines:
    line_s = line.strip()
    if line_s.startswith('## '):
        current_section = line_s.replace('## ', '')
    elif line_s.startswith('| **TC-'):
        parts = [p.strip() for p in line_s.split('|')[1:-1]]
        if len(parts) >= 7:
            tc_id = parts[0].replace('**', '')
            tc_name = parts[1]
            tc_pre = parts[2]
            tc_data = parts[3]
            tc_steps = parts[4].replace('<br/>', ' ')
            tc_exp = parts[5].replace('<br/>', ' ')
            tc_tech = parts[6]
            table_rows.append({
                'id': tc_id,
                'name': tc_name,
                'steps': tc_steps,
                'exp': tc_exp,
                'tech': tc_tech
            })

print(f"Parsed {len(table_rows)} test cases from Chapter 4.")

# Format into LaTeX longtable
latex_tables = []
latex_tables.append("\\section{Danh sách Ca Kiểm thử Chức năng Chi tiết Toàn diện}\n")
latex_tables.append("Dưới đây là bảng đặc tả chi tiết của toàn bộ các ca kiểm thử chức năng được thiết kế cho hệ sinh thái Mioto.vn, chuẩn hóa theo chuẩn quốc tế IEEE 829:\n\n")

latex_tables.append("\\begin{longtable}{p{2.2cm}p{4cm}p{5.5cm}p{4cm}}\n")
latex_tables.append("\\caption{Danh mục chi tiết các ca kiểm thử chức năng hệ thống Mioto.vn} \\label{tab:full_test_cases} \\\\\n")
latex_tables.append("\\toprule\n")
latex_tables.append("\\textbf{Mã TC} & \\textbf{Tên ca kiểm thử} & \\textbf{Các bước \& Dữ liệu (Steps)} & \\textbf{Kỳ vọng (Expected Result)} \\\\\n")
latex_tables.append("\\midrule\n")
latex_tables.append("\\endfirsthead\n\n")

latex_tables.append("\\multicolumn{4}{c}{{\\bfseries \\tablename\\ \\thetable{} -- Tiếp tục từ trang trước}} \\\\\n")
latex_tables.append("\\toprule\n")
latex_tables.append("\\textbf{Mã TC} & \\textbf{Tên ca kiểm thử} & \\textbf{Các bước \& Dữ liệu (Steps)} & \\textbf{Kỳ vọng (Expected Result)} \\\\\n")
latex_tables.append("\\midrule\n")
latex_tables.append("\\endhead\n\n")

latex_tables.append("\\midrule \\multicolumn{4}{r}{{Còn tiếp ở trang sau...}} \\\\\n")
latex_tables.append("\\endfoot\n\n")

latex_tables.append("\\bottomrule\n")
latex_tables.append("\\endlastfoot\n\n")

for row in table_rows:
    cid = escape_tex(row['id'])
    cname = escape_tex(row['name'])
    csteps = escape_tex(row['steps'])
    cexp = escape_tex(row['exp'])
    latex_tables.append(f"\\textbf{{{cid}}} & {cname} & {csteps} & {cexp} \\\\ \\midrule\n")

latex_tables.append("\\end{longtable}\n")

with open('BaoCao_KTPM_Mioto/generated_test_cases.tex', 'w', encoding='utf-8') as out:
    out.writelines(latex_tables)

print("Generated BaoCao_KTPM_Mioto/generated_test_cases.tex successfully!")

