from pathlib import Path
import scrapy
from scrapy import Selector
from ..items import GraphicsCardResearchItem

class QuotesSpider(scrapy.Spider):
    name = "main"
    start_urls = [
        "https://technical.city/zh/video/best-price-to-performance",
    ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)

        # 表格
        res = response.css("tbody#rating_table_data")
        if res.get() is None:
            raise ValueError("解析结果为空")
        
        # 排除广告 并 筛选 桌面显卡
        rows=res.xpath("tr[not(contains(@class, 'banner')) and td[3]/i/span[text()='桌面']]")
        if rows.get() is None:
            raise ValueError("解析结果为空")
        
        # 遍历
        for row in rows:
            item = GraphicsCardResearchItem()
            item["name"] = row.xpath("td[2]").css("a::text").get().strip()
            item["rating"] = row.xpath("td[4]").css("td::text").get().strip()
            item["performance"] = row.xpath("td[6]").css("td::text").get().strip()
            item["year"] = row.xpath("td[7]").css("td::text").get().strip()
            
            yield item
            # 京东华硕价格
            # 京东微星价格
            # 京东技嘉价格
            