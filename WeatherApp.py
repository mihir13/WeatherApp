import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk
import os


root = tk.Tk()

# Set the title of the window
root.title("Weather App")

HEIGHT = 500
WIDTH = 600 


# Load API key from environment variable
weather_key = os.getenv('WEATHER_API_KEY', 'ffa0bbcd4c1e7489c0c8d1a52c3ab6c0')


def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		
		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name,desc.title(),temp)
	except KeyError:
		final_str = "There was a problem retrieving that information"

	return final_str

def get_weather(city):
    # Geocoding API to get latitude and longitude
    geocode_url = 'http://api.openweathermap.org/geo/1.0/direct'
    geocode_params = {'q': city, 'limit': 1, 'appid': weather_key}
    geocode_response = requests.get(geocode_url, params=geocode_params)

    print(f"Fetching coordinates for city: {city}")
    print(f"Geocode response status: {geocode_response.status_code}")
    print(f"Geocode response data: {geocode_response.text}")

    if geocode_response.status_code == 200:
        try:
            location = geocode_response.json()[0]
            lat = location['lat']
            lon = location['lon']

            # One Call API to get weather data
            weather_url = 'https://api.openweathermap.org/data/3.0/onecall'
            weather_params = {'lat': lat, 'lon': lon, 'exclude': 'minutely,hourly', 'appid': weather_key, 'units': 'metric'}
            weather_response = requests.get(weather_url, params=weather_params)

            print(f"Fetching weather data for coordinates: lat={lat}, lon={lon}")
            print(f"Weather response status: {weather_response.status_code}")
            print(f"Weather response data: {weather_response.text}")

            if weather_response.status_code == 200:
                weather = weather_response.json()
                icon_name = weather['current']['weather'][0]['icon']
                open_image(icon_name)
                label['text'] = format_response(weather)
            else:
                label['text'] = "Error: Unable to fetch weather data"
        except (KeyError, IndexError, TypeError):
            label['text'] = "Error: Unexpected response format"
    else:
        label['text'] = "Error: Unable to fetch location data"


def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
background_image = Image.open("assets/landscape.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=('Helvetica Neue', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Helvetica Neue', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

bg_color = "white"
label = tk.Label(lower_frame, font=('Helvetica Neue', 20), anchor='nw', justify='left', bd=4, bg=bg_color)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=0.5, relheight=0.5)

root.mainloop()
