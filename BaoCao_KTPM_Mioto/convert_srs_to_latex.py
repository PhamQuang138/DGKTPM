import re

def escape_tex(text):
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('_', '\\_')
    text = text.replace('#', '\\#')
    return text

with open('BaoCao_KTPM_Mioto/chapters/02_kien_truc_va_dac_ta_yeu_cau.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
srs_rows = []
for l in lines:
    ls = l.strip()
    if ls.startswith('| **REQ-'):
        parts = [p.strip() for p in ls.split('|')[1:-1]]
        if len(parts) >= 5:
            req_id = parts[0].replace('**', '')
            req_mod = parts[1]
            req_name = parts[2]
            req_desc = parts[3].replace('<br/>', ' ')
            req_crit = parts[4].replace('<br/>', ' ')
            srs_rows.append({
                'id': req_id,
                'mod': req_mod,
                'name': req_name,
                'desc': req_desc,
                'crit': req_crit
            })

latex = []
latex.append("\\begin{longtable}{p{2.3cm}p{2.5cm}p{3cm}p{4.5cm}p{4.2cm}}\n")
latex.append("\\caption{Ma trận đặc tả 21 yêu cầu chức năng cốt lõi (SRS) hệ thống Mioto.vn} \\label{tab:srs_full_table} \\\\\n")
latex.append("\\toprule\n")
latex.append("\\textbf{Mã YC} & \\textbf{Phân hệ} & \\textbf{Tên chức năng} & \\textbf{Mô tả yêu cầu chi tiết} & \\textbf{Tiêu chí nghiệm thu} \\\\\n")
latex.append("\\midrule\n")
latex.append("\\endfirsthead\n\n")

latex.append("\\multicolumn{5}{c}{{\\bfseries \\tablename\\ \\thetable{} -- Tiếp tục từ trang trước}} \\\\\n")
latex.append("\\toprule\n")
latex.append("\\textbf{Mã YC} & \\textbf{Phân hệ} & \\textbf{Tên chức năng} & \\textbf{Mô tả yêu cầu chi tiết} & \\textbf{Tiêu chí nghiệm thu} \\\\\n")
latex.append("\\midrule\n")
latex.append("\\endhead\n\n")

latex.append("\\midrule \\multicolumn{5}{r}{{Còn tiếp ở trang sau...}} \\\\\n")
latex.append("\\endfoot\n\n")

latex.append("\\bottomrule\n")
latex.append("\\endlastfoot\n\n")

for r in srs_rows:
    rid = escape_tex(r['id'])
    rmod = escape_tex(r['mod'])
    rname = escape_tex(r['name'])
    rdesc = escape_tex(r['desc'])
    rcrit = escape_tex(r['crit'])
    latex.append(f"\\textbf{{{rid}}} & {rmod} & {rname} & {rdesc} & {rcrit} \\\\ \\midrule\n")

latex.append("\\end{longtable}\n")

with open('BaoCao_KTPM_Mioto/generated_srs_table.tex', 'w', encoding='utf-8') as out:
    out.writelines(latex)

print(f"Generated {len(srs_rows)} SRS rows to BaoCao_KTPM_Mioto/generated_srs_table.tex")
