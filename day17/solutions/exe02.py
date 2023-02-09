# Labels and pack
import tkinter as tk
from tkinter import BOTH

# Define window
root = tk.Tk()
root.title("Label Basics!")
root.iconbitmap("thinking.ico")
root.geometry("400x400")
root.resizable(0, 0)
root.config(bg="blue")

# Create widgets
name_label_one = tk.Label(root, text="Hello, my name is Mike.")
name_label_one.pack()

name_label_two = tk.Label(root, text="Hello, my name is John.", font=("Arial", 18, "bold"))
name_label_two.pack()

name_label_three = tk.Label(root)
name_label_three.config(text="Hello, my name is Paul")
name_label_three.config(font=("Segoe UI", 10))
name_label_three.config(bg="#f00")
name_label_three.pack(padx=10, pady=50)

name_label_four = tk.Label(root, text="Hello, my name is Sue", bg="#000", fg="green")
name_label_four.pack(pady=(0, 10), ipadx=50, ipady=10, anchor="w")

name_label_five = tk.Label(root, text="Hello, my name is Pat", bg="#fff", fg="#123456")

name_label_five.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Run the root window's main loop
root.mainloop()
