import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image

# Define window
root = tk.Tk()
root.title("Notepad")
root.iconbitmap("pad.ico")
root.geometry("600x600")
root.resizable(False, False)

# Define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"

root.config(bg=root_color)


# Define functions
def change_font(event=None):
    ''' Change the given font base off dropbox options. '''
    my_font = (font_family.get(), font_size.get())

    if font_option.get() != "none":
        my_font += (font_option.get(),)

    # Change the font style
    input_text.config(font=my_font)


def new_note():
    ''' Create a new note which essentially clears the screen. '''
    # Use a messagebox to ask for a new note
    question = messagebox.askyesno("New Note", "Are you sure you want to start a new note?")

    if question == 1:
        # ScrolledText widgets starting index is 1.0 not 0.
        input_text.delete("1.0", tk.END)


def close_note():
    ''' Closes the note which essentially quits the program. '''
    # Use a messagebox to ask to close
    question = messagebox.askyesno("Close Note", "Are you sure you want to close your note?")

    if question == 1:
        root.destroy()


def save_note():
    ''' Save the given note. First three lines are saved as font family, font size, and font option '''
    # Use filedialog to get location and name of where/what to save the file as
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note", filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))

    with open(save_name, 'w') as f:
        # First three lines of save file are font_family, font_size, and font_options. Font size must be a string not int
        f.write(font_family.get() + '\n')
        f.write(str(font_size.get()) + '\n')
        f.write(font_option.get() + '\n')

        # Write remaining text in field to the file
        f.write(input_text.get("1.0", tk.END))


def open_note():
    ''' Open a previously saved note. First three lines of note are font-family, font-size, and font-option. First set the font, then load the text. '''
    # Use filedialog to get location and directory of note file
    open_name = filedialog.askopenfilename(initialdir="./", title="Open Note", filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))

    with open(open_name, 'r') as f:
        # Clear the current text
        input_text.delete("1.0", tk.END)

        # First three lines are font family, font size, and font option...You must strip the new line char at the end of each line!
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        # Call the change font for these .set() and pass an arbitary value
        change_font()

        # Read the rest of the file and insert it into the text field
        text = f.read()
        input_text.insert("1.0", text)



# Define layout
# Define frames
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)

menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Layout for menu frame
# Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open("new.png"))
new_button = tk.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
open_button = tk.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open("save.png"))
save_button = tk.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open("close.png"))
close_button = tk.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

# Create a list of fonts to use
families = ["Terminal", "Modern", "Script", "Courrier", "Arial", "Calibri", "Cambria",
            "Georgia", "MS Gothic", "SimSun", "Tahoma", "Times New Roman", "Verdana", "Wingdings"]

font_family = tk.StringVar()
font_family.set("Terminal")

font_family_drop = tk.OptionMenu(
    menu_frame, font_family, *families, command=change_font)

# Set the width so it will fit "Times New Roman" and remain constant
font_family_drop.grid(row=0, column=4, padx=5, pady=5)
font_family_drop.config(width=16)

sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = tk.IntVar()

font_size.set(12)
font_size_drop = tk.OptionMenu(
    menu_frame, font_size, *sizes, command=change_font)

# Set width to be constant even if its 8.
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ["none", "bold", "italic"]
font_option = tk.StringVar()
font_option.set("none")
font_option_drop = tk.OptionMenu(menu_frame, font_option, *options, command=change_font)

# Set the width to be constant
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

# Layout for the text frame
# Create input_text as a scrolltext so you can scroll through the text field
# Set default width and height to be more than the window size so that on the smallest text size,
# the text field size is constant
my_font = (font_family.get(), font_size.get())
input_text = scrolledtext.ScrolledText(
    text_frame, bg=text_color, font=my_font, width=1000, height=100)
input_text.pack()

# Run the root window's main loop
root.mainloop()
