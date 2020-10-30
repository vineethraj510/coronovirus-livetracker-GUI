import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL.ImageTk import PhotoImage
from PIL import Image


screen = tkinter.Tk()
screen.title('Coronavirus Tracker')
screen.geometry('600x600')
country="india"


photo = PhotoImage(Image.open("IMAGE.jpg"))
lab = Label(screen, image = photo)
lab.grid(row=0, column=0)

# This function is useful in getting individual country details
def indiv_country():
    country=c.get()
    page=requests.get('https://www.worldometers.info/coronavirus/country/' + country)
    Soup = BeautifulSoup(page.content, 'html.parser')
    info = Soup.find_all(class_='maincounter-number')

    
    a = [items.get_text() for items in info]
    tot_cases = Label(lab,foreground = 'white', background = 'black', font = ('Times new Roman', 12),text=country + " Total Cases ")
    tot_cases.grid(column=100, row=10)

    cases_value = Label(lab, text = a[0],foreground = 'white', background = 'black', font = ('Times new Roman', 12))
    cases_value.grid(column=100, row=11)
    

    tot_deaths = Label(lab,foreground = 'white', background = 'black', font = ('Times new Roman', 12),text=country + " Total Deaths")
    tot_deaths.grid(column=100, row=12)
    

    deaths_value= Label(lab, text = a[1],foreground = 'white', background = 'black', font = ('Times new Roman', 12))

    deaths_value.grid(column=100, row=13)
    
    tot_recovered = Label(lab,foreground = 'white', background = 'black', font = ('Times new Roman', 12),text=country + " Total Recovered")
    tot_recovered.grid(column=100, row=14)
    
    recover_value= Label(lab, text = a[2],foreground = 'white', background = 'black', font = ('Times new Roman', 12))
    recover_value.grid(column=100, row=15)
    
    

#This is for getting individually country data

lbl = Label(lab, text = 'Please enter the country you want to check',
                       foreground = 'white', background = 'black', font = ('Times new Roman', 14))
lbl.grid(column=100, row=1)
c = Entry(lab,  foreground = 'black', font = ('Times new Roman', 12) )
c.grid(column = 100, row = 2)


search_Btn = tkinter.Button(lab, text="search", command=indiv_country,bg="white")  # Here i created a search button
search_Btn.grid(column = 100, row = 3)

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