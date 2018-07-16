# 101"股票数据Scrapy爬虫"实例编写
"""步骤
1： 建立工程和Spider模板
2： 编写Spider
3： 编写ITEM Pipelines
"""

"""1建立工程和Spider模板
\>>>scrapy startproject BaiduStocks
\>>>cd BaiduStock
\>>>scrapy genspider stocks baidu.com
进一步修改spiders/stocks.py文件

"""
"""2编写Spider
配置stocks.py文件
修改对返回页面的处理
修改对新增URL爬取请求的处理
"""
# 接下来请转到Scrapy框架3
"""3编写Pipelines
配置pipelines.py文件
定义对爬取项(Scraped Item)的处理类
"""
#  转到Pipelines
"""配置ITEM_PIPELINES选项"""
# 然后开settings.py
"""找到ITEM_PIPELINES,
把那个类给改了"""
