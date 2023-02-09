# Morse Code Translator
import tkinter as tk
from playsound import playsound
from PIL import ImageTk, Image

# Define window
root = tk.Tk()
root.title("Morse Code Translator")
root.iconbitmap("morse.ico")
root.geometry("500x350")
root.resizable(False, False)

# Define fonts and colors
button_font = ("SimSun", 10)
root_color = "#778899"
frame_color = "#dcdcdc"
button_color = "#c0c0c0"
text_color = "#f8f8ff"

root.config(bg=root_color)


# Define functions
def show_guide():
    ''' Show a morse code guide in a second window '''
    # Image "morse" needs to be a global variable to put on our window
    # Window "guide" needs to be global to close in another function
    global morse
    global guide

    # Create second window relative to the root window
    guide = tk.Toplevel()
    guide.title("Morse Guide")
    guide.iconbitmap("morse.ico")
    guide.geometry(f"350x350+{root.winfo_x() + 500}+{root.winfo_y()}")
    guide.config(bg=root_color)

    # Create the image, label, and pack
    morse = ImageTk.PhotoImage(Image.open("morse_chart.JPG"))
    label = tk.Label(guide, image=morse, bg=frame_color)
    label.pack(padx=10, pady=10, ipadx=5, ipady=5)

    # Create a close button
    close_button = tk.Button(guide, text="Close", font=button_font, bg=button_color, command=hide_guide)
    close_button.pack(padx=10, ipadx=50)

    # Disable the guide window
    guide_button.config(state=tk.DISABLED)


def hide_guide():
    ''' Hide the guide '''
    guide_button.config(state=tk.NORMAL)
    guide.destroy()


def play():
    ''' Play tones for corresponding dots and dashs '''
    # Determine where the morse code is
    if language.get() == 1:
        text = output_text.get("1.0", tk.END)
    elif language.get() == 2:
        text = input_text.get("1.0", tk.END)

    # Play the tones (., -, " ", |)
    for value in text:
        if value == '.':
            playsound("dot.mp3")
            root.after(100)
        elif value == '-':
            playsound("dash.mp3")
            root.after(200)
        elif value == ' ':
            root.after(300)
        elif value == '|':
            root.after(700)


def convert():
    ''' Call the appropriate conversion function based off radio button values '''
    # English to morse code:
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()


def get_morse():
    ''' Convert english message to morse code '''
    # String to hold morse code message
    morse_code = ''

    # Get the input text and standardize it to lower case
    text = input_text.get("1.0", tk.END)
    text = text.lower()

    # Remove any letters of symbols not in our dict keys
    for letter in text:
        if letter not in english_to_morse:
            text = text.replace(letter, '')

    # Break up into individual words based on space " " and put into a list
    word_list = text.split(" ")

    # Turn each individual word in word_list into a list of letters
    for word in word_list:
        letters = list(word)
        # For each letter, get the morse code representation and append it to the string morse_code
        for letter in letters:
            morse_char = english_to_morse[letter]
            morse_code += morse_char
            # Seperate individual letters with a space
            morse_code += ' '
        # Separate individual words with a |
        morse_code += '|'
    output_text.insert("1.0", morse_code)


def get_english():
    ''' Convert a morse code message to english '''
    # String to hold english message
    english = ''

    # Get the input text
    text = input_text.get("1.0", tk.END)

    # Remove any letters or symbols not in our dict keys
    for letter in text:
        if letter not in morse_to_english:
            text = text.replace(letter, '')

    # Break up each word based on | and put into a list
    word_list = text.split('|')

    # Turn each word into a list of letters
    for word in word_list:
        letters = word.split(' ')
        # For each letter, get the english representation and add it to the string english
        for letter in letters:
            english_char = morse_to_english[letter]
            english += english_char
        # Seperate individual words with a space
        english += ' '
    output_text.insert("1.0", english)


def clear():
    ''' Clear both the TextFields '''
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


# Create our morse code dictionaries
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': ' ', '|': '|', "": ""}

morse_to_english = {
    value: key
    for key, value in english_to_morse.items()
}

# Define layout
# Create frames
input_frame = tk.LabelFrame(root, bg=frame_color)
output_frame = tk.LabelFrame(root, bg=frame_color)

input_frame.pack(padx=16, pady=(16, 8))
output_frame.pack(padx=16, pady=(8, 16))

# Layout for the input frame
input_text = tk.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

# Create the radio buttons
language = tk.IntVar()
language.set(1)

morse_button = tk.Radiobutton(input_frame, text="English --> Morse Code",
                              variable=language, value=1, font=button_font, bg=frame_color)
english_button = tk.Radiobutton(input_frame, text="Morse Code --> English",
                                variable=language, value=2, font=button_font, bg=frame_color)
guide_button = tk.Button(input_frame, text="Guide",
                         font=button_font, bg=button_color, command=show_guide)

morse_button.grid(row=0, column=0, pady=(15, 0))
english_button.grid(row=1, column=0)
guide_button.grid(row=2, column=0, sticky="WE", padx=10)

# Layout for the output frame
output_text = tk.Text(output_frame, width=30, height=8, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

convert_button = tk.Button(
    output_frame, text="Convert", bg=button_color, font=button_font, command=convert)
play_button = tk.Button(output_frame, text="Play Morse",
                        bg=button_color, font=button_font, command=play)
clear_button = tk.Button(output_frame, text="Clear",
                         bg=button_color, font=button_font, command=clear)
quit_button = tk.Button(output_frame, text="Quit",
                        bg=button_color, font=button_font, command=root.destroy)

# Convert ipadx defines column width
convert_button.grid(row=0, column=0, padx=10, ipadx=50)
play_button.grid(row=1, column=0, padx=10, sticky="WE")
clear_button.grid(row=2, column=0, padx=10, sticky="WE")
quit_button.grid(row=3, column=0, padx=10, sticky="WE")

# Run the root window's main loop
root.mainloop()
