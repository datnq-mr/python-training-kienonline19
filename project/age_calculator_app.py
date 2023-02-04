from tkinter import *
from datetime import datetime # Lấy thời gian hiện tại



root = Tk() # Màn hình chính

root.title('Máy tính tuổi') # Đặt tiêu đề

def calc():
    year = year_entry.get() # Lấy năm sinh
    age = datetime.now().year - int(year)
    result_label['text'] = "Năm sinh của bạn là: " + str(age) # Ghi kết quả lên màn hình


info_label = Label(root, text='Mời bạn nhập vào năm sinh') # Dòng thông báo hiển thị cho người dùng
info_label.grid(row=0, column=0) # Hiện widget lên màn hình

year_label = Label(root, text="Năm sinh:"); year_label.grid(row=1, column=0) # Tạo một label cho dễ nhìn

year_entry = Entry(root); year_entry.grid(row=1, column=1) # Tạo một ô nhập

result_label = Label(root); result_label.grid(row=2, column=0) # Tạo một ô hiện kết quả

submit_button = Button(root, text="Tính tuổi", command=calc); submit_button.grid(row=3, column=0) # Tạo nút tính kết quả


root.mainloop()