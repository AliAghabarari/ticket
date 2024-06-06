import tkinter as tk
import sqlite3
import os
from tkinter import messagebox, IntVar, ttk

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

        self.cur.execute('CREATE TABLE IF NOT EXISTS Ceremony(Ceremony_name TEXT PRIMARY KEY, Address TEXT, Date TEXT)')
        self.con.commit()
    
    def insert_data(self, Ceremony_name, Address, Date):

        self.cur.execute('INSERT INTO Ceremony VALUES(?, ?, ?)', (Ceremony_name, Address, Date))
        self.con.commit()
    
    def update_data_ceremony_name(self, new_name):

        self.cur.execute('UPDATE Ceremony SET Ceremony_name = ?')