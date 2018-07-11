# 麻瓜爬虫二号
import os
import urllib.request
import scrapy

class MySpider(scrapy.spiders.Spider):
    # 爬虫的名字，每只爬虫必须有不同的名字
    name = 'mySpider'
    allowed_domain = ['www.zust.edu.cn']    # www.sdibt.edu.cn>>>emmmm广告植入
    # 要爬取的起始页面，！！必须是列表！！，可以包含多个URL
    start_urls = ['http://www.zust.edu.cn/html/service/hy']
    # http://www.sdibt.edu.cn/info/1026/11238.html，原链接失效了,,,

    # 对于每个要爬取的网页，会自动调用下面这个方法(parse, 解析)
    def parse(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

        # 检查页面中的超链接，并继续爬取
        hxs = scrapy.Selector(response)   # 选择器
        sites = hxs.xpath('//u1/li')    # 看来得撸一下这个xpath,,,
        for site in sites:
            link = site.xpath('a/@href').extract()[0]    # 喵喵喵，这他喵都什么东西啊
            if link == '#':
                continue
            # 将相对地址转化为绝对地址
            elif link.startwith('..'):
                next_url = os.path.dirname(response.url)
                next_url += '/'+link
            else:
                next_url = link
            # 生成的Request对象，并指定回调函数
            yield scrapy.Request(url=next_url, callback=self.parse_item)   # 什么鬼，还有蜜汁parse_item

        # 回调函数，对起始页面中的每个超链接起作用
        def parse_item(self, response):
            self.downloadWebpage(response)
            self.downloadImages(response)

        # 下载当前页面中的图片
        def downloadImages(self, response):
            hxs = scrapy.Selector(response)
            images = hxs.xpath('//img/@src').extract()
            for image_url in images:
                imageFilename = image_url.split('/')[-1]
                if os.path.exists(imageFilename):
                    continue
                # 把相对地址转化成绝对地址
                if image_url.startswith('..'):
                    image_url = os.path.dirname(response.url) + '/'+image_url
                # 打开网页图片
                fp = urllib.request.urlopen(image_url)
                # 创建本地图片文件
                with open(imageFilename, 'wb') as f:
                    f.write(fp.read())
                fp.close()

        # 把网页内容保存为本地文件
        def downloadWebpage(self, response):
            filename = response.url.split('/')[-1]   # 取了最后一部分做名字
            with open(filename, 'wb') as f:
                f.write(response.body)

# 命令提示符输入
# scrapy crawl mySpider
