# Response对象的属性

'''前面有段内容放在 #笔记一 里'''
import requests
r = requests.get()

r.status_code
#    HTTP请求的访问状态，200表示连接成功，404表示失败
#    但，其实只要不是两百都算失败
r.text
#    HTTP相应内容的字符串形式，即，url对应页面内容

r.encoding
#    从HTTP header中 猜测出来的 响应内容的编码方式
# 服务器对资源编码（charset）有相关要求，就把这种编码存在r.en,,,,,里
# 但，并不是所有都有的，所以
# 如果header中不存在charset,则认为编码为'ISO-8859-1'

r.apparent_encoding
#    从 内容 中分析出响应内容编码方式（备选编码方式）

r.content
#    HTTP响应内容的二进制形式
