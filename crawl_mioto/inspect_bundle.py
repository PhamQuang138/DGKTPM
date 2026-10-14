import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

req = urllib.request.Request('https://www.mioto.vn', headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Find all script src
scripts = re.findall(r'<script[^>]+src=[\'"]([^\'"]+)[\'"]', html)
print("Found scripts:", scripts)

api_endpoints = set()
routes = set()

for s in scripts:
    url = s if s.startswith('http') else 'https://www.mioto.vn' + s
    print("Inspecting script:", url)
    try:
        s_req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(s_req) as s_resp:
            js = s_resp.read().decode('utf-8', errors='ignore')
            # Look for API paths
            apis = re.findall(r'[\'"](/api/[^\'"]+|\bhttps?://[^\'"]+api[^\'"]*)[\'"]', js)
            api_endpoints.update(apis)
            # Look for path strings / routes like /booking, /car/, /user, etc.
            found_routes = re.findall(r'[\'"](/[a-zA-Z0-9\-_]{2,30})[\'"]', js)
            for r in found_routes:
                if any(kw in r for kw in ['car', 'book', 'rent', 'user', 'auth', 'login', 'trip', 'profile', 'pay', 'order', 'notif', 'search', 'fav', 'policy', 'term', 'promo', 'voucher', 'wallet']):
                    routes.add(r)
    except Exception as e:
        print("Failed to inspect script", url, e)

print("Found API endpoints:", len(api_endpoints))
for a in list(api_endpoints)[:20]:
    print("  API:", a)

print("Found interesting routes:", len(routes))
for r in sorted(list(routes))[:40]:
    print("  Route:", r)

with open('crawl_mioto/routes_and_apis.json', 'w', encoding='utf-8') as f:
    json.dump({'apis': list(api_endpoints), 'routes': sorted(list(routes))}, f, ensure_ascii=False, indent=2)

