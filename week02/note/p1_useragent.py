# pip install fake-useragent
from fake_useragent import UserAgent
# 从网络中请求目前常用的浏览器的User-agent，不去验证ver
ua = UserAgent(verify_ssl = False)

# 模拟不同的浏览器
print(f'Chrome浏览器: {ua.chrome}')
# print(ua.safari)
# print(ua.ie)

# 随机返回头部信息
print(f'随机浏览器: {ua.random}')