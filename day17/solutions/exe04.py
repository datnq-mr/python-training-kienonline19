# Frames
import tkinter as tk
from tkinter import BOTH

# Define window
root = tk.Tk()
root.title("Frame Basics")
root.iconbitmap("thinking.ico")
root.geometry("500x500")

# Example of why to use frames?
""" name_label = tk.Label(root, text="Enter your name")
name_label.pack()

name_button = tk.Button(root, text="Submit your name")
name_button.grid(row=0, column=1)
 """

# Define frames
pack_frame = tk.Frame(root, bg="red")
grid_frame1 = tk.Frame(root, bg="blue")
grid_frame2 = tk.LabelFrame(root, text="Grid System Rules!", borderwidth=5)

# Pack frames onto root
pack_frame.pack(fill=BOTH, expand=True)
grid_frame1.pack(fill="x", expand=True)
grid_frame2.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Pack frame
tk.Label(pack_frame, text="text").pack()
tk.Label(pack_frame, text="text").pack()
tk.Label(pack_frame, text="text").pack()

# Grid one layout
tk.Label(grid_frame1, text="text").grid(row=0, column=0)
tk.Label(grid_frame1, text="text").grid(row=1, column=1)
tk.Label(grid_frame1, text="text").grid(row=2, column=2)
# tk.Label(grid_frame1, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row=3, column=0)

# Grid 2 layout
tk.Label(grid_frame2, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(
    row=0, column=0)

root.mainloop()
