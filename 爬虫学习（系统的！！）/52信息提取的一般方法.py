# 信息提取的一般方法

# 方法一: 完整解析信息的标记形式，再提取关键信息
"""XML JSON YAML
需要标记解析器 例如：bs4库的标签树遍历
优点： 信息解析准确
缺点： 提取过程繁琐，速度慢
"""
# 方法二： 无视标记形式
"""搜索
对信息文本查找函数即可
优点： 提取过程简洁，速度较快
缺点：提取结果准确性与内容信息相关
"""

# 以下为操作内容

>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> for link in soup.find_all("a"):
	print(link.get("href"))

	
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
