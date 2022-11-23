from tkinter import *
from tkinter import messagebox
import requests

mywindow=Tk()
mywindow.title("Amber weather App")
mywindow.geometry("500x500")

def get_weather():
    mycity=city_entry.get()
    weatherkey = '7f65701f025236c354d7754c5a4e0b71'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params1 = {'appid': weatherkey, 'q': mycity, 'units': 'Metric'}
    response = requests.get(url, params=params1)
    weather = response.json()
    result = weather['main']['temp']
    mylabel.config(text=str(result))

    print(weather)
def clear():
    pass

city_label=Label(mywindow, text="Enter the name of the city")
city_label.place(x=5, y=10)
city_entry=Entry(mywindow)
city_entry.place(x=250, y=10)
label1=Label(mywindow, text="Temperature")
label1.place(x=5, y=50)
mylabel = Label(mywindow)
mylabel.place(x=250, y=50)
mybutton=Button(mywindow, text="Check weather", command=get_weather)
mybutton.place(x=10, y=100 )
mybutton=Button(mywindow, text="Clear", command=clear)
mybutton.place(x=180, y=100 )
mybutton=Button(mywindow, text="Exit", command=mywindow.destroy)
mybutton.place(x=280, y=100)
mywindow.mainloop()