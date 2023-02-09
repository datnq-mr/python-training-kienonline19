# Weather Forecast
import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO

# Define window
root = tk.Tk()
root.title("Weather Forecast")
root.iconbitmap("weather.ico")
root.geometry("400x400")
root.resizable(False, False)

# Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ("SimSun", 14)
small_font = ("SimSun", 10)


# Define functions
def search():
    ''' Use open weather api to look up current weather conditions given a city/city, country '''
    global response

    # Get API response
    # URL and my api key....USE YOUR OWN API KEY!
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "30b927f5311527a76b8536d6cc06b1d2"

    # Search by the appropriate query, either city name or zip
    if search_method.get() == 1:
        query_string = {'q': city_entry.get(), 'appid': api_key, 'units': 'imperial'}
    elif search_method.get() == 2:
        query_string = {'zip': city_entry.get(), 'appid': api_key, 'units': 'imperial'}

    # Call API
    response = requests.request("GET", url, params=query_string).json()

    # Example response return
    '''
    {
        "coord": {
            "lon": -71.0598,
            "lat": 42.3584
        },
        "weather": [
            {
                "id": 801,
                "main": "Clouds",
                "description": "few clouds",
                "icon": "02d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 274.97,
            "feels_like": 271.03,
            "temp_min": 273.53,
            "temp_max": 276.57,
            "pressure": 1018,
            "humidity": 58
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.12,
            "deg": 290
        },
        "clouds": {
            "all": 20
        },
        "dt": 1674832667,
        "sys": {
            "type": 2,
            "id": 2013408,
            "country": "US",
            "sunrise": 1674820971,
            "sunset": 1674856248
        },
        "timezone": -18000,
        "id": 4930956,
        "name": "Boston",
        "cod": 200
    }
    '''
    get_weather()
    get_icon()


def get_icon():
    ''' Get the approprite weather icon from API response '''
    global img

    # Get the icon id from API response
    icon_id = response['weather'][0]['icon']

    # Get the icon from the correct website
    url = "https://openweathermap.org/img/wn/{icon}.png".format(icon=icon_id)

    # Make a request at the url to download the icon; stream=True automatically download
    icon_response = requests.get(url, stream=True)

    # Turn into a form tkinter/python can use
    img_data = icon_response.content

    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    photo_label.config(image=img)


def get_weather():
    """ Grab information from API response and update our weather labels. """
    # Gather the data to be used from the API response
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    # update output
    city_info_label.config(text="{}({}, {})".format(city_name, city_lat, city_lon), font=large_font, bg=output_color)

    weather_label.config(text="Weather: {}, {}".format(main_weather, description), font=small_font, bg=output_color)

    temp_label.config(text="Temperature: {}F".format(temp), font=small_font, bg=output_color)
    feels_label.config(text="Feels Like: {}F".format(feels_like), font=small_font, bg=output_color)
    temp_min_label.config(text="Min Temperature: {}F".format(temp_min), font=small_font, bg=output_color)
    temp_max_label.config(text="Max Temperature: {}F".format(temp_max), font=small_font, bg=output_color)
    humidity_label.config(text="Humidity: {}".format(humidity), font=small_font, bg=output_color)


# Define layout
sky_frame = tk.Frame(root, bg=sky_color, height=250)
grass_frame = tk.Frame(root, bg=grass_color)
sky_frame.pack(fill=tk.BOTH, expand=True)
grass_frame.pack(fill=tk.BOTH, expand=True)

output_frame = tk.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tk.LabelFrame(grass_frame, bg=input_color, width=325)

output_frame.pack(pady=30)
output_frame.pack_propagate(False)
input_frame.pack(pady=15)

# Output frame layout
city_info_label = tk.Label(output_frame, bg=output_color)
weather_label = tk.Label(output_frame, bg=output_color)
temp_label = tk.Label(output_frame, bg=output_color)
feels_label = tk.Label(output_frame, bg=output_color)
temp_min_label = tk.Label(output_frame, bg=output_color)
temp_max_label = tk.Label(output_frame, bg=output_color)
humidity_label = tk.Label(output_frame, bg=output_color)
photo_label = tk.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

# Input frame layout
# Create input frame button and entry
city_entry = tk.Entry(input_frame, width=20, font=large_font)
submit_button = tk.Button(input_frame, text="Submit",
                          font=large_font, bg=input_color, command=search)

search_method = tk.IntVar()
search_method.set(1)

search_city = tk.Radiobutton(input_frame, text="Search by city name",
                             variable=search_method, font=small_font, value=1, bg=input_color)
search_zip = tk.Radiobutton(input_frame, text="Search by zipcode",
                            variable=search_method, font=small_font, value=2, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10, pady=(10, 0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, pady=2, padx=5)

# Run the root window's main loop
root.mainloop()
