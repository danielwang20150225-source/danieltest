import json
with open(r'C:\Users\danie\.openclaw\workspace\repos.json', 'r', encoding='utf-8') as f:
    repos = json.load(f)
for repo in repos:
    name = repo.get('name', '')
    if 'skill' in name.lower():
        print(f"{name} -> {repo.get('html_url', '')}")
