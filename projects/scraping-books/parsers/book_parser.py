import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger("scraping.book_parser")


class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f"New book parser created from `{parent}`.")
        self.parent = parent

    @property
    def name(self):
        logger.debug("Finding book name...")
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f"Found book name, `{item_name}`.")
        return item_name

    @property
    def link(self):
        logger.debug("Finding book link...")
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        logger.debug(f"Found book link, `{item_link}`.")
        return item_link.attrs['href']

    @property
    def price(self):
        logger.debug("Finding book price...")
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        # £19.678
        pattern = r'£(\d+\.\d+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f"Found book price, `{float_price}`.")
        return float_price

    @property
    def rating(self):
        logger.debug("Finding book rating...")
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs.get('class')
        rating_classes = list(filter(lambda x: x != 'star-rating', classes))
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f"Found book rating, `{rating_number}`.")
        return rating_number

    def __repr__(self):
        return f"<Book {self.name}, £{self.price} ({self.rating} star{'s' if self.rating > 1 else ''})>"
