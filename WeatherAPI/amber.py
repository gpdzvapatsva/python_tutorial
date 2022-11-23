from tkinter import *
import tkinter as tk
import requests

window = tk.Tk()
window.title('Weather App')
window.geometry("500x500")
window.configure(background="blue")
heading=Label(text="Weather", bg="light grey", fg="black")
heading.pack()

def weather():
    try:
        city=entry.get()
        api_address='https://api.openweather.org/data/2.5/weather'
        url=api_address+city
        weatherkey='b53a991aa35c7fab55d88abd0fcceaaa'
        params1={'appid':weatherkey,'q':city,'units':'Metric'}
        response=requests.get(url,params=params1)
        weather=response.json()
        mylabel.config(text=str(weather['main']['temp']))
        print(weather)
    except:
        print("error")


def clear():
    entry.delete('1.0',END)

open_buttonclear = Button(window,text="Clear", command=clear)
open_buttonclear.place(x=320,y=230)

open_button_exit = Button(window,text="Exit",command=exit)
open_button_exit.place(x=420,y=230)



frame=tk.Frame(window,bg="light blue",bd='25')
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.15,anchor='n')
frame.pack()

entry=tk.Entry(frame,font=30)
entry.place(relwidth=0.5,relheight=1)
entry.pack()

wbutton=tk.Button(window,text="Check Temperature",command=weather)
wbutton.pack()
mylabel = tk.Label(window, font=40, bd=10, text="", anchor='nw', justify='left')
mylabel.pack()
window.mainloop()