# IP地址归属地的自动查询
import requests
"http://m.ip138.com/ip.asp?ip=101.200.44.73"

url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")

