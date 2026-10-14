import re
import json

with open('crawl_mioto/main_part.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Search API URLs
api_urls = set(re.findall(r'https?://[a-zA-Z0-9_\-\./]+(?:api|v1|v2|v3)[a-zA-Z0-9_\-\./]*', text))
print("Found API URLs:", api_urls)

# Search string literals starting with /
all_literals = set(re.findall(r'"(/[^"\\s]{2,40})"', text))
keywords = ['car', 'book', 'trip', 'rent', 'user', 'owner', 'pay', 'order', 'notif', 'search', 'fav', 'policy', 'term', 'promo', 'gift', 'blog', 'faq', 'about', 'guide', 'profile', 'login', 'register', 'city', 'filter', 'account', 'gplx', 'license']

routes = [r for r in all_literals if any(k in r.lower() for k in keywords)]
print(f"Total relevant routes: {len(routes)}")
for r in sorted(routes):
    print(" ", r)

with open('crawl_mioto/extracted_routes.json', 'w', encoding='utf-8') as out:
    json.dump({'apis': list(api_urls), 'routes': sorted(routes)}, out, ensure_ascii=False, indent=2)

