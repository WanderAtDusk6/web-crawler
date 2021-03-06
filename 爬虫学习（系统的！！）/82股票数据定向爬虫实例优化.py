# 股票数据定向爬虫实例优化

import requests
from bs4 import BeautifulSoup
import traceback
import re
# traceback是为了调试方便

def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200,引发HTTPError异常
        r.encoding = code         # !##此处更改
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    # 股票的列表类型 股票的URL网站
    count = 0     # 用于计数进度条 
    html = getHTMLText(stockURL,'GB2312')   # !#更
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')       # 找出所有的a标签
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])   # [[],[]]-->[,,,]
        except:
            continue
    return ""


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue     # 空页面跳过
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            if stockInfo is None:
                # print("测试自用")
                continue
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]}) #e.g.源码 <a class="bets-name" href="/stock/sz002415.html">海康威视 (<span>002415</span>)

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val          # 加入字典

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print("\r当前进度：{:.2f}%".format(count*100/len(lst)),end='')
        except:
            traceback.print_exc()   # 从traceback对象tb到文件打印异常信息和堆栈跟踪条目
            print("\r当前进度：{:.2f}%".format(count*100/len(lst)),end='')
            continue
    return ""


def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "F:\\PythonSaver2\\BaiduStockInfo.txt"
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
    print("爬完了请滴滴我")

main()