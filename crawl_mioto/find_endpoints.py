import re
import json

with open('crawl_mioto/main_part.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for function calls that build API requests
# In React/Redux apps, they often have api callers like:
# api.get('/path'), request('/path'), etc.
endpoints = re.findall(r'["\'](/api/[^"\']+|/v[12]/[^"\']+)["\']', text)
print("Endpoints with /api/ or /v1/:", set(endpoints))

# Look for all strings matching /...
all_paths = set(re.findall(r'["\'](/[a-zA-Z0-9_\-\./]{3,50})["\']', text))
car_paths = [p for p in all_paths if any(k in p for k in ['car', 'booking', 'trip', 'rent', 'user', 'owner', 'wallet', 'bill', 'insurance', 'coupon', 'gplx'])]
print(f"Total matching paths: {len(car_paths)}")
for p in sorted(car_paths):
    print("  ", p)

with open('crawl_mioto/detailed_paths.json', 'w', encoding='utf-8') as f:
    json.dump({'all_paths': sorted(car_paths)}, f, ensure_ascii=False, indent=2)

