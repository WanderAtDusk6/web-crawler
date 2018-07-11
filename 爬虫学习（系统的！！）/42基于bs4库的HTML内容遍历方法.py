# 基于bs4库的HTML内容遍历方法


# 标签树的下行遍历
属性         |   说明
.contents    |子节点的列表，把<tag>所有节点存入列表
.children    |子节点的迭代类型，与.contents类似，用于循环遍历子节点
.descendants |子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

# 标签树的上行遍历
## 注：html的父辈是它自己
.parent      |节点的父标签
.parents     |节点先辈标签的迭代类型，用于循环遍历先辈节点

# 标签树的平行遍历
## 注： 平行遍历发生在同一个父节点下的各节点间
.next_silibling    | 返回按照HTML文本顺序的下一个平行节点标签
.previous_siblings | 返回按照HTML文本顺序的上一个平行节点标签
.next_siblings     | 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings | 迭代类型，，，，，，，，，，，，前续，，，，，，，，

# 部分操作
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.head
<head><title>This is a python demo page</title></head>
>>> soup.head.contents
[<title>This is a python demo page</title>]
>>> soup.body.contents
['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
>>> len(_)
5
>>> soup.body.contents[1]
<p class="title"><b>The demo python introduces several python courses.</b></p>

# 标签树的下行遍历
for child in soup.body.children:
    print(child)    # 遍历子节点

for child in soup.body.descendants:
    print(child)    # 遍历子孙节点

# 标签树的上行遍历


    
