# 百度360搜索关键字提交
import requests
'''
百度的关键词接口：
    http://www.baidu.com/s?wd=keyword
360的关键词接口：
    http://www.so.com/s?q=keyword
'''
keyword = input("输入 搜索词: ")
print("="*20)
if keyword == "":
    keyword = "Python"
    
def _baidu_search():
    print("**百度：")
    try:
        kv = {'wd': keyword}   # 见上，百度的是wd
        r = requests.get("http://www.baidu.com/s", params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
         print(r.text[:2000])
        print("="*20)
    except:
        print("爬取失败")
def _360_search():
    print("**360:")
    try:
        kv = {'q': keyword}   # 见上，百度的是wd
        r = requests.get("http://www.so.com/s", params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
        print("="*20)
    except:
        print("爬取失败")
   
_baidu_search()
_360_search()
