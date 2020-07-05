# http 协议的 GET 方法
import requests
r = requests.get('http://github.com') 
r.status_code
# 获取headers信息
r.headers['content-type']
# r.text
r.encoding
# r.json()

# http协议的POST方法
import requests
r = requests.post('http://httpbin.org/post',data = {'key':'value'})
r.json()