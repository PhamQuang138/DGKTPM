import re
import json

with open('crawl_mioto/main_part.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find all action strings
actions = sorted(list(set(re.findall(r'type:\s*["\']([A-Z0-9_]{3,40})["\']', text))))
print(f"Total redux action types: {len(actions)}")
for a in actions:
    print(a)

# Find HTTP method patterns like .get( , .post( , axios.post(
calls = re.findall(r'\.(get|post|put|delete)\(["\']([^"\']+)["\']', text)
print(f"\nDirect HTTP calls: {len(calls)}")
for m, url in set(calls):
    print(f"  {m.upper()} {url}")

with open('crawl_mioto/actions_and_methods.json', 'w', encoding='utf-8') as out:
    json.dump({'actions': actions, 'calls': list(set(calls))}, out, ensure_ascii=False, indent=2)

