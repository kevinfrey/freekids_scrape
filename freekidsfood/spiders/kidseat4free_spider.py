from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from freekidsfood.items import FreekidsfoodItem

class Kidseat4freeSpider(CrawlSpider):
	name = "kidseat4free"
	allowed_domains = ["kidseat4free.com"]
	start_urls = [
		"http://kidseat4free.com/browse/"
	]

	rules = (
		
		Rule(SgmlLinkExtractor(deny=('item\.php', )), callback='parse_item', follow= True),
		
	)

	def parse_item(self, response):
		self.log('Hi, this is an item page! %s' % response.url)

		sel = Selector(response)
		tr_s = sel.xpath('//table[@id="list"]/tbody/tr')
		self.log('There are  %s on the page' % len(tr_s))
		items = []
		for tr in tr_s:
			item = FreekidsfoodItem()
			item['name'] = tr.xpath('td[1]/a/text()').extract()[0].strip()
			item['address'] = tr.xpath('td[2]/text()').extract()[0].strip()
			item['city'] = tr.xpath('td[3]/text()').extract()[0].strip()
			item['state'] = tr.xpath('td[4]/text()').extract()[0].strip()
			item['phone'] = tr.xpath('td[5]//a/text()').extract()[0].strip()
			item['days'] = tr.xpath('td[6]/text()').extract()[0].strip()
			item['rating'] = tr.xpath('td[7]/text()').extract()[0].strip()
			self.log('item is %s' % item)
			items.append(item)
		return items
		
