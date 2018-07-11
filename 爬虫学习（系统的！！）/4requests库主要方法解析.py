# requests库主要方法解析
import requests

###requests.request(method, url, **kwargs)
###
# r = requests.request("GET", url, **kwaargs)
# r = requests.request("HEAD", url, **kwaargs)
# POST PUT PATCH 同上
# r = requests.request("delete", url, **kwargs)
# # r = requests.request("OPTIONS", url, **kwaargs)

"""
method：请求方式，对应get/put/post等7种
url：拟获取页面的url链接

**kwargs：控制访问参数，共13个,|均为可选项|
:
1 params:字典或字节序列，作为参数增加到 url 中"""
##e.g.
 '''>>> import requests
>>> kv = {'key1': 'value1', 'key2': 'value2', 'ma': 'gua'}
>>> r = requests.request('GET', 'http://python123.io/ws', params=kv)
>>> print(r.url)
https://python123.io/ws?key1=value1&key2=value2&ma=gua'''
##
'''
2 data:字典，字节序列或文件对象，作为Request的内容
kv = {'key1': 'v1', 'key2': 'v2', 'ma': 'gua'}
>>> body = '主体内容'
>>> r = requests.request('POST', 'http://python123.io/ws', data=body)
'''
#3 json:JSON格式的数据，作为Request的内容
#4 headers：字典，HTTP定制头（模拟浏览器进行访问）
##e.g. 伪装成chrome10访问URL
'''>>> hd = {'user-agent': 'chrome/10'}
>>> r = requests.request('POST', 'http://python123.io/ws', headers=hd)'''
#5 cokies：字典或CoolieJar,Request中的cookie |R库的高级功能
##       从http协议中解析cookies
#6 auth: 元组，支持HTTP认证功能              |R库的高级功能
#7 files: 字典类型，传输文件
##e.g.  即： 向某一个链接，提供一个文件
'''fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', 'http://python123.io/ws', files=fs)'''
#8 timeout: 设定超时时间，秒为单位
##e.g. r = requests.request('POST', 'http://www.baidu.com', timeout=10)
#9 proxies: 字典类型，设定代理服务器，可以增加登录认证（用户名&密码）
##   （可用于隐藏自己的ip地址，防止对爬虫的逆追踪）
##e.g.
'''>>> pxs ={'http': 'http://user:pass@10.10.10.1:1234', 'https': 'https://10.10.10.1:4321'}
>>> r = requests.resquest('GET', 'http://www.baidu.com', proxies=pxs)'''# 注： 百度方无响应，翻车
#10 allow_redirects: True/False,默认为True,重定向开关
##                  （暂时碰不上，不管了）
#11 stream: True/False,默认为True,获取内容立即下载开关
#12 verify: True/False,默认为True，认证SSL证书开关
#13 cert: 本地SSL证书路径

requests.head(url, **kwargs)   # **13

requests.post(url, data=None, json=None, **kwargs)   # 见上

requests.put(url, data=None, **kwargs)

requests.patch(url, data=None, **kwargs)

requests.delete(url, **kwargs)    # url: 拟删除页面的url链接
# 全场最佳
requests.get(url, params=None, **kwargs)

