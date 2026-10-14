import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

urls = [
    'https://www.mioto.vn',
    'https://www.mioto.vn/about-us',
    'https://www.mioto.vn/how-it-works',
    'https://www.mioto.vn/policy',
    'https://www.mioto.vn/insurance',
    'https://www.mioto.vn/owner',
    'https://www.mioto.vn/guide-booking',
    'https://www.mioto.vn/faq'
]

results = {}
for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            title = re.search(r'<title>(.*?)</title>', html, re.I)
            # Find links
            links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
            internal_links = list(set([l for l in links if l.startswith('/') or 'mioto.vn' in l]))
            results[u] = {
                'status': resp.status,
                'title': title.group(1) if title else '',
                'internal_links': internal_links[:20],
                'html_len': len(html)
            }
            print(f"Fetched {u}: {title.group(1) if title else 'No Title'} ({len(html)} bytes)")
    except Exception as e:
        print(f"Failed {u}: {e}")

with open('crawl_mioto/crawl_summary.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved summary to crawl_mioto/crawl_summary.json")

