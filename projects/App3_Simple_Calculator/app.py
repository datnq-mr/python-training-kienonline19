# Simple Calculator
import tkinter as tk

# Define window
root = tk.Tk()
root.title("Simple Calculator")
root.iconbitmap("calc.ico")
root.geometry("300x400")
root.resizable(False, False)

# Define colors and fonts
dark_green = "#93af22"
light_green = "#acc253"
white_green = "#edefe0"
button_font = ("Arial", 18)
display_font = ("Arial", 30)

# Define functions


def submit_number(number):
    ''' Add a number or decimal to the display '''
    # Insert the number or decimal pressed to the end of the display
    display.insert(tk.END, number)

    # If decimal was pressed, disable button so it cannot be pressed twice
    if '.' in display.get():
        decimal_button.config(state=tk.DISABLED)


def operate(operator):
    ''' Store the first number of the expression and the operation to be used '''
    global first_number
    global operation

    # Get the operator pressed and the current value of the display. This is the first number in the calculation
    operation = operator
    first_number = display.get()

    # Delete the value (first number) from entry display
    display.delete(0, tk.END)

    # Disable all operator buttons until equal or clear is pressed
    add_button.config(state=tk.DISABLED)
    subtract_button.config(state=tk.DISABLED)
    multiply_button.config(state=tk.DISABLED)
    divide_button.config(state=tk.DISABLED)
    exponent_button.config(state=tk.DISABLED)
    inverse_button.config(state=tk.DISABLED)
    square_button.config(state=tk.DISABLED)

    # Return decimal button to normal state
    decimal_button.config(state=tk.NORMAL)


def equal():
    ''' Run the stored operation for two numbers. '''
    # Perform the desired mathematics
    if operation == "add":
        value = float(first_number) + float(display.get())
    elif operation == "subtract":
        value = float(first_number) - float(display.get())
    elif operation == "multiply":
        value = float(first_number) * float(display.get())
    elif operation == "divide":
        if display.get() == '0':
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == "exponent":
        value = float(first_number) ** float(display.get())

    # Remove the current value of the display and update it with the answer
    display.delete(0, tk.END)
    display.insert(0, value)

    # Return buttons to normal states
    enable_buttons()


def enable_buttons():
    ''' Enable all buttons on the calculator '''
    decimal_button.config(state=tk.NORMAL)
    add_button.config(state=tk.NORMAL)
    subtract_button.config(state=tk.NORMAL)
    multiply_button.config(state=tk.NORMAL)
    divide_button.config(state=tk.NORMAL)
    exponent_button.config(state=tk.NORMAL)
    inverse_button.config(state=tk.NORMAL)
    square_button.config(state=tk.NORMAL)


def clear():
    ''' Clear the display '''
    display.delete(0, tk.END)

    # Returns buttons to normal state
    enable_buttons()


def inverse():
    ''' Calculate the inverse of a given number. '''
    # Do not allow for 1/0
    value = display.get()

    if value == '0':
        result = "ERROR"
    else:
        result = 1 / float(value)

    # Remove the current value in the display and update it with the answer
    display.delete(0, tk.END)
    display.insert(0, result)


def square():
    ''' Calculate the square of a given number. '''
    value = float(display.get()) ** 2
    # Remove the current value in the display and update it with the answer
    display.delete(0, tk.END)
    display.insert(0, value)


def negate():
    ''' Negate a given number '''
    value = -float(display.get())
    display.delete(0, tk.END)
    display.insert(0, value)


# GUI Layout
# Define frames
display_frame = tk.Frame(root)
button_frame = tk.Frame(root)

display_frame.pack(padx=2, pady=(0, 20))
button_frame.pack(padx=2, pady=5)

# Layout for the display frame
display = tk.Entry(display_frame, width=50, font=display_font,
                   bg=white_green, borderwidth=5, justify=tk.RIGHT)
display.pack(padx=5, pady=5)

