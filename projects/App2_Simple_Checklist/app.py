# Simple Checklist
import tkinter as tk

# Define window
root = tk.Tk()
root.title("Simple Checklist")
root.iconbitmap("check.ico")
root.geometry("400x400")
root.resizable(False, False)

# Define fonts and colors
my_font = ("Times New Roman", 12)
root_color = "#6c1cbc"
button_color = "#e2cff4"
root.config(bg=root_color)

# Define functions


def add_item():
    ''' Add an individual item to the listbox '''
    my_listbox.insert(tk.END, list_entry.get())
    list_entry.delete(0, tk.END)


def remove_item():
    ''' Remove selected (ANCHOR) item from the listbox '''
    my_listbox.delete(tk.ANCHOR)


def clear_list():
    ''' Delete all items from the listbox '''
    my_listbox.delete(0, tk.END)


def save_list():
    ''' Save the list to ma simple txt file '''
    with open("checklist.txt", 'w') as f:
        # Listbox.get() returns a tuple ...
        list_tuple = my_listbox.get(0, tk.END)

        for item in list_tuple:
            # Take proper precautions to include only one \n for formatting purposes
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + '\n')


def open_list():
    ''' Open the list upon starting the program if there is one '''
    try:
        with open("checklist.txt", 'r') as f:
            for line in f:
                my_listbox.insert(tk.END, line)
    except:
        return


# Define layout
# Create frames
input_frame = tk.Frame(root, bg=root_color)
output_frame = tk.Frame(root, bg=root_color)
button_frame = tk.Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

# Input frame layout
list_entry = tk.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tk.Button(input_frame, text="Add Item",
                            borderwidth=2, font=my_font, bg=button_color, command=add_item)

list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

# Output frame layout
my_scroll_bar = tk.Scrollbar(output_frame)
my_listbox = tk.Listbox(output_frame, width=45,
                        height=15, borderwidth=3, font=my_font, yscrollcommand=my_scroll_bar.set)

my_listbox.grid(row=0, column=0)
my_scroll_bar.grid(row=0, column=1, sticky="NS")

# Link Scrollbar to Listbox
my_scroll_bar.config(command=my_listbox.yview)

# Button frame layout
list_remove_button = tk.Button(
    button_frame, text="Remove Item", borderwidth=2, font=my_font, bg=button_color, command=remove_item)
list_clear_button = tk.Button(
    button_frame, text="Clear List", borderwidth=2, font=my_font, bg=button_color, command=clear_list)
save_button = tk.Button(button_frame, text="Save List",
                        borderwidth=2, font=my_font, bg=button_color, command=save_list)
quit_button = tk.Button(button_frame, text="Quit", borderwidth=2,
                        font=my_font, bg=button_color, command=root.destroy)

list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

# Open the previous list if available
open_list()

# Run the root window's main loop
root.mainloop()
