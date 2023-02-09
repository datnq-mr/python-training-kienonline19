# Hello GUI World
import tkinter as tk
from PIL import ImageTk, Image

# Define window
root = tk.Tk()
root.title("Hello GUI World")
root.iconbitmap("wave.ico")
root.geometry("400x400")
root.resizable(False, False)

# Define fonts and colors
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
root.config(bg=root_color)


# Define functions
def submit_name():
    ''' Say hello to the user '''
    # Create a label for the user name based of radio button values
    if case_style.get() == "normal":
        name_label = tk.Label(output_frame, text='Hello ' +
                              name.get() + '! Keep learning Tkinter', bg=output_color)
    elif case_style.get() == "upper":
        name_label = tk.Label(output_frame, text=(
            'Hello ' + name.get() + '! Keep learning Tkinter').upper(), bg=output_color)

    name_label.pack()
    name.delete(0, tk.END)


# Define layout
# Define frames
input_frame = tk.LabelFrame(root, bg=input_color)
output_frame = tk.LabelFrame(root, bg=output_color)

input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

# Create widgets
name = tk.Entry(input_frame, width=20)
submit_button = tk.Button(input_frame, text="Submit", command=submit_name)

name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# Create radio buttons for text display
case_style = tk.StringVar()
case_style.set("normal")

normal_button = tk.Radiobutton(
    input_frame, text="Normal Case", variable=case_style, value="normal", bg=input_color)
upper_button = tk.Radiobutton(
    input_frame, text="Upper Case", variable=case_style, value="upper", bg=input_color)

normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# Add an image
smile_image = ImageTk.PhotoImage(Image.open("smile.png"))
smile_label = tk.Label(output_frame, image=smile_image, bg=output_color)
smile_label.pack()

# Run root window's main loop
root.mainloop()
