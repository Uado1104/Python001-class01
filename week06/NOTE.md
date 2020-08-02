学习笔记
学号: G20200343050044
姓名: uado233
班级: 2班
小组: 1组
作业&总结链接: https://github.com/Uado1104/Python001-class01/tree/master/week06

# 学习笔记-Django Web开发入门
## Django框架简介
1. 基于MVC设计模式、MTV框架，开源的Web应用框架，最初用于管理劳伦斯出版集团下的网站，2005年7月在BSD许可证下发布
2. 强调快速开发和代码复用DRY(Do Not Repeat Yourself)
3. 组件丰富：ORM（对象关系映射）映射类型来构建数据模型；URL支持正则表达式；模版可继承；内置用户认证，提供用户认证和权限功能；admin管理系统；内置表单模型、Cache缓存系统、国际化系统

### MTV框架模式
浏览器请求视图层，视图层执行，将响应反馈给浏览器
#### 视图
1. 接收请求
2. 调用模型
3. 调用Tempaltes模版
4. 将数据填充到模版上再响应

#### 模型
创建模型，执行Crud
#### 模版
****.html 

### Django的特点
采用MTV框架

## 创建项目和目录结构
### 启动Django
1. 创建Django项目
2. 创建应用程序
3. 启动

### 命令

```
django-admin startproject MyDjango
```
```
cd MyDjango/
```
```
python manage.py help
```
```
python manage.py startapp index
```
```
python manage.py runserver
# 运行Django
```
注意——DEBUG=True；调试模式
默认的端口为：127.0.0.1:/8000

```
python manage.py runserver 0.0.0.0:80
# 其他人可访问，访问端口为80
```
```
CONTROL-C
# 结束Django的开发环境
```

配置文件：项目路径；密钥；域名访问权限；App列表；静态资源，包括CSS、JavaScript图片；模版文件；数据库配置；缓存；中间件
#### 目录结构

find MyDjango/
MyDjango/
MyDjango/manage.py 命令行工具
MyDjango/MyDjango
MyDjango/MyDjango/__init__.py
MyDjango/MyDjango/settings.py 项目的配置文件
MyDjango/MyDjango/urls.py
MyDjango/MyDjango/wsgi.py

###
python manage.py help查看该工具的具体功能
python manage.py startapp index
index/migrations 数据库迁移文件夹
index/models.py 模型
index/apps.py 当前app配置文件
index/admin.py 管理后台
index/tests.py 自动化测试
index/views.py 视图

####
DEBUG=True 

## Django如何处理一个请求
### 当一个用户请求Django站点的页面：
1. 如果传入HttpRequest对象拥有urlconf属性（通过中间件设置），它的值将被用来替代ROOT_URLCONF设置。
2. Django加载URLconf模块并寻找可用的urlpartterns，Django依次匹配每个URL模式（可以支持正则表达式），在与请求的URL匹配的第一个模式停下来。
3. 一旦有URL匹配成功，Django导入并调用相关的视图，视图会获得如下参数：一个HttpRequest实例；一个或多个位置参数提供
4. 如果没有URL被匹配，或者匹配过程中出现了异常，Django会调用一个适当的错误处理视图。

```
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
	# 请求url路径，返回admin.site.urls
	path('admin/',admin.site.urls),
	# 不同功能分别创建app应用程序
	# 以下代码：当指定为空时，使用index.url来解析
	path('',include('index.urls')),
]
```
增加index的urls

```
# index/urls.py
from django.urls import path
# .表示相对路径，表示同一级别的文件的名称
from . import views

urlpatterns = [
	path('',viewss.index)
]

# index/view.py
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello Django!")
```
## 模块和包
### 模块
.py结尾的Python程序
### 包
存放多个模块的目录
### __init__.py
包运行的初始化文件，可以是空文件

### 以模块方式运行函数
```
def func1():
	print('import func1')
	
if __name__ == '__main__':
	func1()
```

Django支持对URL设置变量，URL变量类型包括：str;int;slug;uuid;path
接收不定长的参数：不用去指定几个，直接用**kwargs——关键数参数

## URL支持正则表达式
```
re_path('(?P<year>[0-9]{4}.html)',views.myyear,name='urlyear')
```

views.py
```
def myyear(request,year):
	return render(request,'yearview.html')
```
### 自定义过滤器

```
# 注册自定义过滤器'myint','yyyy'
register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')
```
converters指的是自己编写的文件

### views视图
#### 响应类型
1. HTTP状态码：

### Django常用快捷函数
#### render()
将给定的模版和给定的上下文字典绑定在一起，并以渲染的文本返回一个HttpResponse对象
#### redirect()
将一个HttpResponseRedirect返回到传递的参数的适当的URL
#### get_object_or_404()
在给定的模型管理器(model manager)上调用get()，但它会引发Http404而不是模型的DoesNotExist异常。

### manage.py makemigrations
把对应的class加上必要的功能转换成SQL表
### manage.py migration
1. 将必要的条件转换成Django能认得ORM的语句
2. 找到mySql客户端，export PATH=$PATH:/user/local/mysql/bin

model是数据来生成模型，view用来具体取出这些信息，template用于结合前端的框架，URLconf用
来转到页面