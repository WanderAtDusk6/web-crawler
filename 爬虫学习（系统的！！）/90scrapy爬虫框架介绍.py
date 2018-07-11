# scrapy爬虫框架介绍
喵喵喵
Scrapy爬虫框架结构
“5+2”结构
'''                 spider |
item pipelines      engine + --   downloader
                    scheduler
    --: middleware
'''

Engine:   控制所有模块之间的数据流
          根据条件出发事件
Scheduler:   对所有爬取请求进行调度管理
Downloader:  根据请求下载网页
