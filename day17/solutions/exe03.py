# Buttons and Grid
import tkinter as tk

# Define window
root = tk.Tk()
root.title("Button Basics!")
root.iconbitmap("thinking.ico")
root.geometry("500x500")
root.resizable(0, 0)

# Define layout
name_button = tk.Button(root, text="Name")
name_button.grid(row=0, column=0)

time_button = tk.Button(root, text="Time", bg="#0ff")
time_button.grid(row=0, column=1)

place_button = tk.Button(root, text="Place", bg="#0ff", activebackground="#f00")
place_button.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

day_button = tk.Button(root, text="Day", bg="black", fg="white", borderwidth=5)
day_button.grid(row=1, column=0, columnspan=3, sticky="WE")

test1 = tk.Button(root, text="Test 1")
test2 = tk.Button(root, text="Test 2")
test3 = tk.Button(root, text="Test 3")
test4 = tk.Button(root, text="Test 4")
test5 = tk.Button(root, text="Test 5")
test6 = tk.Button(root, text="Test 6")

test1.grid(row=2, column=0, padx=5, pady=5)
test2.grid(row=2, column=1, padx=5, pady=5)
test3.grid(row=2, column=2, padx=5, pady=5, sticky="W")
test4.grid(row=3, column=0, padx=5, pady=5)
test5.grid(row=3, column=1, padx=5, pady=5)
test6.grid(row=3, column=2, padx=5, pady=5, sticky="W")

# Call the root window's main loop
root.mainloop()
