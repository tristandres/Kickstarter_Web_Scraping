import scrapy

class KickstarterItem(scrapy.Item):
	Location = scrapy.Field()
	Nb_Comments = scrapy.Field()
	Pledged_Dollars = scrapy.Field()
	Pledged_Goal = scrapy.Field()
	Nb_Backers = scrapy.Field()
	Title = scrapy.Field()
	Description = scrapy.Field()
	Type = scrapy.Field()
	We_Love_Tag = scrapy.Field()
	Nb_Created_Projects = scrapy.Field()
	Nb_Rewards = scrapy.Field()
	Rewards_Dollars = scrapy.Field()
	Nb_Updates = scrapy.Field()
	Launch_Date = scrapy.Field()
	End_Date =  scrapy.Field()
