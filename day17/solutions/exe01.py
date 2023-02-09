# Window Basics
import tkinter as tk

# Define window
root = tk.Tk()
root.title("Window Basics!")
root.iconbitmap("thinking.ico")
root.geometry("250x700")
root.resizable(0, 0)
root.config(bg="blue")

# Second Window
top = tk.Toplevel()
top.title("Second Window")
top.config(bg='#123456')
top.geometry("200x200+500+50")

# Run root window's main loop
root.mainloop()
