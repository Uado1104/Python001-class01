# 基于twisted的异步IO框架
# 事件的循环，while(true)，先执行代码，在请求有结果后进行回调，再重复执行代码；如果没有结果，进入下一个循环
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor
# 接收key-value形式的参数
def response(*args, **kwargs):
    # print(args,kwarg)
    print ('返回页面的内容')

def callback(*args):
    print('执行了一个回调',args)
#装饰器
@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode('utf-8'))
    d.addCallback(response)
    d.addCallback(callback)
    yield d

def stop(*args, **kwargs):
    reactor.stop()

urls = ['http://www.baidu.com','http://www.sougou.com']
li = []

for url in urls:
    ret = start(url)
    li.append(ret)
print(li)

d = defer.DeferredList(li)
d.addBoth(stop)
reactor.run()
