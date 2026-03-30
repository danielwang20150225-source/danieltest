$token = "t-g1043ciXD4BDSFMLODEXYJEY6FQCFUKCHYVGL2HY"
# 尝试带文档类型前缀的方式
$body = '{"member_id":"ou_0e0a80c4361f24e4d431bf7b838ec802","member_id_type":"openid","perm":"full_access"}'
Invoke-RestMethod -Uri "https://open.feishu.cn/open-apis/drive/v1/permissions/docx_EzfadPw9poDjFNxMZigcZHsSnnb/members" -Method POST -Headers @{"Authorization"="Bearer $token"} -Body $body -ContentType "application/json"
