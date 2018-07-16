# "股票数据Scrapy爬虫"实例介绍

"""
技术路线：scrapy
目标：获取上交所和深交所所有股票的名称和交易信息

获取股票列表：
东方财富网： http://quote.eastmoney.com/stocklist.html
获取个股信息：
百度股票： https://gupiao.baidu.com/stock/
单个股票： https://gupiao.baidu.com/stock/sz002439.html
"""

#CSS Selector的基本使用
#<HTML>.css('a::attr(href)').extract()
#       标签名称     标签属性
