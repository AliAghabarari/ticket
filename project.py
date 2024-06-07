from math import ceil
import tkinter as tk
import sqlite3
import os
from tkinter import StringVar, messagebox, IntVar, ttk
from datetime import date
from tkcalendar import Calendar
import smtplib, requests

'''
https://7learn.com/blog/tkinter-in-python


'''

class Ceremony_data:

    def __init__(self, path):

        self.path = path
        self.con, self.cur = self.connector()
        self.create = self.create_table()
    
    def connector(self):

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        return con, cur
    
    def create_table(self):

        self.cur.execute('CREATE TABLE IF NOT EXISTS Ceremony(Ceremony_name TEXT PRIMARY KEY, Destination TEXT, Date TEXT, Description TEXT, Price integer)')
        self.con.commit()
    
    def insert_data(self, Ceremony_name : str, destination : str, Date, Description : str, Price : int):

        self.cur.execute('INSERT INTO Ceremony VALUES(?, ?, ?, ?, ?)',
                          (Ceremony_name, destination, Date, Description, Price))
        self.con.commit()
    
    def update_data_ceremony_name(self, ceremony_name, new_name):

        self.cur.execute('UPDATE Ceremony SET Ceremony_name = ? WHERE Ceremony_name = ?', 
                         (new_name, ceremony_name))
        self.con.commit()

    def update_data_ceremony_destination(self, ceremony_name,new_destination):

        self.cur.execute('UPDATE Ceremony SET Destination = ? WHERE Ceremony_name = ?',
                          (new_destination, ceremony_name))
        self.con.commit()

    def update_data_ceremony_date(self, ceremony_name,new_date):

        self.cur.execute('UPDATE Ceremony SET Date = ? WHERE Ceremony_name = ?', (new_date, ceremony_name))
        self.con.commit() 

    def update_data_ceremony_description(self, ceremony_name,new_description):

        self.cur.execute('UPDATE Ceremony SET Description = ? WHERE Ceremony_name = ?', (new_description, ceremony_name))
        self.con.commit()

    def update_data_ticket_price(self, ceremony_name,new_price):

        self.cur.execute('UPDATE Ceremony SET Price = ? WHERE Ceremony_name = ?', (new_price, ceremony_name))
        self.con.commit()
    def close(self):

        self.con.close()



path = 'C:/Users/salam/Desktop/testing/testing_project.db'
# cerem = Ceremony_data(path)

# # cerem.insert_data('hallowin', "newyork", 'lj;asdfpo', 'akjsdfhiuaohf', 905843)
# cerem.update_data_ceremony_destination('hallowin' , 'washingtion')
# cerem.close()

ceremony = Ceremony_data(path)

root1 = tk.Tk()
root1.config(bg='powder blue')
root1.geometry('900x700')
name = tk.StringVar()
destination = tk.StringVar()
price = tk.IntVar()

#Ceremony name
ttk.Label(root1, text='Ceremony Name:',font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=5, pady=5)
ceremony_name_entry = ttk.Entry(root1,font=('Arial', 15, 'bold') ,textvariable=name)
ceremony_name_entry.grid(column=1, row=0, padx=5, pady=5)
ceremony_name_entry.focus()

#Destination
ttk.Label(root1, text='Destination: ', font=("Arial", 10, 'bold')).grid(column=3, row=0, padx=3, pady=4)
destination_entry = ttk.Entry(root1, font=("Arial", 15, 'bold'), textvariable=destination )
destination_entry.grid(column=4, row=0, padx=4, pady=4)
destination_entry.focus()

#Date
today = date.today()
ttk.Label(root1,text='Date: ' ,font=("Arial", 20, 'bold')).grid(column=0, row=2, pady=15)
calender = Calendar(root1, selectmode='day', year=today.year, month=today.month, day=today.day, mindate=today)
calender.grid(column=1, row=3)

#Price
ttk.Label(root1, text="Price: ", font=("Arial", 15, "bold")).grid(column=0, row=10, padx=5, pady=50)
ticket_price = ttk.Entry(root1, font=("Arial", 15, 'bold'), textvariable=price)
ticket_price.grid(column=1, row=10)
ticket_price.focus()

#Description
ttk.Label(root1, text="Description: ", font=("Arial", 15, "bold")).grid(column=0, row=15)
describe = tk.Text(root1, width=50, height=5, font=("Arial", 12))
describe.grid(column=1, row=16, pady=10)
describe.focus()

root1.mainloop()

x = name.get()
print(x)
y = destination.get()
print(y)
z = calender.get_date()
print(z)
p = price.get()
print(p)
t = describe.get('1.0', tk.END)
print(t)