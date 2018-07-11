# requests库的异常
import requests

requests.ConnectionError
#    网络连接错误异常，如DNS查询失败，拒绝连接等

requests.HTTPError
#    HTTP错误异常

requests.URLRequired
#    URL缺失异常

requests.TooManyRedirects
#    超过最大重定向次数，产生重定向异常
# 即超过了requests库的要求，常见于比较复杂的链接

requests.ConnectTimeout
#    连接远程服务器超时异常

requests.Timeout
#     请求URL超时，产生超时异常
# 与r.CT的区别： 发出url到接到内容整个的过程的超时

r.raise_for_status()
#    如果不是200，产生异常requests.HTTPError
