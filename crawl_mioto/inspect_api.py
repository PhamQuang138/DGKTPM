import re
import json

with open('crawl_mioto/main_part.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Look for patterns like axios, fetch, or apiUrl definitions
url_defs = re.findall(r'[a-zA-Z0-9_]+URL\s*[:=]\s*["\']([^"\']+)["\']', text)
print("URL definitions:", set(url_defs))

# Look for domains
domains = re.findall(r'https?://[a-zA-Z0-9_\-\.]+\.[a-z]{2,5}', text)
print("Domains:", set(domains))

# Look for strings containing "api" or "request"
api_patterns = re.findall(r'["\'](https?://[^"\']*(?:api|mioto)[^"\']*)["\']', text)
print("API candidates:", set(api_patterns[:20]))

# Search for state / redux / dispatch / actions
actions = re.findall(r'type:\s*["\']([A-Z0-9_]{3,30})["\']', text)
print("Redux actions sample:", set(actions[:30]))

