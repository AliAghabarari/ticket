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

    def select(self, Ceremony_name: str):

        self.cur.execute("SELECT * FROM Ceremony WHERE Ceremony_name = ?", (Ceremony_name, ))
        cerm = self.cur.fetchone()
        return cerm
    
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

class Manager:

    def __init__(self, path):

        self.path = path
        self.con, self.cur = self.connector()
        self.create_table()
    
    def connector(self):

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        return con, cur
    
    def create_table(self):
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS Manager(Ceremony_name TEXT PRIMARY KEY, Destination TEXT, Date TEXT, Description TEXT, Price integer)')
        self.con.commit()
    
    def insert_data(self, Ceremony_name : str, destination : str, Date : str, Description : str, Price : int):
        self.cur.execute('INSERT INTO Manager VALUES(?, ?, ?, ?, ?)',
                         (Ceremony_name, destination, Date, Description, Price))
        self.con.commit()

    def select_data(self):

        self.cur.execute("SELECT * FROM Manager")
        ceremonies = self.cur.fetchall()
        return ceremonies
    
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
manager = Manager(path)
while 1:
    root1 = tk.Tk()
    root1.config(bg='lightgreen')
    root1.geometry('1500x700')
    root1.title('Ceremony')
    name = tk.StringVar()
    destination = tk.StringVar()
    price = tk.IntVar()

    #Ceremony name
    tk.Label(root1, text='Ceremony Name:',font=('Arial', 10, 'bold')).grid(column=0, row=0,padx=3, pady=4)
    ceremony_name_entry = tk.Entry(root1,font=('Arial', 15, 'bold'),bg='white' ,textvariable=name)
    ceremony_name_entry.grid(column=1, row=0,padx=4,  pady=4)
    ceremony_name_entry.focus()

    #Destination
    tk.Label(root1, text='Destination: ', font=("Arial", 10, 'bold')).grid(column=3, row=0, padx=30, pady=4)
    destination_entry = tk.Entry(root1, font=("Arial", 15, 'bold'), bg='white', textvariable=destination )
    destination_entry.grid(column=4, row=0, padx=4, pady=4)
    destination_entry.focus()


    #Price
    tk.Label(root1, text="Price: ", font=("Arial", 15, "bold")).grid(column=0, row=3, padx=5, pady=50)
    ticket_price = tk.Entry(root1, font=("Arial", 15, 'bold'),bg='white',  textvariable=price)
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
    describe = tk.Text(root1, width=50, height=5, font=("Arial", 15), bg='white' , fg='black')
    describe.grid(column=5, row=5, ipady=30)
    describe.focus()


    #Countinue(yes/no)
    var = tk.IntVar()
    tk.Label(root1,bg='green' , font=("Arial", 12, "bold"), text="Do you want to create\nanother ceremony?").grid(row=6, column=0, pady=40)
    R1 = tk.Radiobutton(root1, text="yes", variable=var, value=1, bg='lightblue', font=("Arial", 12))
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
    
    if var.get() == 0:

        r = tk.Tk()
        r.geometry("300x200")
        tk.Label(r, text='Are you sure to cancelling\ncreating any cermony?', font=("Arial", 15)).grid(column=0, row=0)
        v = tk.IntVar()
        r1 = tk.Radiobutton(r, text='yes', variable=v, value=1, bg='lightgreen', font=("Arial", 12))
        r1.grid(column=0, row=2, pady=20)
        r2 = tk.Radiobutton(r, text='no', variable=v, value=0, bg='red', font=("Arial", 12))
        r2.grid(column=1, row=2, pady=20)
        b = tk.Button(r, text='Ok', font=("Arial", 12), bg='lightblue', command=lambda: r.destroy())
        b.grid(column=0, row=3)
        r.mainloop()
        
        if v.get() == 0: continue

        else: break

    elif var.get() == 2 :
        
        ceremony.insert_data(n, dest, d, t, p)
        manager.insert_data(n, dest, d, t, p)
        break
    
    else:
        
        ceremony.insert_data(n, dest, d, t, p)
        manager.insert_data(n, dest, d, t, p)
        continue

ceremonies = ceremony.select_data()

# print(ceremonies)
if len(ceremonies):

    names = [c[0] for c in ceremonies]
    x = len(ceremonies)
    i = 0
    while 1:

        if i == x: break

        root2 = tk.Tk()
        root2.config(bg="lightgreen")
        root2.geometry('800x700')
        root2.title('Ticket')
        select = ''
        def selected(event):
            global select
            select = combo.get()
            cdata = ceremony.select(select)
            tk.Label(root2, text=f'Ceremony name: {cdata[0]}', font=("Arail", 12), bg='lightgreen').place(x=0, y=100)
            tk.Label(root2, text=f'Ceremony destination: {cdata[1]}', font=("Arail", 12), bg='lightgreen').place(x=300, y=100)
            tk.Label(root2, text=f'Ceremony date: {cdata[2]}', font=("Arail", 12), bg='lightgreen').place(x=0, y=130)
            tk.Label(root2, text=f'Ceremony price: {cdata[4]}', font=("Arail", 12), bg='lightgreen').place(x=300, y=130)

        combo = ttk.Combobox(root2, values=names, width=40)
        combo.bind("<<ComboboxSelected>>", selected)
        combo.current()
        combo.place(x=250, y=10)

        b = tk.Button(root2 ,text='test' ,command=lambda:root2.destroy())
        b.place(x=20, y=50)
        root2.mainloop()
        print(bool(select))
        print(select)
        if bool(select) == False:

            r1 = tk.Tk()
            r1.geometry('300x300')
            tk.Label(r1, text='Do you want to continue?').place(x=100, y=0)
            v = tk.IntVar()
            R1 = tk.Radiobutton(r1, text='yes', variable=v, value=1)
            R1.place(x=100, y=30)
            R1 = tk.Radiobutton(r1, text='no', variable=v, value=0)
            R1.place(x=150, y=30)

            def e():

                if v.get():
                    messagebox.showinfo('', 'continue')
                else:
                    messagebox.showinfo('', 'goodbye')
                
                r1.destroy()

            b = tk.Button(r1, text='Ok', command=e)
            b.place(x=120, y=50)
            r1.mainloop()
            if v.get():
                continue
            else: break
        else:
            names.remove(select)
            i += 1

else:
    print("Goodbye\nYou don`t create any ceremony!!")

