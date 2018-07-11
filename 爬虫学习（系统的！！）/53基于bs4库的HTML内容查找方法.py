# 基于bs4库的HTML内容查找方法

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")

# 注： find_all()是针对标签（tag）的方法  
# <>.find_all(name, attrs, recursive, string, **kwargs)
#返回一个列表类型，存储查找的结果
#name: 对标签名称的检索字符串
#attrs: 对标签属性值的检索字符串，可标注属性检索
#recursive: 是否对子孙全部检索，默认为True
#string: <>...</>中字符串区域检索字符串


###
# <tag>(..) 等价于 <tag>.find_all(..)
# soup(..) 等价于 soup.find_all(..)
# for tag in soup.find_all()

### 同时，还有些扩展方法（mmp码不动了，copy一下）
'''

<>.find()         | 搜索并只返回一个结果，字符串类型，同.find_all()参数
<>.find_parents() | 在先辈节点中搜索，返回列表类型，同.find_all()参数
<>.find_parent()  | 在先辈节点中返回一个结果，字符串类型，同.find()参数
<>.find_next_siblings()  |          ,,         列表类型    ,,
<>.find_next_sibling     |            ,,        字符串     ,,
<>.find_previous_siblings()  |      ,,          列表    ,,
<>.find_previous_sibling()   |                   字符串
'''


>>> soup.find_all("a")
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
>>> soup.find_all(['a', 'b'])
[<b>The demo python introduces several python courses.</b>, <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]

>>> for tag in soup.find_all(True):
	print(tag.name)

	
html
head
title
body
p
b
p
a
a
###
import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
soup.find_all("p", "course")
Out[7]: 
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
 <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]
soup.find_all(id="link2")
Out[8]: [<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
soup.find_all(href="http://www.icourse163.org/course/BIT-1001870001")
Out[9]: [<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
import re
soup.find_all(id=re.compile('link'))
Out[11]: 
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>,
 <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
soup.find_all('a')
Out[12]: 
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>,
 <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
soup.find_all('a', recursive=False)
Out[13]: []
soup.prettify()
Out[14]: '<html>\n <head>\n  <title>\n   This is a python demo page\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The demo python introduces several python courses.\n   </b>\n  </p>\n  <p class="course">\n   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\n   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">\n    Basic Python\n   </a>\n   and\n   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">\n    Advanced Python\n   </a>\n   .\n  </p>\n </body>\n</html>'
print(soup.prettify())
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
soup.find_all(string= "Basic Python")
Out[16]: ['Basic Python']
soup.find_all(string= re.compile("python"))
Out[17]: 
['This is a python demo page',
 'The demo python introduces several python courses.']
