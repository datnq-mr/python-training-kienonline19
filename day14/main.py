import json

USER_MENU = '''Nhap
a - them sach
l - hien thi sach
x - xoa sach
s - tim kiem
q - thoat
Nhap lua chon: '''

BOOK_FILE = "books.json"
prevs = set()


try:
    with open(BOOK_FILE, 'x') as book_file:
        json.dump([], book_file)
except FileExistsError:
    pass


def read_book_file():
    with open(BOOK_FILE) as f:
        return json.load(f)


def write_book_file(data):
    with open(BOOK_FILE, mode='w') as f:
        json.dump(data, f, indent=4)


def add_book():
    book_id = input("Nhap ma so cuon sach: ")

    while book_id in prevs:
        print("Ma so bi trung, hay nhap lai!")
        book_id = input("Nhap ma so cuon sach: ")

    book_name = input("Nhap ten cuon sach: ")
    book_author = input("Nhap ten tac gia: ")

    book_dict = {
        'book_id': book_id,
        'book_name': book_name,
        'book_author': book_author
    }

    books = read_book_file()
    books.append(book_dict)
    write_book_file(books)
    print("Them thanh cong")
    prevs.add(book_id)


def show_book(book):
    print(f"{book['book_name']} - {book['book_author']}")


def show_books(_books):
    if _books:
        for book in _books:
            show_book(book)
    else:
        print("Danh sach trong")


def delete_book():
    id = input("Nhap id cuon sach can xoa: ")

    books = read_book_file()
    new_books = [book for book in books if book['book_id'] != id]

    if new_books != books:
        write_book_file(new_books)
        print("Xoa thanh cong")
    else:
        print("Khong tim thay cuon sach voi id:", repr(id))


def search_book():
    id = input("Nhap id cuon sach can xoa: ")

    books = read_book_file()
    new_books = [book for book in books if book['book_id'] == id]
    if new_books:
        show_books(new_books)
    else:
        print("Khong tim thay cuon sach voi id:", repr(id))


while True:
    user_choice = input(USER_MENU)

    if user_choice == 'a':
        add_book()
    elif user_choice == 'l':
        books = read_book_file()
        show_books(books)
    elif user_choice == 'x':
        delete_book()
    elif user_choice == 's':
        search_book()
    elif user_choice == 'q':
        break
    else:
        print("Lua chon khong hop le, vui long thu lai!")
