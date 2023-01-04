# Ex1 Tạo một movies list chứa tên các bộ phim đã xem
movie_list = ["Doremon", "gió", "OnePiece", "Dragonball", "Pokemon"]
print(f"danh sách phim {movie_list}")
# Ex2 Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
insert_movie_list = movie_list.append(input("nhập thêm Phim :"))
# Ex3 Thêm bộ phim vừa nhập vào cuối của danh sách movies
print(f"nhập thêm phim : ", movie_list)
# Ex5 Tính tổng bộ phim có trong movies
Count_movie = len(movie_list)
# Ex4 In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
print("In phim đầu , giữa , cuối \n",
      movie_list[0], movie_list[Count_movie//2], movie_list[-1], sep="||")
# Ex6 Xóa bộ phim đầu và cuối trong movies
movie_list.remove(movie_list[0])
movie_list.remove(movie_list[-1])
print("Xoá Phim đầu và phim cuối của list ", movie_list)
# Ex7 Lấy ra và xóa bộ phim cuối cùng trong movies
print("Xoá bộ phim cuối cùng trong danh sách : ",
      movie_list.pop(), "\n Danh sách còn lại : ", movie_list)
# Ex8 Chèn một bộ phim bất kỳ vào đầu danh sách movies
print(movie_list.insert((0), input("Tên Phim mới : ")),
      "\n danh sách phim mới : ", movie_list)
# Ex9 Đếm số bộ phim có tiêu đề là "One Piece"
print("Đếm phim One Piece : ", movie_list.count("OnePiece"))
# Ex10 Tìm vị trí của bộ phim có tên là "gió"
print("Tìm vị trí của bộ phim có tên là 'gió' :", movie_list.index("gió"))
# Ex11 Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
movie_extend = movie_list.extend(["conan", "Batman", "Inuyasha"])
print("danh sách phim mới :", movie_list)
# Ex12 Xóa tất cả các bộ phim có trong danh sách
movie_list.clear()
