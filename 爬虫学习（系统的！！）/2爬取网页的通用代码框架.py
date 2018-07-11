# 爬取网页的通用代码框架
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200,引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    # url = "http://www.baidu.com"
    url = "http://jwxt.zust.edu.cn/xs_main_zzjk1.aspx?xh=1170199164&type=1"
    print(getHTMLText(url))
    url = input("请输入一个URL：")
    print(getHTMLText(url))
