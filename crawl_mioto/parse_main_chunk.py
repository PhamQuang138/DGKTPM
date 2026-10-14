import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
js_url = 'https://www.mioto.vn/static/js/main.bd284d10.chunk.js'

try:
    req = urllib.request.Request(js_url, headers=headers)
    data = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
    
    pattern = re.compile(r'"(/[a-zA-Z0-9_\-/]+)"')
    matches = pattern.findall(data)
    keywords = ['car', 'book', 'trip', 'user', 'auth', 'noti', 'coupon', 'fav', 'contract', 'insur', 'pay', 'v2', 'v1', 'api', 'register', 'login', 'gplx', 'license', 'driver', 'rating', 'feedback', 'cancel', 'policy']
    
    unique_paths = sorted(list(set([m for m in matches if len(m) > 2 and any(w in m.lower() for w in keywords)])))
    print(f"Total matching paths: {len(unique_paths)}")
    for p in unique_paths[:60]:
        print(p)
        
    with open('crawl_mioto/main_paths.json', 'w', encoding='utf-8') as f:
        json.dump(unique_paths, f, ensure_ascii=False, indent=2)
except Exception as e:
    print("Error:", e)

