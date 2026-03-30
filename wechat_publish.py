# 微信公众号自动发布脚本

import requests
import json

APP_ID = "wx0ff149e5844778ef"
APP_SECRET = "d08f078f6a970ffaa5153793c100d3fa"

def get_access_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    r = requests.get(url)
    data = r.json()
    return data.get("access_token")

def upload_image(token, image_path):
    """上传图片获取media_id"""
    url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={token}"
    files = {'media': open(image_path, 'rb')}
    r = requests.post(url, files=files)
    return r.json()

def upload_thumb(token, image_path):
    """上传封面图片"""
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={token}&type=image"
    files = {'media': open(image_path, 'rb')}
    r = requests.post(url, files=files)
    return r.json()
    """创建草稿"""
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    articles = [{
        "title": title,
        "author": "虾仁",
        "content": content,
        "content_source_url": "",
        "digest": content[:120],
        "show_cover_pic": 1,
        "thumb_media_id": thumb_media_id or ""
    }]
    
    data = {"articles": articles}
    r = requests.post(url, json=data)
    return r.json()

def publish(token, media_id):
    """发布草稿"""
    url = f"https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token={token}"
    data = {"media_id": media_id}
    r = requests.post(url, json=data)
    return r.json()

# 测试
if __name__ == "__main__":
    print("1. 获取Token...")
    token = get_access_token()
    if not token:
        print("获取Token失败")
        exit(1)
    print(f"Token: {token[:20]}...")
    
    print("\n2. 创建草稿...")
    test_article = """
    <p>这是一篇测试文章</p>
    <p>来自OpenClaw自动发布</p>
    """
    result = create_draft(token, "测试文章-来自OpenClaw", test_article)
    print(result)
