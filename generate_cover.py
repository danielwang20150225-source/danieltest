import requests
import json

url = 'https://ark.cn-beijing.volces.com/api/v3/images/generations'
headers = {
    'Authorization': 'Bearer daf16924-b6b6-4bd1-bd72-cdd6666d4e5b',
    'Content-Type': 'application/json'
}
data = {
    'model': 'doubao-seedream-4-0-250828',
    'prompt': '公众号封面图：当AI学会自己上网。科技感风格，一个AI机器人正在操作电脑上网，蓝色主色调，现代简约设计。包含标题文字：Web Access Skill - 当AI学会自己上网。16:9宽屏比例，清晰干净',
    'size': '1920x1080',
    'quality': 'standard'
}

print("正在生成封面图...")
resp = requests.post(url, headers=headers, json=data, timeout=120)
print(f"Status: {resp.status_code}")

if resp.status_code == 200:
    result = resp.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # 保存结果
    with open('C:/Users/danie/.openclaw/workspace/cover-result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, indent=2, ensure_ascii=False))
else:
    print(f"Error: {resp.text[:1000]}")
