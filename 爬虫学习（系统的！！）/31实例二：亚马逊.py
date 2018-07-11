#实例二：亚马逊
import requests

url = input("请输入一个URL：")
"""e.g.
https://www.amazon.cn/gp/product/B073LBRNV2?ref_=plp_web_a_A2XQOEEUXFBHEM_pc_2&me=A1AJ19PSB66TGU
"""
print()
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    print("headers: ", r.request.headers)
    r.raise_for_status()
    print("以下为详细信息：")
    print("原r.encoding: ",r.encoding)
    print("原r.apparent_encoding: ",r.apparent_encoding)
    r.encoding = r.apparent_encoding
    # print(r.text[1000: 2000])

except:
    print("爬取失败")
    
