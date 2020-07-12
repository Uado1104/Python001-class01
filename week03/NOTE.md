# 学习笔记-Scrapy框架解析
## Scrapy并发参数优化原理
### 区别
Requests库为同步请求，需要等待网页响应并下载数据后加载下一个网页。<br>
Scrapy为异步请求，通过settings.py参数调优

```
#默认最大的并发请求数为16
Configure maxium concurrent requests performed by Scrapy(default:16)
CONCURRENT_REQUESTS = 32
#考虑目标网站的性能承载问题、发起端的每台服务器的承载力

#Configure a delay for requests for the same website(default:0)
#设置下载的延时，防止爬取过快导致IP被封掉
DOWNLOAD_DELAY = 3

#针对域名和IP的并行爬取
#The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
```

### 多任务模型
分为同步模型和异步模型；
Scrapy使用的是Twisted模型，异步编程模型，任务之间相互独立，大量I/O密集操作

### 多进程模型
多进程、多线程、协程的目的都是尽可能多处理任务，产生新的进程如下：
```
os.fork()
multiprocessing.Process()
```

##
