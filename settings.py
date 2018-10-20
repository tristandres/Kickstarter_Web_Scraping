
DOWNLOADER_MIDDLEWARES = {
	'scrapy_splash.SplashCookiesMiddleware': 723,
	'scrapy_splash.SplashMiddleware': 725,
	'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
BOT_NAME = 'Kickstarter'

SPIDER_MODULES = ['Kickstarter.spiders']
NEWSPIDER_MODULE = 'Kickstarter.spiders'
SPLASH_URL = 'http://192.168.99.100:8050'

ITEM_PIPELINES = { 'Kickstarter.pipelines.WriteItemPipeline': 200}

ROBOTSTXT_OBEY = False

AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 1

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
#}
SPIDER_MIDDLEWARES = {
	'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}