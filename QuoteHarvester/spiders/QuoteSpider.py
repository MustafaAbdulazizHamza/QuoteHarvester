import scrapy
from QuoteHarvester.items import QuoteItem
class QuotespiderSpider(scrapy.Spider):
    name = "QuoteSpider"
    allowed_domains = ["www.goodreads.com"]
    start_urls = ["https://www.goodreads.com/quotes"]

    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            Quote_Item = QuoteItem()
            Quote_Item['quote'] = quote.css('.quoteText::text').get()
            Quote_Item['author'] = quote.css("span.authorOrTitle::text").get()
            if not quote.css("#quote_book_link_6 a.authorOrTitle::text").get():
                Quote_Item['book_title'] = quote.css("#quote_book_link_6 a.authorOrTitle::text").get()
            Quote_Item['likes'] = quote.css("div.quoteFooter div.right a.smallText::text").get()
            yield Quote_Item
        next_page = response.css(".next_page::attr(href)").get()
        if next_page is not None:
            next_page = next_page.replace("quotes", '')
            next_page = "https://www.goodreads.com/quotes" + next_page
            yield response.follow(next_page, callback=self.parse)
        
    # CSS Selectors comments:

    # Quote = q.css('.quoteText::text').get()
    # author = q.css("span.authorOrTitle::text").get()
    # book_title = quote.css("#quote_book_link_6 a.authorOrTitle::text").get() # Some quotes are not from books.
    # likes = quote.css("div.quoteFooter div.right a.smallText::text").get()
    # The next page URL = response.css(".next_page::attr(href)").get()
