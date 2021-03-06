git clone http://gitee.com/wilsonyin/pythontrain.git
学习笔记
学号: G20200343050044
姓名: uado233
班级: 2班
小组: 1组
作业&总结链接: https://github.com/Uado1104/Python001-class01/tree/master/week03

# 第二周学习笔记
## 掌握Scrapy框架
```
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
```
```
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
```
```
import requests
# 在同一个Session实例发出的所有请求之间保持 cookie
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncoolie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncoolie/123456789')

```
```
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl = False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'http://account.douban.com/passport/login_popup?login_source=anomy'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持cookie
# 期间使用 urbllib3 的connection polling 功能
# 向同一个主机发送多个请求，底层的TCP连接将会被重用，从而带来显著的性能提升
login_url = 'http://account.douban.com/j/mobile/login/basic'
form_data = {
'ck':'',
'name':'15055495@qq.com',
'password':'test123456',
'remember':'false',
'ticket':''
}

response = s.post(login_url, data= form_data,headers = headers)

# 登陆后可以进行后续的请求
# url2 = 'http://account.douban.com/passport/setting'
# response2 = s.get(url2,headers = headers)
# response3 = newSession.get(url3,headers = headers,cookies = s.cookies)
# with open('profile.html','w+')as f:
    # f.write(response2.text)
```
```
 自定义一个异常类，继承Exception类
class UserInputError(Exception):
    # __init__函数在类刚一执行时就运行，ErroInfo用作错误信息的返回
    def __init__(self,ErroInfo):
        super().__init__(self,ErroInfo)
        self.errorinfo = ErroInfo
    # 魔术方法，使得类像字符串一样去使用
    def __str__(self):
        return self.errorinfo

userinput = 'a'

try:
    if(not userinput.isdigit()):
        # 抛出异常
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
# 无论程序错误有无捕获，都执行,把使用的内存清理掉。
finally:
    del userinput
```
```
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver ，和浏览器的版本保持一致
    # https://chromedriver.storage.googleapis.com/index.html

    browser.get('http://www.douban.com')
    time.sleep(1)
    # 切换登陆的输入框
    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    # 找到密码登陆输入框
    btm1 = browser.find_elements_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    # 模拟鼠标点击
    btm1.click()
    # 使用xpath找到账号密码的输入栏
    btm1 = browser.find_elements_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_elements_by_id('password').send_keys('test123test456')
    time_sleep(1)
    # 使用xpath找到登陆按钮
    browser.find_elements_by_xpath('//a[contains(@class,"btn-account")]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
# finally:
#     browser.close()
```

## 下载中间件
1.```process_request(request,spider)```<br>
request对象经过下载中间件时会被调用，优先级高先调用。
2.```proecess_reponse(request,response,spider)```<br>
response对象经过下载中间件时会被调用，优先级高后调用
3.```process_exception(request,exception,spider)```<br>
当process_response()和process_request()抛出异常时会被调用
4.```from_crawler(cls,crawler)```<br>
使用crawler来创建中间器对象，并（必须）返回一个中间件对象
### 具体步骤
1. 在scrapy框架中找到settings.py文件
2. 改写DOWNLOADER_MIDDLEWARES
3. ```spider.middlewares.RandomHttpProxyMiddleware```spider为项目名称，middlewares为其中一个配置文件middlewares.py
```
DOWNLOADER_MIDDLEWARES = {
    'spiders.middlewares.SpidersDownloaderMiddleware': 543,
    'spider.middlewares.RandomHttpProxyMiddleware':400,
}
HTTP_PROXY_LIST = {
    'http://52.179.231.206:80',
    'http://95.0.194.241:9090',
}
```

## 进程间的通信
进程间主要的共享方式为：队列、管道、共享内存；资源的抢占：加锁机制
### 共享方式
全局变量在多个进程中不能共享：在子进程中修改全局变量对父进程中的全局变量没有影响，因为父进程在创建子进程时对全局变量做了一个变量，所以父进程中的全局变量与子进程的全局变量完全是不同的两个变量。

### multiprocessing通信
multiprocessing支持进程之间的两种通信通道，Queue。