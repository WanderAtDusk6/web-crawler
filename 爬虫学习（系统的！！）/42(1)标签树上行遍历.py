# 42(1)标签树上行遍历
from bs4 import BeautifulSoup
import requests

r = requests.get(url="http://python123.io/ws/demo.html",
                         timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text)

demo = r.text
#>>>demo
soup = BeautifulSoup(demo, "html.parser")
print("="*20)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
