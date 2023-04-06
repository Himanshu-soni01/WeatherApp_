from tkinter import *
from tkinter import ttk
import requests

def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=410356dc26dd34f02ad954f4762df595").json()
    w.config(text=data["weather"][0]['main'])
    wd.config(text=data["weather"][0]['description'])
    temp.config(text=str(int(data["main"]["temp"]-273)))
    pr.config(text=data["main"]["pressure"])

win = Tk()

win.title("Weather app")
win.config(bg = "light blue")
win.geometry("500x400")


name_label = Label(win,text = "Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=10,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

combo = ttk.Combobox(win,text = "Weather App",values=list_name,font=("Times New Roman",10,"bold"),textvariable=city_name)
combo.place(x=50,y=70,height=40,width=400)

w_label = Label(win,text = "Weather climate : ",font=("Times New Roman",10,"bold"),bg="light blue")
w_label.place(x=50,y=170,height=30,width=150)

w = Label(win,text = "",font=("Times New Roman",10,"bold"),bg="light blue")
w.place(x=200,y=170,height=30,width=150)


wd_label = Label(win,text = "Weather Description : ",font=("Times New Roman",10,"bold"),bg="light blue")
wd_label.place(x=50,y=220,height=30,width=150)

wd = Label(win,text = "",font=("Times New Roman",10,"bold"),bg="light blue")
wd.place(x=200,y=220,height=30,width=150)


temp_label = Label(win,text = "Temperature : ",font=("Times New Roman",10,"bold"),bg="light blue")
temp_label.place(x=50,y=270,height=30,width=150)

temp= Label(win,text = "",font=("Times New Roman",10,"bold"),bg="light blue")
temp.place(x=200,y=270,height=30,width=150)


pr_label = Label(win,text = "Pressure : ",font=("Times New Roman",10,"bold"),bg="light blue")
pr_label.place(x=50,y=320,height=30,width=150)

pr = Label(win,text = "",font=("Times New Roman",10,"bold"),bg="light blue")
pr.place(x=200,y=320,height=30,width=150)

done_btn  = Button(win,text = "Done",font=("Times New Roman",10,"bold"),command=get_data)
done_btn.place(x=200,y=120,height=30,width=80)

win.mainloop()