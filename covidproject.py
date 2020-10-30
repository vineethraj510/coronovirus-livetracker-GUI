import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import pandas as pd
from PIL.ImageTk import PhotoImage
from PIL import Image


screen = tkinter.Tk()
#screen.configure(bg = 'black')
screen.title('Coronavirus Tracker')
screen.geometry('600x600')
country="india"


# here i uploaded a image

photo = PhotoImage(Image.open("IMAGE.jpg"))
lab = Label(screen, image = photo)
lab.grid(row=0, column=0)


def indiv_country():
    country=c.get()
    page=requests.get('https://www.worldometers.info/coronavirus/country/' + country)
    Soup = BeautifulSoup(page.content, 'html.parser')
    info = Soup.find_all(class_='maincounter-number')

    
    a = [items.get_text() for items in info]
    ccd = Label(lab,foreground = 'white', background = 'black', font = ('Times new Roman', 12),text=country + " Total Cases ")
    ccd.grid(column=100, row=10)

    cc = Label(lab, text = a[0],foreground = 'white', background = 'black', font = ('Times new Roman', 12))
    cc.grid(column=100, row=11)
    

    cd1 = Label(lab,foreground = 'white', background = 'black', font = ('Times new Roman', 12),text=country + " Total Deaths")
    cd1.grid(column=100, row=12)
    

    cd = Label(lab, text = a[1],foreground = 'white', background = 'black', font = ('Times new Roman', 12))

    cd.grid(column=100, row=13)
    
    cr1 = Label(lab,foreground = 'white', background = 'black', font = ('Times new Roman', 12),text=country + " Total Recovered")
    cr1.grid(column=100, row=14)
    
    cr= Label(lab, text = a[2],foreground = 'white', background = 'black', font = ('Times new Roman', 12))
    cr.grid(column=100, row=15)
    
    

#This is for getting individually country data

lbl = Label(lab, text = 'Please enter the country you want to check',
                       foreground = 'white', background = 'black', font = ('Times new Roman', 14))
lbl.grid(column=100, row=1)
c = Entry(lab,  foreground = 'black', font = ('Times new Roman', 12) )
c.grid(column = 100, row = 2)


sendBtn = tkinter.Button(lab, text="search", command=indiv_country,bg="white")  # Here i created a search button
sendBtn.grid(column = 100, row = 3)

#...........






#web scraping


link = 'https://www.worldometers.info/coronavirus/'

request = requests.get(link).content

soup= BeautifulSoup(request, 'html.parser')


cases = soup.find_all('div', class_ = 'maincounter-number')



total_cases = cases[0].text

total_deaths = cases[1].text

total_recovered = cases[2].text

# print(total_cases)
# print(total_recovered)
# print(total_deaths)





#creating label
label = tkinter.Label(lab, text = 'WorldWide Coronavirus Tracker',
                       foreground = 'white', background = 'black', font = ('Times new Roman', 14))
label.grid(row = 1, column = 1, padx = 5)

label1 = tkinter.Label(lab, text = 'Total Cases',
             foreground = 'white', background = 'black', font = ('Times new Roman', 12))

label1.grid(row = 2, column = 1, pady = 1)

value1 = tkinter.Label(lab, text = total_cases,
                       foreground = 'white', background = 'black', font = ('Times new Roman', 12))
value1.grid(row = 3, column = 1, pady = 1)

label2 = tkinter.Label(lab, text = 'Total Recovered Cases',
                       foreground = 'white', background = 'black', font = ('Times new Roman', 12))
label2.grid(row = 4, column = 1, pady = 1)

value2 = tkinter.Label(lab, text = total_recovered,
                       foreground = 'white', background = 'black', font = ('Times new Roman', 12))
value2.grid(row = 5, column = 1, pady = 1)

label3 = tkinter.Label(lab, text = 'Total Death Cases',
                       foreground = 'white', background = 'black', font = ('Times new Roman', 12))
label3.grid(row = 6, column = 1, pady = 20)


value3 = tkinter.Label(lab, text = total_deaths,
                       foreground = 'white', background = 'black', font = ('Times new Roman', 12))
value3.grid(row = 7, column = 1, pady = 1)


screen.mainloop()