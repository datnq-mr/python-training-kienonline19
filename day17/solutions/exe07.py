# Images
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Image Basics!")
root.iconbitmap("thinking.ico")
root.geometry("700x700")


def make_image():
    ''' Print an image '''
    global cat_image

    cat_image = ImageTk.PhotoImage(Image.open("cat.jpg"))
    cat_label = tk.Label(root, image=cat_image)
    cat_label.pack()


my_img = tk.PhotoImage(file="shield.png")
lbl_image = tk.Label(root, image=my_img)
lbl_image.pack()

my_button = tk.Button(root, image=my_img)
my_button.pack()

# Not for JPEG files
# cat_image = tk.PhotoImage(file="cat.jpg")
# tk.Label(root, image=cat_image).pack()
make_image()

root.mainloop()
