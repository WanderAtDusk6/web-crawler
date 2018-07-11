# BeautifulSoup库的基本元素

## mmp怕是要把这个当成txt来用了
'''
http://python123.io/ws/demo.html
'''

<p>...</p>  : 标签 Tag

       <p class="title">....</p>
名称 Name | 属性Attributes  | 名称（同前）
成对出现  | 0个或多个       |

# beautifulSoup库解析器
解析器           |  使用方法                         |  条件  
bs4的HTML解析器  |  BeaurifulSoup(mk, 'html.parser') | 安装bs4库
lxml的HTML解析器 |  BeautifulSoup(mk, 'lxml')        | pip install lxml
lxml的XML解析器  |  BeautifulSoup(mk, 'xml')         | pip intsall lxml
html5lib的解析器 |  BeautifulSoup(mk, 'html5lib')    | pip install html5lib

# BeautifulSoup类的基本元素
Tag        |标签：最基本的信息组织单元，分别用<></>表明开头和结尾
Name       |标签的名字： <p>..</p>的名字是'p',格式：<tag>.name
Attributes |标签的属性。字典形式组织，格式：<tag>.attrs
NavigableString |标签内非属性字符串，<>...</>中字符串，格式：<tag>.string
Comment	   |标签内字符串的注释部分，一种特殊的Comment类型
           | <b><!--This is a comment--></b>

'''
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.title
<title>This is a python demo page</title>
'''  # title: 浏览器上方标签页的题目





# 操作记录
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")

>>> import requests
>>> r = requests.get("http://python123.io/ws/demo.html")
>>> demo = r.text
>>> demo
'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p class="title"><b>The demo python introduces several python courses.</b></p>\r\n<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>\r\n</body></html>'

>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.title
<title>This is a python demo page</title>
>>> tag = soup.a
>>> tag
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
>>> soup.a.name
'a'
>>> soup.a.parent.name
'p'
>>> soup.a.parent.parent.name
'body'
>>> tag = soup.a
>>> tag.attrs
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
>>> tag.attrs["class"]
['py1']
>>> tag.attrs["href"]
'http://www.icourse163.org/course/BIT-268001'
>>> type(tag.attrs)
<class 'dict'>
>>> soup.a
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
>>> soup.a.string
'Basic Python'
>>> soup.p
<p class="title"><b>The demo python introduces several python courses.</b></p>
>>> soup.p.string
'The demo python introduces several python courses.'
>>> type(soup.p.string)
<class 'bs4.element.NavigableString'>
>>> newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", 'html.parser')
>>> newsoup.b.string
'This is a comment'
>>> type(_)
<class 'bs4.element.Comment'>
>>> newsoup.p.string
'This is not a comment'
>>> type(_)
<class 'bs4.element.NavigableString'>
