# ***********************   USING Xpath   ********************
import scrapy
from scrapy.crawler import CrawlerProcess

class Awesom_books(scrapy.Spider):
    name = "AwesomeBooks"

    def start_requests(self):
        base_url = 'https://www.awesomebooks.com/books/category/303/fiction?page={}'
        for page_number in range(1, 501):  # Change range as needed for 500 pages
            url = base_url.format(page_number)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Parse the current page
        for book in response.xpath('//div[contains(@class, "product-item__body") and contains(@class, "pb-xl-2") and contains(@class, "text-center")]'):
            book_name = book.xpath('.//h5[contains(@class, "product-item__title") and contains(@class, "book_title")]/a/text()').get().strip()
            author_name = book.xpath('.//h5[contains(@class, "product-item__title") and contains(@class, "book_author")]/a/text()').get(default='').strip()
            price = book.xpath('.//div[contains(@class, "product-price")]/span[not(contains(@class, "rrp"))]/text()').get().strip().replace('\u00a3','')

            yield {
                'book_name': book_name,
                'author_name': author_name,
                'price': price,
            }

# Start the scraping process
process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',  # Set the format to JSON
    'FEED_URI': 'scraped_data_xpath.json',  # Set the output file name
})
process.crawl(Awesom_books)
process.start()
























# ***************************      USING css      ************************
# import scrapy
# from scrapy.crawler import CrawlerProcess

# class Awesom_books(scrapy.Spider):
#     name = "AwesomeBooks"

#     def start_requests(self):
#         base_url = 'https://www.awesomebooks.com/books/category/303/fiction?page={}'
#         for page_number in range(1, 501):  # Change range as needed for 500 pages
#             url = base_url.format(page_number)
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # Parse the current page
#         for book in response.css('div.product-item__body.pb-xl-2.text-center'):
#             book_name = book.css('h5.mb-1.product-item__title.book_title a::text').get().strip()
#             author_name = book.css('h5.mb-1.product-item__title.book_author a::text').get(default='').strip()
#             price = book.css('div.product-price span:not(.rrp)::text').get().strip().replace('\u00a3','')

#             yield {
#                 'book_name': book_name,
#                 'author_name': author_name,
#                 'price': price,
#             }

# # Start the scraping process
# process = CrawlerProcess(settings={
#     'FEED_FORMAT': 'json',  # Set the format to JSON
#     'FEED_URI': 'scraped_data_css.json',  # Set the output file name
# })
# process.crawl(Awesom_books)
# process.start()




