from math import ceil
import tkinter as tk
import sqlite3
import os
from tkinter import messagebox, ttk
from datetime import date
from tkcalendar import Calendar
import smtplib, requests



class Ceremony_data:

    def __init__(self, path):

        self.path = path
        self.con, self.cur = self.connector()
        self.create_table()
    
    def connector(self):

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        return con, cur
    
    def create_table(self):
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS Ceremony(Ceremony_name TEXT PRIMARY KEY, Destination TEXT, Date TEXT, Description TEXT, Price integer)')
        self.con.commit()
    
    def insert_data(self, Ceremony_name : str, destination : str, Date : str, Description : str, Price : int):
        self.cur.execute('INSERT INTO Ceremony VALUES(?, ?, ?, ?, ?)',
                         (Ceremony_name, destination, Date, Description, Price))
        self.con.commit()

    def select_data(self):

        self.cur.execute("SELECT * FROM Ceremony")
        ceremonies = self.cur.fetchall()
        return ceremonies
    # def update_data_ceremony_name(self, ceremony_name, new_name):

    #     self.cur.execute('UPDATE Ceremony SET Ceremony_name = ? WHERE Ceremony_name = ?', 
    #                      (new_name, ceremony_name))
    #     self.con.commit()

    # def update_data_ceremony_destination(self, ceremony_name,new_destination):

    #     self.cur.execute('UPDATE Ceremony SET Destination = ? WHERE Ceremony_name = ?',
    #                       (new_destination, ceremony_name))
    #     self.con.commit()

    # def update_data_ceremony_date(self, ceremony_name,new_date):

    #     self.cur.execute('UPDATE Ceremony SET Date = ? WHERE Ceremony_name = ?', (new_date, ceremony_name))
    #     self.con.commit() 

    # def update_data_ceremony_description(self, ceremony_name,new_description):

    #     self.cur.execute('UPDATE Ceremony SET Description = ? WHERE Ceremony_name = ?', (new_description, ceremony_name))
    #     self.con.commit()

    # def update_data_ticket_price(self, ceremony_name,new_price):

    #     self.cur.execute('UPDATE Ceremony SET Price = ? WHERE Ceremony_name = ?', (new_price, ceremony_name))
    #     self.con.commit()

    def close(self):

        self.con.close()

class Customer_date:

    def __init__(self, path):

        self.path = path
        self.con, self.cur = self.connector()
        self.create_table()
    
    
    def connector(self):

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        return con, cur
    
    def create_talbe(self):

        self.cur.execute('CRATE TABLE IF NOT EXISTS Customer(Name TEXT PRIMARY KEY, Email TEXT, Number integer)')
        self.con.commit()
    
    def insert_customer(self, name : str, email : str, number : int):
        
        self.cur.execute("INSERT INTO Customer VALUES(?, ?, ?)", (name, email, number))
        self.con.commit()

path = 'C:/Users/salam/Desktop/testing/testing_project.db'

ceremony = Ceremony_data(path)

while 1:
    root1 = tk.Tk()
    root1.config(bg='powder blue')
    root1.geometry('1500x700')
    name = tk.StringVar()
    destination = tk.StringVar()
    price = tk.IntVar()

    #Ceremony name
    ttk.Label(root1, text='Ceremony Name:',font=('Arial', 10, 'bold')).grid(column=0, row=0,padx=3, pady=4)
    ceremony_name_entry = ttk.Entry(root1,font=('Arial', 15, 'bold') ,textvariable=name)
    ceremony_name_entry.grid(column=1, row=0,padx=4,  pady=4)
    ceremony_name_entry.focus()

    #Destination
    ttk.Label(root1, text='Destination: ', font=("Arial", 10, 'bold')).grid(column=3, row=0, padx=30, pady=4)
    destination_entry = ttk.Entry(root1, font=("Arial", 15, 'bold'), textvariable=destination )
    destination_entry.grid(column=4, row=0, padx=4, pady=4)
    destination_entry.focus()


    #Price
    ttk.Label(root1, text="Price: ", font=("Arial", 15, "bold")).grid(column=0, row=3, padx=5, pady=50)
    ticket_price = ttk.Entry(root1, font=("Arial", 15, 'bold'), textvariable=price)
    ticket_price.grid(column=1, row=3)
    ticket_price.focus()

    #Date
    today = date.today()
    ttk.Label(root1,text='Date: ' ,font=("Arial", 20, 'bold')).grid(column=0, row=4, pady=15)
    calender = Calendar(root1, selectmode='day', year=today.year, month=today.month, day=today.day, mindate=today)
    calender.grid(column=1, row=5)

    #Description
    description = tk.StringVar()
    tk.Label(root1, text="Description: ", bg='yellow',font=("Arial", 15, "bold")).grid(column=4, row=4)
    describe = tk.Text(root1, width=50, height=5, font=("Arial", 15), bg='gray' , fg='red')
    describe.grid(column=5, row=5, ipady=30)
    describe.focus()


    #Countinue(yes/no)
    var = tk.IntVar()
    tk.Label(root1,bg='green' , font=("Arial", 12, "bold"), text="Do you want to create\nanother ceremony?").grid(row=6, column=0, pady=40)
    R1 = tk.Radiobutton(root1, text="yes", variable=var, value=1, bg='lightgreen', font=("Arial", 12))
    R1.grid(column=0, row=7)
    R1.focus()

    R2 = tk.Radiobutton(root1, text="no", variable=var, value=2, bg='red', font=("Arial", 12))
    R2.grid(column=1, row=7)
    R2.focus()
    def cont():
        
        global t
        t = describe.get('1.0', 'end-1c')
        if var.get() == 1:
            messagebox.showinfo('test', 'continue')
            root1.destroy()
        
        else:
            messagebox.showinfo('test', 'bye')
            root1.destroy()
    b = tk.Button(root1, text='submit', command=cont , bg='gold', font=("Arial", 15))
    b.grid(column=0, row=8, pady=25)

    root1.mainloop()
    n = name.get()
    dest = destination.get()
    d = calender.get_date()
    p = price.get()
    if var.get() == 0: break

    elif var.get() == 2 :
        
        ceremony.insert_data(n, dest, d, t, p)
        break
    
    else:
        
        ceremony.insert_data(n, dest, d, t, p)
        continue

ceremonies = ceremony.select_data()

print(ceremonies)
