import re

def clean_latex_text(text):
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('_', '\\_')
    text = text.replace('#', '\\#')
    # Replace broken arrows or weird chars
    text = text.replace('->', '$\\to$')
    text = text.replace('>=', '$\\ge$')
    text = text.replace('<=', '$\\le$')
    text = text.replace('>', '$>$')
    text = text.replace('<', '$<$')
    return text

# 1. Regenerate generated_test_cases.tex
with open('BaoCao_KTPM_Mioto/chapters/04_bo_ca_kiem_thu_chuc_nang.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

table_rows = []
for line in lines:
    line_s = line.strip()
    if line_s.startswith('| **TC-'):
        parts = [p.strip() for p in line_s.split('|')[1:-1]]
        if len(parts) >= 7:
            tc_id = parts[0].replace('**', '')
            tc_name = parts[1]
            tc_steps = parts[4].replace('<br/>', ' ')
            tc_exp = parts[5].replace('<br/>', ' ')
            table_rows.append({
                'id': tc_id,
                'name': tc_name,
                'steps': tc_steps,
                'exp': tc_exp
            })

tc_tex = []
tc_tex.append("\\section{Danh sách 68 Ca Kiểm thử Chức năng Chi tiết Toàn diện}\n")
tc_tex.append("Dưới đây là bảng đặc tả chi tiết của toàn bộ các ca kiểm thử chức năng được thiết kế cho hệ sinh thái Mioto.vn, chuẩn hóa theo chuẩn quốc tế IEEE 829:\n\n")
tc_tex.append("{\\small\n")
tc_tex.append("\\begin{longtable}{p{2.3cm}p{3.8cm}p{4.8cm}p{4.2cm}}\n")
tc_tex.append("\\caption{Danh mục chi tiết 68 ca kiểm thử chức năng hệ thống Mioto.vn} \\label{tab:full_test_cases} \\\\\n")
tc_tex.append("\\toprule\n")
tc_tex.append("\\textbf{Mã TC} & \\textbf{Tên ca kiểm thử} & \\textbf{Các bước \& Dữ liệu (Steps)} & \\textbf{Kỳ vọng (Expected Result)} \\\\\n")
tc_tex.append("\\midrule\n")
tc_tex.append("\\endfirsthead\n\n")

tc_tex.append("\\multicolumn{4}{c}{{\\bfseries \\tablename\\ \\thetable{} -- Tiếp tục từ trang trước}} \\\\\n")
tc_tex.append("\\toprule\n")
tc_tex.append("\\textbf{Mã TC} & \\textbf{Tên ca kiểm thử} & \\textbf{Các bước \& Dữ liệu (Steps)} & \\textbf{Kỳ vọng (Expected Result)} \\\\\n")
tc_tex.append("\\midrule\n")
tc_tex.append("\\endhead\n\n")

tc_tex.append("\\midrule \\multicolumn{4}{r}{{\\slshape Còn tiếp ở trang sau...}} \\\\\n")
tc_tex.append("\\endfoot\n\n")

tc_tex.append("\\bottomrule\n")
tc_tex.append("\\endlastfoot\n\n")

for row in table_rows:
    cid = clean_latex_text(row['id'])
    cname = clean_latex_text(row['name'])
    csteps = clean_latex_text(row['steps'])
    cexp = clean_latex_text(row['exp'])
    tc_tex.append(f"\\textbf{{{cid}}} & {cname} & {csteps} & {cexp} \\\\ \\midrule\n")

tc_tex.append("\\end{longtable}\n")
tc_tex.append("}\n")

with open('BaoCao_KTPM_Mioto/generated_test_cases.tex', 'w', encoding='utf-8') as out:
    out.writelines(tc_tex)

print(f"Generated {len(table_rows)} test cases cleanly.")

# 2. Regenerate generated_srs_table.tex
with open('BaoCao_KTPM_Mioto/chapters/02_kien_truc_va_dac_ta_yeu_cau.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

srs_rows = []
for l in lines:
    ls = l.strip()
    if ls.startswith('| **REQ-'):
        parts = [p.strip() for p in ls.split('|')[1:-1]]
        if len(parts) >= 5:
            srs_rows.append({
                'id': parts[0].replace('**', ''),
                'mod': parts[1],
                'name': parts[2],
                'desc': parts[3].replace('<br/>', ' '),
                'crit': parts[4].replace('<br/>', ' ')
            })

srs_tex = []
srs_tex.append("{\\small\n")
srs_tex.append("\\begin{longtable}{p{2.3cm}p{2.2cm}p{2.8cm}p{4.2cm}p{3.8cm}}\n")
srs_tex.append("\\caption{Ma trận đặc tả 21 yêu cầu chức năng cốt lõi (SRS) hệ thống Mioto.vn} \\label{tab:srs_full_table} \\\\\n")
srs_tex.append("\\toprule\n")
srs_tex.append("\\textbf{Mã YC} & \\textbf{Phân hệ} & \\textbf{Tên chức năng} & \\textbf{Mô tả yêu cầu chi tiết} & \\textbf{Tiêu chí nghiệm thu} \\\\\n")
srs_tex.append("\\midrule\n")
srs_tex.append("\\endfirsthead\n\n")

srs_tex.append("\\multicolumn{5}{c}{{\\bfseries \\tablename\\ \\thetable{} -- Tiếp tục từ trang trước}} \\\\\n")
srs_tex.append("\\toprule\n")
srs_tex.append("\\textbf{Mã YC} & \\textbf{Phân hệ} & \\textbf{Tên chức năng} & \\textbf{Mô tả yêu cầu chi tiết} & \\textbf{Tiêu chí nghiệm thu} \\\\\n")
srs_tex.append("\\midrule\n")
srs_tex.append("\\endhead\n\n")

srs_tex.append("\\midrule \\multicolumn{5}{r}{{\\slshape Còn tiếp ở trang sau...}} \\\\\n")
srs_tex.append("\\endfoot\n\n")

srs_tex.append("\\bottomrule\n")
srs_tex.append("\\endlastfoot\n\n")

for r in srs_rows:
    rid = clean_latex_text(r['id'])
    rmod = clean_latex_text(r['mod'])
    rname = clean_latex_text(r['name'])
    rdesc = clean_latex_text(r['desc'])
    rcrit = clean_latex_text(r['crit'])
    srs_tex.append(f"\\textbf{{{rid}}} & {rmod} & {rname} & {rdesc} & {rcrit} \\\\ \\midrule\n")

srs_tex.append("\\end{longtable}\n")
srs_tex.append("}\n")

with open('BaoCao_KTPM_Mioto/generated_srs_table.tex', 'w', encoding='utf-8') as out:
    out.writelines(srs_tex)

print(f"Generated {len(srs_rows)} SRS rows cleanly.")

# 3. Regenerate generated_rtm_table.tex
with open('BaoCao_KTPM_Mioto/chapters/08_quan_ly_loi_rtm.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

rtm_rows = []
for l in lines:
    ls = l.strip()
    if ls.startswith('| **REQ-'):
        parts = [p.strip() for p in ls.split('|')[1:-1]]
        if len(parts) >= 5:
            rtm_rows.append({
                'id': parts[0].replace('**', ''),
                'name': parts[1],
                'tcs': parts[2].replace('`', ''),
                'exec': parts[3],
                'res': parts[4].replace('**', '')
            })

rtm_tex = []
rtm_tex.append("{\\small\n")
rtm_tex.append("\\begin{longtable}{p{2.3cm}p{3.5cm}p{5.8cm}p{1.7cm}p{1.8cm}}\n")
rtm_tex.append("\\caption{Ma trận truy xuất nguồn gốc yêu cầu (Requirements Traceability Matrix - RTM)} \\label{tab:rtm_full_table} \\\\\n")
rtm_tex.append("\\toprule\n")
rtm_tex.append("\\textbf{Mã YC} & \\textbf{Tên chức năng} & \\textbf{Các ca kiểm thử liên kết (Test Cases)} & \\textbf{Thực thi} & \\textbf{Kết quả} \\\\\n")
rtm_tex.append("\\midrule\n")
rtm_tex.append("\\endfirsthead\n\n")

rtm_tex.append("\\multicolumn{5}{c}{{\\bfseries \\tablename\\ \\thetable{} -- Tiếp tục từ trang trước}} \\\\\n")
rtm_tex.append("\\toprule\n")
rtm_tex.append("\\textbf{Mã YC} & \\textbf{Tên chức năng} & \\textbf{Các ca kiểm thử liên kết (Test Cases)} & \\textbf{Thực thi} & \\textbf{Kết quả} \\\\\n")
rtm_tex.append("\\midrule\n")
rtm_tex.append("\\endhead\n\n")

rtm_tex.append("\\midrule \\multicolumn{5}{r}{{\\slshape Còn tiếp ở trang sau...}} \\\\\n")
rtm_tex.append("\\endfoot\n\n")

rtm_tex.append("\\bottomrule\n")
rtm_tex.append("\\endlastfoot\n\n")

for r in rtm_rows:
    rid = clean_latex_text(r['id'])
    rname = clean_latex_text(r['name'])
    rtcs = clean_latex_text(r['tcs'])
    rexec = clean_latex_text(r['exec'])
    rres = clean_latex_text(r['res'])
    rtm_tex.append(f"\\textbf{{{rid}}} & {rname} & {rtcs} & {rexec} & \\textbf{{{rres}}} \\\\ \\midrule\n")

rtm_tex.append("\\end{longtable}\n")
rtm_tex.append("}\n")

with open('BaoCao_KTPM_Mioto/generated_rtm_table.tex', 'w', encoding='utf-8') as out:
    out.writelines(rtm_tex)

print(f"Generated {len(rtm_rows)} RTM rows cleanly.")

