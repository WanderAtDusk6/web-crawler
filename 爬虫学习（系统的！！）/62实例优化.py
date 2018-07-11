#62实例优化
# 写在前面：（填充时）中西文字的宽度不同，造成了表格没有对齐
# 采用中文字符的空格填充 chr(12288)

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
    pass


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"   # e.g. {:{*}^10}   用*来填充
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))   # ^表示居中对齐
    for i in range(num):
        u = ulist[i]     # 这代表第i个学校的信息
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    print("Suc" + str(num))
    
def main():
    uinfo = []    # 将大学信息放入一个列表中
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html" # 先试下2016
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)     # 20 Univ

main()

