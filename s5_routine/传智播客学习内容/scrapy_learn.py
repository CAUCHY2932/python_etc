#架构
scheduler
调度

spiders
爬虫内容

Item Pipeline
管道文件，数据处理

downloader
下载器
制作 Scrapy 爬虫 一共需要4步：

    新建项目  (scrapy startproject xxx)：新建一个新的爬虫项目
    明确目标 （编写items.py）：明确你想要抓取的目标
    制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
    存储内容 （pipelines.py）：设计管道存储爬取内容
