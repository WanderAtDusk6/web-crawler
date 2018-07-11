# HTTP协议及requests库方法

##
'''
HTTP协议：
HTTP，Hypertext Transfer Protocol,超文本传输协议。
HTTP是一个基于“请求与响应”模式的，无状态的应用层协议。
HTTP协议采用URL作为定位网络资源的标识。
URL格式：http://host[:port][path]
host:合法的Internet主机域名或IP地址
port：端口号，缺省端口为80
path:请求资源的路径
'''
HTTP协议对资源的操作：
GET：请求获取URL位置的资源
HEAD:请求获取URL位置资源的响应消息报告，即获得该资源的头部信息
POST：请求想URL位置的资源后附加新的数据
PUT：请求URL位置存储的一个资源，覆盖原URL位置的资源
PATCH：请求局部更新URL位置的资源，即改变该处资源的部分内容
DELETE：请求删除URL位置存储的资源

# requests库的
# head()方法操作记录
'''
>>> import requests
>>> r = requests.head('http://httpbin.org/get')
>>> r.headers
{'Connection': 'keep-alive', 'Server': 'gunicorn/19.8.1', 'Date': 'Sat, 26 May 2018 06:13:53 GMT', 'Content-Type': 'application/json', 'Content-Length': '209', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Via': '1.1 vegur'}
>>> r.text
''
'''

# post()方法操作记录
'''
>>> example = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.post("http://httpbin.org/post", data = example)
>>> print(r.text)
{"args":{},"data":"","files":{},"form":{"key1":"value1","key2":"value2"},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"23","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":null,"origin":"112.10.253.34","url":"http://httpbin.org/post"}
'''# 向该URL POST一个字典（键值对也行） 自动编码为form(表单)
'''
>>> r = requests.post("http://httpbin.org/post", data = "123")
>>> print(r.text)
{"args":{},"data":"123","files":{},"form":{},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"3","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":123,"origin":"112.10.253.34","url":"http://httpbin.org/post"}

'''# 向该URL POST一个字符串 自动编码为data
