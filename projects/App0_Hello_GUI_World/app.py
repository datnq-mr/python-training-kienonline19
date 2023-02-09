import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Hello GUI World")
root.geometry("400x400")
root.iconbitmap("wave.ico")
root.config(bg="#264653")
root.resizable(False, False)


def print_message():
    template = "Hello, {}! Keep learning Tkinter!"
    text = msg.get()
    if number.get() == 1:
        output_label = tk.Label(output_frame, text=template.format(text), bg="#90e0ef")
    elif number.get() == 2:
        output_label = tk.Label(output_frame, text=template.format(text).upper(), bg="#90e0ef")

    output_label.pack(pady=5)
    txt_msg.delete(0, tk.END)


input_frame = tk.Frame(root, width=300, height=100, bg="#457b9d")
input_frame.pack(pady=10)

msg = tk.StringVar()
txt_msg = tk.Entry(input_frame, width=25, textvariable=msg)
txt_msg.grid(row=0, column=0, padx=10, pady=10)
input_frame.grid_propagate(False)

submit_button = tk.Button(input_frame, text="Submit", command=print_message)
submit_button.grid(row=0, column=1, ipadx=30, padx=10)

number = tk.IntVar()
number.set(1)

radio1 = tk.Radiobutton(input_frame, text="Normal Case", variable=number, value=1, bg="#457b9d")
radio1.grid(row=1, column=0, pady=10)

radio2 = tk.Radiobutton(input_frame, text="Upper Case", variable=number, value=2, bg="#457b9d")
radio2.grid(row=1, column=1)

output_frame = tk.Frame(root, width=400, height=300, bg="#90e0ef")
output_frame.pack(padx=10, pady=(0, 20))

img = ImageTk.PhotoImage(Image.open("smile.png"))
lbl_img = tk.Label(output_frame, image=img, bg="#90e0ef")
lbl_img.pack()
output_frame.pack_propagate(False)

root.mainloop()
