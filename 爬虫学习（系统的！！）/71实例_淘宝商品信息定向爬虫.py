# 实例_淘宝商品信息定向爬虫

import re
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    print("")


def parsePage(ilt, html):     # ilt:结果的列表类型
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d.]*\"',html)    # 价格
        tle = re.findall(r'\"raw_title\"\:\".*?\"',html)        # 名称
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])       # veiw_price : 软妹币 分割取后
            title = eval(tle[i].split(':')[1])       # 同上
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:8}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

    print("")


def main():
    goods = "书包"
    depth = 2   # e.g. 爬取这一页和下一页，深度为二
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []     # 结果信息保存在这里
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
