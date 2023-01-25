# Định nghĩa menu hiển thị gợi ý người dùng nhập tùy chọn (option)
USER_MENU = """Nhập
a - Thêm một bộ phim mới
l - Hiển thị danh sách phim
s - Tìm kiếm các bộ phim theo tên
x - Xóa phim theo tên
u - Cập nhật thông tin phim
q - Thoát
Lựa chọn của bạn: """

# Định nghĩa cấu trúc dữ liệu lưu trữ các bộ phim
# list[dict]: mỗi bộ phim là một dictionary nằm trong danh sách
movies  = []

# Kiểm tra các bộ phim duy nhất
prevs   = set()


# Định nghĩa các hàm xử lý
# Thêm một bộ phim mới
def add_movie():
    # Nhập thông tin bộ phim
    name         = input("Nhập vào tên bộ phim\t: ")
    
    while name in prevs:
        print("Tên phim bị trùng! yêu cầu nhập lại!")
        name     = input("Nhập vào tên bộ phim\t: ")

    director     = input("Nhập vào tên đạo diễn\t: ")
    release_year = input("Nhập vào năm phát hành\t: ")

    # Tạo bộ phim
    movie = {
        'name'        : name,
        'director'    : director,
        'release_year': release_year
    }

    # Thêm vào danh sách
    movies.append(movie)
    prevs.add(name)


# Hiển thị thông tin chi tiết
def show_movie(movie):
    movie_name          = movie['name']
    movie_director      = movie['director']
    movie_release_year  = movie['release_year']
    
    print(f"Tên\t\t: {movie_name}")
    print(f"Đạo diễn\t: {movie_director}")
    print(f"Năm phát hành\t: {movie_release_year}")
    

# Hiển thị các bộ phim
def show_movies():
    if movies:
        for idx, movie in enumerate(movies, start=1):
            print("THÔNG TIN BỘ PHIM", idx)
            show_movie(movie)
    else:
        print("Danh sách phim trống!")


# Tìm kiếm phim theo tên
def search_movie():
    if movies:
        movie_name = input("Nhập vào tên bộ phim: ")

        for idx, movie in enumerate(movies, start=1):
            if movie['name'] == movie_name:
                print("THÔNG TIN BỘ PHIM", idx)
                show_movie(movie)
                break
        else:
            print("Không tìm thấy bộ phim có tên là", movie_name)
    else:
        print("Danh sách phim trống!")


# Xóa phim theo tên
def remove_movie():
    if movies:
        movie_name = input("Nhập vào tên bộ phim: ")

        for idx, movie in enumerate(movies):
            if movie['name'] == movie_name:
                del movies[idx]
                print("Đã xóa bộ phim thành công!")
                break
        else:
            print("Không tìm thấy bộ phim có tên là", movie_name)
    else:
        print("Danh sách phim trống!")


# Cập nhật thông tin phim
def update_movie():
    if movies:
        movie_name = input("Nhập vào tên bộ phim: ")

        founds = [
            idx
            for idx, movie in enumerate(movies)
            if movie['name'] == movie_name
        ]

        if founds:
            position                            = founds[0]

            movies[position]['director']        = input("Nhập vào tên đạo diễn\t: ")
            movies[position]['release_year']    = input("Nhập vào năm phát hành\t: ")

            print("Cập nhật bộ phim thành công!")
        else:
            print("Không có bộ phim có tên là", movie_name)
    else:
        print("Danh sách phim trống!")


# Nhập sự chọn lựa của người dùng
user_choice = input(USER_MENU)

# Định nghĩa một dict dùng để lưu các option ứng với hành động
operations = {
    'a': add_movie,
    'l': show_movies,
    's': search_movie,
    'x': remove_movie,
    'u': update_movie
}

# Chọn nhiều option cho đến khi bấm thoát
while user_choice != 'q':
    # Kiểm tra tùy chọn có nằm trong operations dict hay không ?
    # Nếu có thì gọi hàm không thì in ra "Lựa chọn không hợp lệ, yêu cầu nhập lại!"
    if user_choice in operations:
        # Lấy ra giá trị của key: user_choice
        operation = operations[user_choice]
        operation()  # gọi hàm tương ứng với tùy chọn
    else:
        print("Lựa chọn không hợp lệ, yêu cầu nhập lại!")

    # Nhập sự chọn lựa của người dùng
    user_choice = input(USER_MENU)
