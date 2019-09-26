import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk


root = tk.Tk()

HEIGHT = 500
WIDTH = 600 

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

# key : 0ea3e8895f43be1cc1506432f4bb380e

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		
		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name,desc.title(),temp)
	except:
		final_str = "There was a problem retrieving that information"

	return final_str

def get_weather(city):
	weather_key = '0ea3e8895f43be1cc1506432f4bb380e'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'} 
	response = requests.get(url, params = params)
	weather = response.json()

	label['text'] = format_response(weather)

	icon_name = weather['weather'][0]['icon']
	open_image(icon_name)


def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
background_image = tk.PhotoImage(file = "/Users/Mihir/Downloads/landscape.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

canvas.pack()

frame = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

entry = tk.Entry(frame, font = ('Helvetica Neue',20))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", font = ('Helvetica Neue',15), command=lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

bg_color = "white"
label = tk.Label(lower_frame, font = ('Helvetica Neue',20), anchor = 'nw', justify = 'left', bd = 4, bg = bg_color)
label.place(relwidth = 1, relheight = 1)

weather_icon = tk.Canvas(label, bg = bg_color, bd=0, highlightthickness = 0)
weather_icon.place(relx=.75, rely=0, relwidth=0.5, relheight=0.5)

root.mainloop()

