# 中国大学排名定向爬虫_实例编写
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)   
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):    # 因为所有信息都封装在<tr>里过滤掉非标签类型的其他信息
            tds = tr('td')       # 存成列表，，，| <tag>(..) 等价于 <tag>.find_all(..)
            ulist.append([tds[0].string, tds[1].string, tds[3].string])      # 将大学的信息放入列表中
    #pass


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))   # ^表示右对齐
    for i in range(num):
        u = ulist[i]     # 这代表第i个学校的信息
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
    print("Suc" + str(num))
    
def main():
    uinfo = []    # 将大学信息放入一个列表中
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html" # 先试下2016
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)     # 20 Univ

main()
