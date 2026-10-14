import re

def escape_tex(text):
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('_', '\\_')
    text = text.replace('#', '\\#')
    return text

with open('BaoCao_KTPM_Mioto/chapters/08_quan_ly_loi_rtm.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
rtm_rows = []
for l in lines:
    ls = l.strip()
    if ls.startswith('| **REQ-'):
        parts = [p.strip() for p in ls.split('|')[1:-1]]
        if len(parts) >= 5:
            req_id = parts[0].replace('**', '')
            req_name = parts[1]
            req_tcs = parts[2].replace('`', '')
            req_exec = parts[3]
            req_res = parts[4].replace('**', '')
            rtm_rows.append({
                'id': req_id,
                'name': req_name,
                'tcs': req_tcs,
                'exec': req_exec,
                'res': req_res
            })

latex = []
latex.append("\\begin{longtable}{p{2.5cm}p{4cm}p{6.5cm}p{1.8cm}p{1.8cm}}\n")
latex.append("\\caption{Ma trận truy xuất nguồn gốc yêu cầu (Requirements Traceability Matrix - RTM)} \\label{tab:rtm_full_table} \\\\\n")
latex.append("\\toprule\n")
latex.append("\\textbf{Mã YC} & \\textbf{Tên chức năng} & \\textbf{Các ca kiểm thử liên kết (Test Cases)} & \\textbf{Thực thi} & \\textbf{Kết quả} \\\\\n")
latex.append("\\midrule\n")
latex.append("\\endfirsthead\n\n")

latex.append("\\multicolumn{5}{c}{{\\bfseries \\tablename\\ \\thetable{} -- Tiếp tục từ trang trước}} \\\\\n")
latex.append("\\toprule\n")
latex.append("\\textbf{Mã YC} & \\textbf{Tên chức năng} & \\textbf{Các ca kiểm thử liên kết (Test Cases)} & \\textbf{Thực thi} & \\textbf{Kết quả} \\\\\n")
latex.append("\\midrule\n")
latex.append("\\endhead\n\n")

latex.append("\\midrule \\multicolumn{5}{r}{{Còn tiếp ở trang sau...}} \\\\\n")
latex.append("\\endfoot\n\n")

latex.append("\\bottomrule\n")
latex.append("\\endlastfoot\n\n")

for r in rtm_rows:
    rid = escape_tex(r['id'])
    rname = escape_tex(r['name'])
    rtcs = escape_tex(r['tcs'])
    rexec = escape_tex(r['exec'])
    rres = escape_tex(r['res'])
    latex.append(f"\\textbf{{{rid}}} & {rname} & {rtcs} & {rexec} & \\textbf{{{rres}}} \\\\ \\midrule\n")

latex.append("\\end{longtable}\n")

with open('BaoCao_KTPM_Mioto/generated_rtm_table.tex', 'w', encoding='utf-8') as out:
    out.writelines(latex)

print(f"Generated {len(rtm_rows)} RTM rows to BaoCao_KTPM_Mioto/generated_rtm_table.tex")

