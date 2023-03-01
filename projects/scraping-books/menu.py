import logging

from app import books

logger = logging.getLogger("scraping.menu")

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''


def print_best_books():
    logger.info("Finding best books by rating...")
    best_books = sorted(books, key=lambda x: (-x.rating, x.price))[:10]

    print('---- BEST ----')
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info("Finding best books by price...")
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]

    print('---- CHEAPEST ----')
    for book in cheapest_books:
        print(book)


books_generator = (book for book in books)


def get_next_book():
    logger.info("Getting next books from generator of all books...")
    print(next(books_generator))


def menu():

    user_choices = {
        'b': print_best_books,
        'c': print_cheapest_books,
        'n': get_next_book
    }

    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in user_choices:
            user_choices[user_input]()
        else:
            print("Please choose a valid command!")

        user_input = input(USER_CHOICE)
    logger.debug("Terminating program...")


if __name__ == "__main__":
    menu()
