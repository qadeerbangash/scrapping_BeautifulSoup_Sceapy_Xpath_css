import scrapy
from scrapy.crawler import CrawlerProcess

class DC_Chapter_Spider(scrapy.Spider):
    name = "dc_chapter_spider"
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']
    
    def parse(self, response):
        # Parse the current page
        for book in response.css('article.product_pod'):
            book_name = book.css('h3 a::attr(title)').get().strip()
            book_price = book.css('p.price_color::text').get().strip().replace('\u00a3','')
            img_url = book.css('div.image_container a::attr(href)').get()
            # Yield the data as a dictionary
            yield {
                'book_name': book_name,
                'book_price': book_price,
                'image_url': img_url,
            }
        
        # Follow the next page link and continue scraping
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

# Start the scraping process
process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',  # Set the format to JSON
    'FEED_URI': 'scraped_data.json',  # Set the output file name
})

scraped_data = []
process.crawl(DC_Chapter_Spider)
process.start()






















# import scrapy
# import csv
# from scrapy.crawler import CrawlerProcess

# class DC_Chapter_Spider(scrapy.Spider):
#     name = "dc_chapter_spider"
#     start_urls = ['https://books.toscrape.com/catalogue/page-1.html']
    
#     def parse(self, response):
#         # Parse the current page
#         for book in response.css('article.product_pod'):
#             book_name = book.css('h3 a::attr(title)').get()
#             book_price = book.css('p.price_color::text').get()
            
#             # Yield the data as a dictionary
#             yield {
#                 'book_name': book_name,
#                 'book_price': book_price,
#             }
        
#         # Follow the next page link and continue scraping
#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page:
#             yield response.follow(next_page, self.parse)

# # Start the scraping process
# process = CrawlerProcess()
# process.crawl(DC_Chapter_Spider)
# process.start()






























# import scrapy
# from scrapy.crawler import CrawlerProcess

# class DC_Chapter_Spider(scrapy.Spider):
#     name = "dc_chapter_spider"
    
#     def start_requests(self):
#         url = 'https://books.toscrape.com/catalogue/page-1.html'
#         yield scrapy.Request(url=url, callback=self.parse_front)

#     def parse_front(self, response):
#         # Initialize an empty list to store the scraped items
#         scraped_items = []
        
#         # Parse the front courses page
#         for book in response.css('article.product_pod'):
#             book_name = book.css('h3 a::attr(title)').get()
#             book_price = book.css('p.price_color::text').get()
            
#             # Append the scraped data as a dictionary to the list
#             scraped_items.append({
#                 'book_name': book_name,
#                 'book_price': book_price,
#             })
        
#         # Return the list of scraped items
#         return scraped_items

# # Start the scraping process
# process = CrawlerProcess()
# scraped_data = process.crawl(DC_Chapter_Spider)
# process.start()

# # After the process has finished, print the scraped data
# print(scraped_data)





























# import scrapy
# from scrapy.crawler import CrawlerProcess

# class DC_Chapter_Spider(scrapy.Spider):
#     name = "dc_chapter_spider"
    
#     def start_requests(self):
#         url = 'https://books.toscrape.com/catalogue/page-1.html'
#         yield scrapy.Request(url=url, callback=self.parse_front)

#     def parse_front(self, response):
#         # Parse the front courses page
#         for book in response.css('article.product_pod'):
#             book_name = book.css('h3 a::attr(title)').get()
#             book_price = book.css('p.price_color::text').get()
            
#             # Yield the data as a dictionary
#             yield {
#                 'book_name': book_name,
#                 'book_price': book_price,
#             }

# # Start the scraping process
# process = CrawlerProcess()
# process.crawl(DC_Chapter_Spider)
# process.start()


