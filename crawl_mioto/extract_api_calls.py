import re
import json

with open('crawl_mioto/main_part.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Pattern for axios requests
pattern = re.compile(r'method:\s*["\']([A-Z]+)["\'],\s*url:\s*""\.concat\(([^)]+)\)')
matches = pattern.findall(text)
print(f"Total API callers found: {len(matches)}")

api_list = []
for m, u in matches:
    clean_u = u.replace('"', '').replace("'", "")
    api_list.append({'method': m, 'url_expr': clean_u})
    print(f"{m:6} -> {clean_u}")

with open('crawl_mioto/api_calls.json', 'w', encoding='utf-8') as f:
    json.dump(api_list, f, ensure_ascii=False, indent=2)

