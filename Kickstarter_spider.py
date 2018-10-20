from scrapy import Spider, Request
import numpy as np
from scrapy.contrib.exporter import CsvItemExporter
from Kickstarter.items import KickstarterItem
from scrapy_splash import SplashRequest #for more information on scrapy splash: https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash
import re

class KickstarterSpider(Spider):
	name = 'Kickstarter_spider'
	allowed_urls = ['https://www.kickstarter.com'] 
	start_urls = ['https://www.kickstarter.com/discover/advanced?sort=end_date&seed=2565797&page=1']
	all_ids = list([287,20,21,22,288,54,23,24,53,25,289,290,249,250,251,252,253,343,344,345,346,347,348,350,351,352,353,354,355,356,254,255,256,257,258,259,27,260,28,261,262,263,264,265,266,267,268,269,291,29,292,30,293,294,330,296,295,297,298,299,31,300,301,32,303,302,33,304,305,306,307,308,310,309,311,312,313,314,315,270,271,272,273,274,34,35,357,358,359,360,361,316,317,36,386,37,38,318,38,40,41,319,320,241,42,321,322,43,44,275,276,277,278,280,279,323,324,45,325,46,387,47,349,326,48,49,50,239,327,328,329,389,331,332,333,334,335,336,337,52,362,338,51,339,340,341,342,388,281,282,283,284,285,286])
	all_urls = ['https://www.kickstarter.com/discover/advanced?category_id={}&sort=end_date&seed=2565588&page=1'.format(x) for x in all_ids]
	all_pages = list(range(1,101))
	all_pages = all_pages[0:3]
	all_urls = all_urls[0:3]
	total_urls = []
	for a in all_urls:
		for b in all_pages:
			total_urls += list([a[:-1] + str(b)])
	
	def start_requests(self):
		for url in self.total_urls:
			yield SplashRequest(url, self.parse, args = {'wait':0.5},)

	def parse(self, response):
		project_url = response.xpath('//a[@class="soft-black mb3"]/@href').extract()

		for url in project_url[:2]:
			yield SplashRequest(url, self.parse_projects, args = {'wait':0.5},)

	def parse_projects(self,response):
		Location = response.xpath('//span[@class="ml1"]/text()').extract_first()
		Nb_Comments = int(response.xpath('//*[@itemprop="Project[comments_count]"]/text()').extract_first())
		Pledged_Dollars = response.xpath('//div[@class="flex items-center"]/span/span/text()').extract_first()
		Pledged_Dollars = re.sub("[^0-9]", "",Pledged_Dollars)
		Pledged_Goal = response.xpath('//div[@class="mb2-lg"]/span/span/span/text()').extract_first()
		Pledged_Goal = re.sub("[^0-9]", "",Pledged_Goal)
		Nb_Backers = int(response.xpath('//div[@class="ml5 ml0-lg mb2-lg"]/div/span/text()').extract_first())
		Title = response.xpath('//div[@class="col-full"]/h2/text()').extract_first()
		Description = response.xpath('//div[@class="col-full"]/p/text()').extract_first()
		Type = response.xpath('//span[@class="ml1"]/span/text()').extract()[1]
		We_Love_Tag = response.xpath('//span[@class="ml1"]/span/text()').extract_first() 
		Nb_Created_Projects = response.xpath('//div[@class="hide block-md mb2-md"]/a/text()').extract_first()
		Nb_Rewards = len(response.xpath('//div[@class="NS_projects__rewards_list js-project-rewards"]/ol/li').extract())
		Rewards_Dollars_modify = response.xpath('//*[@class="pledge__amount"]/span/text()').extract()
		Rewards_Dollars = [x for x in Rewards_Dollars_modify if x != '\nAbout ' if x != '\n' ]
		Rewards_Dollars = [int(re.sub("[^0-9]", "",x)) for x in Rewards_Dollars]

		Nb_Updates = int(response.xpath('//span[@class="count"]/text()').extract()[0])
		End_Date = response.xpath('//div[@class="grid-row order-2-md hide-lg mb3-md"]/div/div/p/text()').extract_first()

		update = list(["https://www.kickstarter.com" + response.xpath('//a[@data-content="updates"]/@href').extract_first()])

		item = KickstarterItem()

		item['Location'] = Location
		item['Nb_Comments'] = Nb_Comments
		item['Pledged_Dollars'] = Pledged_Dollars
		item['Pledged_Goal'] = Pledged_Goal
		item['Nb_Backers'] = Nb_Backers
		item['Title'] = Title
		item['Description'] = Description
		item['Type'] = Type
		item['We_Love_Tag'] = We_Love_Tag
		item['Nb_Created_Projects'] = Nb_Created_Projects
		item['Nb_Rewards'] = Nb_Rewards
		item['Rewards_Dollars'] = Rewards_Dollars
		item['Nb_Updates'] = Nb_Updates
		item['End_Date'] = End_Date

		for url in update:
			yield SplashRequest(url, self.update_date, args = {'wait':0.5},)

		yield item

	def update_date(self,response):
		Launch_Date = response.xpath('//div[@class="f5 bold mb2"]/time/text()').extract_first()
		
		item = KickstarterItem()
		item['Launch_Date'] = Launch_Date

		yield item
