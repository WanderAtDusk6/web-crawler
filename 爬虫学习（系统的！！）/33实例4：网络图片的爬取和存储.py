# 实例4：网络图片的爬取和存储
import requests
import os

url = input("请输入URL:")
if url == "":
    url = "http://image.ngchina.com.cn/2018/0526/20180526123801934.jpg"

root = "F://爬取的图片//"
path = root + url.split('/')[-1]   # 取最后部分作为文件名
try:
    if not os.path.exists(root):
        os.mkdir(root)             # 创建目录
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
    r.raise_for_status()
        
