# Kickstarter_Web_Scraping
My web-scraping project on Kickstarter explored the ideal characteristics a project needs to have the highest probability of being successful.
To do so, I utilized Scrapy in combination with Scrapy Splash as a large amount of Kickstarter.com is written in JavaScript.
After having cleaned and organized the data, I identified 3 main characteristics: campaign type, length of campaign and target funding for a successful campaign. 
Having decided upon the first 3 variables, I then identified the ideal and worst states to launch a campaign, the ideal amount of reward levels, how many updates you should give to your backers and the influence of comments on the success of a project.
The combiation of these characteristics obtained through web-scraping would allow a person to create a campaign with a clearly above average probability of successful funding.

Dict_for_categories.csv is used in the Project Kickstarter.IPYNB to be able to convert categories scrapped into a category and subcategory tuple.

Analysis.IPYNB is used for exploring the data scrapped and for data visualization.

Kickstarter3 is used as the data set for Analysis.IPYNB as my IP was banned after scrapping 20 rows of data.

The Kickstarter folder contains my python code for scraping Kickstarter's website.

Project Kickstarter.IPYNB is used to clean and organize the data pulled via the scrapy spider in the Kickstarter folder.
