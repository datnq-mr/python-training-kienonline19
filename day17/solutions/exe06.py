# Radio Buttons
import tkinter as tk

root = tk.Tk()
root.title("Radio Button Basics!")
root.iconbitmap("thinking.ico")
root.geometry("350x350")
root.resizable(False, False)


def make_label():
    ''' Print to the screen '''
    if number.get() == 1:
        num_label = tk.Label(output_frame, text="1 one 1")
    elif number.get() == 2:
        num_label = tk.Label(output_frame, text="2 two 2")

    num_label.pack()


input_frame = tk.LabelFrame(root, text="This is fun!", width=350, height=100)
output_frame = tk.Frame(root, width=350, height=250)

input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0, 10))

number = tk.IntVar()
number.set(2)
radio1 = tk.Radiobutton(input_frame, text="Print the number one!", variable=number, value=1)
radio2 = tk.Radiobutton(input_frame, text="Print the number two!", variable=number, value=2)
print_button = tk.Button(input_frame, text="Print the number!", command=make_label)

radio1.grid(row=0, column=0, padx=10, pady=10)
radio2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