# Layout for the button frame
clear_button = tk.Button(button_frame, text="Clear",
                         bg=dark_green, font=button_font, command=clear)
quit_button = tk.Button(button_frame, text="Quit",
                        bg=dark_green, font=button_font, command=root.destroy)

inverse_button = tk.Button(button_frame, text="1/x",
                           font=button_font, bg=light_green, command=inverse)
square_button = tk.Button(button_frame, text="x^2",
                          font=button_font, bg=light_green, command=square)
exponent_button = tk.Button(button_frame, text="x^n", font=button_font,
                            bg=light_green, command=lambda: operate("exponent"))
divide_button = tk.Button(button_frame, text="/ ", font=button_font,
                          bg=light_green, command=lambda: operate("divide"))

multiply_button = tk.Button(button_frame, text="*", font=button_font,
                            bg=light_green, command=lambda: operate("multiply"))
subtract_button = tk.Button(button_frame, text="-", font=button_font,
                            bg=light_green, command=lambda: operate("subtract"))
add_button = tk.Button(button_frame, text="+", font=button_font,
                       bg=light_green, command=lambda: operate("add"))

equal_button = tk.Button(button_frame, text="=",
                         font=button_font, bg=dark_green, command=equal)
decimal_button = tk.Button(button_frame, text=".", font=button_font,
                           bg="black", fg="white", command=lambda: submit_number('.'))
negate_button = tk.Button(button_frame, text="+/-",
                          font=button_font, bg="black", fg="white", command=negate)

nine_button = tk.Button(button_frame, text="9", font=button_font,
                        bg="black", fg="white", command=lambda: submit_number(9))
eight_button = tk.Button(button_frame, text="8", font=button_font,
                         bg="black", fg="white", command=lambda: submit_number(8))
seven_button = tk.Button(button_frame, text="7", font=button_font,
                         bg="black", fg="white", command=lambda: submit_number(7))
six_button = tk.Button(button_frame, text="6", font=button_font,
                       bg="black", fg="white", command=lambda: submit_number(6))
five_button = tk.Button(button_frame, text="5", font=button_font,
                        bg="black", fg="white", command=lambda: submit_number(5))
four_button = tk.Button(button_frame, text="4", font=button_font,
                        bg="black", fg="white", command=lambda: submit_number(4))
three_button = tk.Button(button_frame, text="3", font=button_font,
                         bg="black", fg="white", command=lambda: submit_number(3))
two_button = tk.Button(button_frame, text="2", font=button_font,
                       bg="black", fg="white", command=lambda: submit_number(2))
one_button = tk.Button(button_frame, text="1", font=button_font,
                       bg="black", fg="white", command=lambda: submit_number(1))
zero_button = tk.Button(button_frame, text="0", font=button_font,
                        bg="black", fg="white", command=lambda: submit_number(0))

# First row
clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")

# Second row
inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")

# Third row (Add padding to create the size of the column)
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20)

# Fourth row
four_button.grid(row=3, column=0, sticky="WE", pady=1)
five_button.grid(row=3, column=1, sticky="WE", pady=1)
six_button.grid(row=3, column=2, sticky="WE", pady=1)
subtract_button.grid(row=3, column=3, sticky="WE", pady=1)

# Fifth row
one_button.grid(row=4, column=0, sticky="WE", pady=1)
two_button.grid(row=4, column=1, sticky="WE", pady=1)
three_button.grid(row=4, column=2, sticky="WE", pady=1)
add_button.grid(row=4, column=3, sticky="WE", pady=1)

# Sixth row
negate_button.grid(row=5, column=0, sticky="WE", pady=1)
zero_button.grid(row=5, column=1, sticky="WE", pady=1)
decimal_button.grid(row=5, column=2, sticky="WE", pady=1)
equal_button.grid(row=5, column=3, sticky="WE", pady=1)

# Run the root window's main loop
root.mainloop()
