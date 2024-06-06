from math import ceil
import tkinter as tk
import sqlite3
import os
from tkinter import messagebox, IntVar, ttk
from datetime import date
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

        self.cur.execute('INSERT INTO Ceremony VALUES(?, ?, ?, ?, ?)', (Ceremony_name, destination, Date, Description, Price))
        self.con.commit()
    
    def update_data_ceremony_name(self, ceremony_name, new_name):

        self.cur.execute('UPDATE Ceremony SET Ceremony_name = ? WHERE Ceremony_name = ?', (new_name, ceremony_name))
        self.con.commit()

    def update_data_ceremony_destination(self, ceremony_name,new_destination):

        self.cur.execute('UPDATE Ceremony SET Destination = ? WHERE Ceremony_name = ?', (new_destination, ceremony_name))
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
cerem = Ceremony_data(path)

# cerem.insert_data('hallowin', "newyork", 'lj;asdfpo', 'akjsdfhiuaohf', 905843)
# cerem.update_data_ceremony_name('hallowin' , 'La Tomatina')
cerem.close()