"""Requests库的七个主要方法：
requests.request()：
    构造一个请求，支撑一下各方法的基础方法
    
requests.get()：
    获取HTML网页的主要方法，对应HTTP的GET
    
requests.head()：
    获取HTML网页头的信息方法，对应HTTP的HEAD
requests.post()：向HTML网页提交POST请求方法，对应HTTP的POST
requests.put()：向HTML网页提交PUT请求的方法，对应HTTP的RUT
requests.patch()：向HTML网页提交局部修改请求，对应于HTTP的PATCH
requests.delete()：向HTML页面提交删除请求,对应HTTP的DELETE
HTTP协议：
HTTP，Hypertext Transfer Protocol,超文本传输协议。
HTTP是一个基于“请求与响应”模式的，无状态的应用层协议。
HTTP协议采用URL作为定位网络资源的标识。
URL格式：http://host[:port][path]
host:合法的Internet主机域名或IP地址
port：端口号，缺省端口为80
path:请求资源的路径
URL是通过HTTP协议存取资源的Internet路径，一个URL对应一个数据资源。

HTTP协议对资源的操作：
GET：请求获取URL位置的资源
HEAD:请求获取URL位置资源的响应消息报告，即获得该资源的头部信息
POST：请求想URL位置的资源后附加新的数据
PUT：请求URL位置存储的一个资源，覆盖原URL位置的资源
PATCH：请求局部更新URL位置的资源，即改变该处资源的部分内容
DELETE：请求删除URL位置存储的资源

"""
##
HTTP协议：
HTTP，Hypertext Transfer Protocol,超文本传输协议。
HTTP是一个基于“请求与响应”模式的，无状态的应用层协议。
HTTP协议采用URL作为定位网络资源的标识。
URL格式：http://host[:port][path]
host:合法的Internet主机域名或IP地址
port：端口号，缺省端口为80
path:请求资源的路径
##

###requests.request(method,url,**kwargs)
"""
method：请求方式，对应get/put/post等7种
url：拟获取页面的url链接
**kwargs：控制访问参数，共13个
**kwargs：控制访问的参数，均为可选项:
params:字典或字节序列，作为参数增加到url中
例：kv={'key1':'value','key2':'value2'}
    r=requests.request('GET','http://python123.io/ws',params=kv)
    print(r.url)
http://python.io/ws?key1=value1&key2=value2
data:字典，字节序列或文件对象，作为Request的内容
json:JSON格式的数据，作为Request的内容
headers：字典，HTTP定制头（模拟浏览器进行访问）
cokies：字典或CpplieJar,Request中的cookie
auth:元祖，支持HTTP认证功能
files：字典类型，传输文件
timeout:设定超时时间，秒为单位
proxies:字典类型，设定访问代理服务器，可以增加登陆认证
allow_redirects:True//False，默认为True，重定向开关
stream:True/False,默认为True,获取内容立即下载开关
verify:True/False,默认为True，认证SSL证书开关
cert：本地SSL证书路径"""

# r = requests.get(url)
#     返回一个包含服务器资源的Response对象 |get() #构造一个向服务器请求资源的Request对象

# requests.get(url， params=None, **kwargs)
# url: 链接| params: url的额外参数，字典或字节流格式，可选|  **kwargs: 12个控制访问的参数，可选




