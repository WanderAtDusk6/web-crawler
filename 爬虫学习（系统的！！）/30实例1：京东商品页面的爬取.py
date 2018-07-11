# 实例1：京东商品页面的爬取

# 操作记录
'''
>>> import requests
>>> r = requests.get("http://item.jd.com/2967929.html")
>>> r.status_code
200
>>> r.encoding
'gbk'
'''
import requests
url = "http://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("异常,爬取失败")
