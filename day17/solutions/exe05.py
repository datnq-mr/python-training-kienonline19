# Entries and Functions
import tkinter as tk
from tkinter import END

root = tk.Tk()
root.title("Entry Basics!")
root.geometry("500x500")
root.resizable(False, False)
root.iconbitmap("thinking.ico")

# Define functions
def make_label():
    ''' Print a label to the app '''
    text = tk.Label(output_frame, text=text_entry.get(), bg="#f00")
    text.pack()
    text_entry.delete(0, END)


def count_up(number):
    ''' Count up on the app '''
    # global value

    text = tk.Label(output_frame, text=number, bg="red")
    text.pack()

    value = number + 1


# Define Frames
input_frame = tk.Frame(root, bg="#00f", width=500, height=100)
input_frame.pack(padx=10, pady=10)

output_frame = tk.Frame(root, bg="#f00", width=500, height=400)
output_frame.pack(padx=10, pady=(0, 10))

# Add inputs
text_entry = tk.Entry(input_frame, width=40)
text_entry.grid(row=0, column=0, padx=5, pady=5)
input_frame.grid_propagate(False)

print_button = tk.Button(input_frame, text="Print", command=make_label)
print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

# Keep output frame size
output_frame.pack_propagate(False)

# Pass a parameter with lambda
value = True
count_button = tk.Button(input_frame, text="Count", command=lambda: count_up(value))
count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()
