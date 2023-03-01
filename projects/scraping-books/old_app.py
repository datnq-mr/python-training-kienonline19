import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info("Loading books list...")

page_content = requests.get('https://books.toscrape.com/').content
page = AllBooksPage(page_content)
books = page.books

for page_num in range(1, page.page_count):
    url = f"https://books.toscrape.com/catalogue/page-{page_num + 1}.html"
    page_content = requests.get(url).content
    logger.debug("Creating AllBooksPage from page content.")
    page = AllBooksPage(page_content)
    books.extend(page.books)
