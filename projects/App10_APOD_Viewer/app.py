# APOD Viewer
import tkinter as tk
import requests
import webbrowser
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import filedialog

# Define window
root = tk.Tk()
root.title("APOD Photo Viewer")
root.iconbitmap("rocket.ico")

# Define fonts and colors
text_font = ("Times New Roman", 14)
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
nasa_red = "#ff1923"
nasa_white = "#fff"
root.config(bg=nasa_blue)


# Define functions
def get_request():
    output_frame.pack(padx=50, pady=(0, 25))

    """ Get request data from NASA APOD API """
    global response

    # Get the parameters for the request
    url = "https://api.nasa.gov/planetary/apod"
    api_key = "1Fpnm5KqwRx6pDqFGLiZzn8BnPbjygYry5ml6uTD"  # USE YOUR OWN API KEY!!!
    date = calendar.get_date()

    query_string = {"api_key": api_key, "date": date}

    # Call the request and turn it into a python usable format
    response = requests.request("GET", url, params=query_string).json()
    print(response)
    # Update output labels
    set_info()


def set_info():
    """ Update output labels based on API call """
    # Example response
    """
    {
        "copyright": "Daniel Stern",
        "date": "2023-02-02",
        "explanation": "The 1970s are are sometimes ignored by astronomers. For example, this beautiful grouping of reflection nebulae in Orion - NGC 1977, NGC 1975, and NGC 1973 - is usually overlooked in favor of the substantial glow from the nearby stellar nursery better known as the Orion Nebula. Found along Orion's sword just north of the bright Orion Nebula complex, these reflection nebulae are also associated with Orion's giant molecular cloud about 1,500 light-years away, but are dominated by the characteristic blue color of interstellar dust reflecting light from hot young stars. In this sharp color image a portion of the Orion Nebula appears along the bottom border with the cluster of reflection nebulae at picture center. NGC 1977 stretches across the field just below center, separated from NGC 1973 (above right) and NGC 1975 (above left) by dark regions laced with faint red emission from hydrogen atoms. Taken together, the dark regions suggest the popular moniker, the Running Man Nebula. At the estimated distance of Orion's dusty molecular cloud this running man would be about 15 light-years across.",
        "hdurl": "https://apod.nasa.gov/apod/image/2302/NGC1975RunningMan.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Reflections on the 1970s",
        "url": "https://apod.nasa.gov/apod/image/2302/NGC1975RunningMan_1024.jpg"
    }
    """
    # Update the picture date and explanation
    picture_date.config(text=response['date'])
    picture_explanation.config(text=response['explanation'])

    # We need to use 3 images in other functions; an img, a thumb, and a full image
    global img
    global thumb
    global full_image

    media_type = response['media_type']
    url = response['url']

    if media_type == "image":
        # Grab the photo that is stored in our response
        img_response = requests.get(url, stream=True)

        # Get the content of the response and use BytesIO to open it as an image.
        # Keep a reference to this img as this is what we can use to save the image (Image not PhotoImage)
        # Create the full screen image for a second window
        image_data = img_response.content
        img = Image.open(BytesIO(image_data))
        full_image = ImageTk.PhotoImage(img)

        # Create the thumbnail for the main screen
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200, 200))
        thumb = ImageTk.PhotoImage(thumb)

        # Set the thumbnail image
        picture_label.config(image=thumb)
    elif media_type == "video":
        picture_label.config(text=url, image='')
        webbrowser.open(url)


def full_photo():
    """ Open the full size photo in a new window """
    top = tk.Toplevel()
    top.title("Full APOD Photo")
    top.iconbitmap("rocket.ico")

    # Load the full image to the top window
    img_label = tk.Label(top, image=full_image)
    img_label.pack()


def save_photo():
    """ Save the desired photo """
    save_name = filedialog.asksaveasfilename(
        initialdir='./', title="Save Image", filetypes=(("JPEG", "*.jpg"), ("All Files", "*.*")))
    img.save(f"{save_name}.jpg")


def init_gui():
    output_frame.pack_forget()


# Define layout
# Create frames
input_frame = tk.Frame(root, bg=nasa_blue)
output_frame = tk.Frame(root, bg=nasa_white)

input_frame.pack()

# Layout for the input frame
calendar = DateEntry(input_frame, width=10, font=text_font,
                     background=nasa_blue, foreground=nasa_white)
submit_button = tk.Button(input_frame, text="Submit",
                          font=text_font, bg=nasa_light_blue, command=get_request)
full_photo = tk.Button(input_frame, text="Full Photo",
                       font=text_font, bg=nasa_light_blue, command=full_photo)
save_button = tk.Button(input_frame, text="Save Photo",
                        font=text_font, bg=nasa_light_blue, command=save_photo)
quit_button = tk.Button(input_frame, text="Exit",
                        font=text_font, bg=nasa_red, command=root.destroy)

calendar.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_photo.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

# Layout for the output frame
picture_date = tk.Label(output_frame, font=text_font, bg=nasa_white)
picture_explanation = tk.Label(output_frame, wraplength=600)
picture_label = tk.Label(output_frame)

picture_date.grid(row=1, column=1, padx=10)
picture_explanation.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
picture_label.grid(row=0, column=1, padx=10, pady=10)

# Get today's photo to start with
# get_request()
init_gui()

# Run the root window's main loop
root.mainloop()
