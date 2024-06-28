from math import ceil
import tkinter as tk
import customtkinter as ctk
import sqlite3
import re
from tkinter import messagebox, ttk
from datetime import date
from tkcalendar import Calendar
import smtplib, requests
from email.message import EmailMessage
from tktimepicker import AnalogPicker


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

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Ceremony(Ceremony_name TEXT PRIMARY KEY, Destination TEXT, Date TEXT, Description TEXT,  Time TEXT)"
        )
        self.con.commit()

    def insert_data(
        self,
        Ceremony_name: str,
        destination: str,
        Date: str,
        Description: str,
        Time: str,
    ):
        self.cur.execute(
            "INSERT INTO Ceremony VALUES(?, ?, ?, ?, ?)",
            (Ceremony_name, destination, Date, Description, Time),
        )
        self.con.commit()

    def select_data(self):

        self.cur.execute("SELECT * FROM Ceremony")
        ceremonies = self.cur.fetchall()
        return ceremonies

    def select(self, Ceremony_name: str):

        self.cur.execute(
            "SELECT * FROM Ceremony WHERE Ceremony_name = ?", (Ceremony_name,)
        )
        cerm = self.cur.fetchone()
        return cerm

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

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Manager(Ceremony_name TEXT PRIMARY KEY, Destination TEXT, Date TEXT, Description TEXT, Time TEXT)"
        )
        self.con.commit()

    def insert_data(
        self,
        Ceremony_name: str,
        destination: str,
        Date: str,
        Description: str,
        Price: int,
    ):
        self.cur.execute(
            "INSERT INTO Manager VALUES(?, ?, ?, ?, ?)",
            (Ceremony_name, destination, Date, Description, Price),
        )
        self.con.commit()

    def select_data(self):

        self.cur.execute("SELECT * FROM Manager")
        ceremonies = self.cur.fetchall()
        return ceremonies


class Customer_data:

    def __init__(self, path):

        self.path = path
        self.con, self.cur = self.connector()
        self.create_table()

    def connector(self):

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        return con, cur

    def create_table(self):

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Customer(Name TEXT PRIMARY KEY, Email TEXT, Number integer, Ceremony_name TEXT, Time TEXT, Date TEXT)"
        )
        self.con.commit()

    def insert_customer(self, name: str, email: str, number: int, ceremony_name: str, ceremony_time: str, ceremony_date: str):

        self.cur.execute(
            "INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?)",
            (name, email, number, ceremony_name, ceremony_time, ceremony_date),
        )
        self.con.commit()

    def select(self):

        self.cur.execute("SELECT * FROM Customer")
        custom = self.cur.fetchall()
        return custom


path = "C:/Users/salam/Desktop/testing/testing_project.db"
#
ceremony = Ceremony_data(path)
manager = Manager(path)
while 1:

    ctk.set_appearance_mode("System")
    # root1 = tk.Tk()
    root1 = ctk.CTk()
    root1.geometry("900x800")
    root1.title("Ceremony")
    frame = ctk.CTkFrame(root1, width=800, height=700, fg_color="lightgray")
    frame.place(x=50, y=50)
    name = ctk.StringVar()
    destination = ctk.StringVar()

    # Ceremony name
    ctk.CTkLabel(
        root1, text="Ceremony Name :", bg_color="lightgray", font=("Arial", 20, "bold")
    ).place(x=90, y=80)
    ceremony_name_entry = ctk.CTkEntry(
        root1,
        font=("Arial", 17, "bold"),
        textvariable=name,
        width=600,
        height=30,
        bg_color="lightgray",
    )
    ceremony_name_entry.place(x=175, y=120)
    # Destination
    ctk.CTkLabel(
        root1, text="Destination : ", font=("Arial", 20, "bold"), bg_color="lightgray"
    ).place(x=90, y=170)
    destination_entry = ctk.CTkEntry(
        root1,
        font=("Arial", 17, "bold"),
        textvariable=destination,
        width=600,
        height=30,
        bg_color="lightgray",
    )
    destination_entry.place(x=170, y=210)

    # Date
    d = ""

    def db():
        dr = ctk.CTk()
        dr.geometry("250x250")
        today = date.today()

        calender = Calendar(
            dr,
            selectmode="day",
            year=today.year,
            month=today.month,
            day=today.day,
            mindate=today,
        )
        calender.place(x=30, y=20)

        def confirm():
            global d
            d = calender.get_date()

            ctk.CTkLabel(
                root1,
                text=f"Ceremony date: {d}",
                font=("Arial", 13, "bold"),
                bg_color="lightgray",
            ).place(x=200, y=340)
            dr.destroy()

        b = ctk.CTkButton(
            dr,
            text="confirm",
            bg_color="lightgray",
            text_color="black",
            command=confirm,
        )
        b.place(x=50, y=200)

        dr.mainloop()

    dbutton = ctk.CTkButton(
        root1,
        text="Date",
        bg_color="lightgray",
        fg_color="green",
        font=("Arial", 13, "bold"),
        text_color="black",
        command=db,
    )
    dbutton.place(x=200, y=300)
    # Time of ceremony
    selected_time = ""
    st = ""

    def dtime():
        root = ctk.CTk()
        time_picker = AnalogPicker(root)
        time_picker.pack()

        def x():
            global selected_time, st
            selected_time = time_picker.time()
            st = f"{selected_time[0]}:{selected_time[1]} {selected_time[2]}"
            ctk.CTkLabel(
                root1,
                text=f"Ceremony time: {st}",
                font=("Airal", 13, "bold"),
                bg_color="lightgray",
            ).place(x=500, y=340)
            root.destroy()

        b = ctk.CTkButton(root, text="confirm", command=x)
        b.pack()
        root.mainloop()

    tb = ctk.CTkButton(
        root1,
        text="Time",
        text_color="black",
        font=("Arial", 13, "bold"),
        bg_color="lightgray",
        fg_color="green",
        command=dtime,
    )
    tb.place(x=500, y=300)

    # Description
    # description = ctk.StringVar()
    ctk.CTkLabel(
        root1, text="Description :", font=("Arial", 20, "bold"), bg_color="lightgray"
    ).place(x=90, y=390)
    describe = ctk.CTkTextbox(root1, width=500, height=100, font=("Arial", 15))

    describe.place(x=170, y=420)

    # Countinue(yes/no)
    c = tk.IntVar()
    check = ctk.CTkCheckBox(
        root1,
        text="want to create anothor ceremony",
        bg_color="lightgray",
        font=("Arial", 14, "bold"),
        variable=c,
    )
    check.place(x=260, y=570)
    x = 0

    def cont():

        global t, x, n, dest, d, ch, st
        n = name.get()
        dest = destination.get()
        t = describe.get("1.0", "end-1c")
        ch = c.get()
        if (
            bool(t) == True
            and bool(n) == True
            and bool(dest) == True
            and bool(d) == True
            and bool(st) == True
        ):
            messagebox.showinfo("ceremony", "Your ceremony created.")
            x = 1
            root1.destroy()

        else:
            messagebox.showerror("Incomplete field", "Please complete the fields.")

    b = ctk.CTkButton(
        root1, text="submit", command=cont, font=("Arial", 15), bg_color="lightgray"
    )
    b.place(x=350, y=650)
    root1.mainloop()

    if x == 0:

        r = ctk.CTk()

        r.geometry("300x200")
        tk.Label(
            r,
            text="Do you want continue?",
            font=("Arial", 15),
        ).place(x=70, y=10)
        v = tk.IntVar()
        r1 = ctk.CTkRadioButton(r, text="yes", variable=v, value=0, font=("Arial", 12))
        r1.place(x=80, y=50)
        r2 = ctk.CTkRadioButton(r, text="no", variable=v, value=1, font=("Arial", 12))
        r2.place(x=150, y=50)
        b = ctk.CTkButton(
            r,
            text="Ok",
            font=("Arial", 12),
            bg_color="lightblue",
            command=lambda: r.destroy(),
        )
        b.place(x=70, y=90)
        r.mainloop()

        if v.get() == 0:
            continue

        else:
            break

    elif ch == 0:

        ceremony.insert_data(n, dest, d, t, st)
        manager.insert_data(n, dest, d, t, st)
        break

    else:

        ceremony.insert_data(n, dest, d, t, st)
        manager.insert_data(n, dest, d, t, st)
        continue

ceremonies = ceremony.select_data()
# print(ceremonies)

customer = Customer_data(path)

if len(ceremonies):

    names = [c[0] for c in ceremonies]
    x = len(ceremonies)
    i = 0
    while 1:

        if i == x:
            break
#
        root2 = ctk.CTk()
        root2.geometry("900x400")
        frame = ctk.CTkFrame(root2, width=800, height=350, fg_color='lightgray')
        frame.configure(fg_color='lightgray')
        frame.place(x=50, y=10)
        root2.title("Ticket")
        select = ""

        def selected(event):
            global select
            global ctime, cdata
            select = combo.get()
            cdata = ceremony.select(select)
            ctk.CTkLabel(root2, text=f'                            ',
                         font=("Arial", 14, "bold"), bg_color='lightgray'
            ).place(x=280, y=70)
            ctk.CTkLabel(
                root2,
                text=f"Ceremony name: {cdata[0]}",
                font=("Arail", 14, "bold"),bg_color='lightgray'
            ).place(x=150, y=70)
            ctk.CTkLabel(root2, text=f'                            ',
                         font=("Arial", 14, "bold"), bg_color='lightgray'
            ).place(x=600, y=70)
            ctk.CTkLabel(
                root2,
                text=f"Ceremony destination: {cdata[1]}",
                font=("Arail", 14, "bold"),bg_color='lightgray'
            ).place(x=450, y=70)
            ctk.CTkLabel(
                root2,
                text=f"Ceremony date: {cdata[2]}",
                font=("Arail", 14, "bold"),bg_color='lightgray'
            ).place(x=150, y=100)
            ctk.CTkLabel(
                root2,
                text=f"Ceremony time: {cdata[4]}",
                font=("Arail", 14, "bold"),bg_color='lightgray'
            ).place(x=450, y=100)

        combo = ttk.Combobox(root2, values=names, width=30,
                             font=("Arial", 15, "bold")
        )
        combo.bind("<<ComboboxSelected>>", selected)
        combo.current()
        combo.place(x=300, y=30)

        # User name
        uname = tk.StringVar()
        ctk.CTkLabel(root2, text="Your name: ", bg_color='lightgray',font=("Arial", 15, "bold")).place(
            x=60, y=160
        )
        un = ctk.CTkEntry(root2, font=("Arial", 15), bg_color='lightgray',width=200,textvariable=uname)
        un.place(x=155, y=160)

        # Number
        num = ''
        def s():
            global num
            num = 0
            num = spin.get()


        ctk.CTkLabel(root2, text="Your number:", bg_color='lightgray',font=("Arial", 15, "bold")).place(
            x=420, y=155
        )
        spin = tk.Spinbox(
            root2,
            from_=0,
            to=20,
            width=30,
            relief="sunken",
            repeatdelay=500,
            repeatinterval=400,
            font=("Arial", 12, "bold"),
            command=s,
        )
        spin.config(justify="center", bd=4)
        spin.place(x=670, y=200)

        uemail = ctk.StringVar()
        ctk.CTkLabel(
            root2, text="Your email: ", font=("Arial", 14, "bold"),
            bg_color='lightgray'
        ).place(x=60, y=230)
        un = ctk.CTkEntry(
            root2, font=("Arial", 15, "bold"), width=350, textvariable=uemail
            ,bg_color='lightgray'
        )
        un.place(x=150, y=230)

        cn = ""
        ce = ""
        val = 0
        def sub():
            global cn, ce ,val

            cn = uname.get()
            ce = uemail.get()
            if bool(select) == False:
                messagebox.showerror(
                    "Ceremony not selected", "Please choose your ceremony."
                )
            else:
                if bool(cn) == False or bool(ce) == False or bool(num) == False:
                    messagebox.showerror(
                        "Blank field", "Please complete your informations."
                    )
                else:
                    pat = re.compile(
                        r"^[a-zA-Z0-9].+[_\\|/?.,]*[a-zA-Z0-9].+[@]gmail\.com$"
                    )

                    result = False
                    result = re.search(pat, ce)

                    if bool(result) == False:
                        messagebox.showerror(
                            "Invalid email", "Please enter your gmail correct!"
                        )

                    else:
                        messagebox.showinfo(
                            "Complete", f"You buy the ticket."
                        )
                        val = 1
                        root2.destroy()

        button = ctk.CTkButton(
            root2, text="Submit", font=("Arial", 12, "bold"), command=sub,
            bg_color='lightgray', fg_color='green'
        )
        button.place(x=300, y=300)

        root2.mainloop()
        # print(bool(select))
        # print(select)
        if (
            bool(select) == False
            or bool(cn) == False
            or bool(ce) == False
            or bool(num) == False
            or val == 0
        ):

            r1 = ctk.CTk()
            r1.geometry("200x200")
            ctk.CTkLabel(r1, text="Do you want to continue?",
                         font=("Arial", 13, "bold")
            ).place(x=20, y=10)

            v = tk.IntVar()
            R1 = ctk.CTkRadioButton(r1, text="yes", variable=v, value=1)
            R1.place(x=30, y=60)
            R1 = ctk.CTkRadioButton(r1, text="no", variable=v, value=0)
            R1.place(x=100, y=60)

            def e():

                # if v.get():
                #     messagebox.showinfo("", "continue")
                # else:
                #     messagebox.showinfo("", "goodbye")

                r1.destroy()

            b = ctk.CTkButton(r1, text="Ok", width=75, fg_color="green",command=e)
            b.place(x=40, y=120)
            r1.mainloop()
            if v.get():
                x += 1
                i += 1
                continue
            else:
                break
        else:

            customer.insert_customer(cn, ce, num, select, cdata[4], cdata[2])
            names.remove(select)
            i += 1
customer = Customer_data(path)
cust = customer.select()
cust.sort(key=lambda x: x[5])
# print(cust)

host = "smtp.gmail.com"
sender = "send.maz.pro@gmail.com"
password = "wlua wcep xllo ktla"
port_ssl = 465
today = date.today()
today = str(today)
today = today.split('-')
day = today[2]
month = today[1][1]
year = today[0][2:]
print(month, day, year)
if bool(cust):
    # THAT FOR SENDING GMAIL
    for i in cust:

        customer_name = i[0]
        customer_email = i[1]
        customer_num = i[2]
        customer_ceremony = i[3]
        ceremony_time = i[4]
        ceremony_date = i[5]

        # managermessage = EmailMessage()

        message = EmailMessage()
        message["Subject"] = "Ticket"
        message["From"] = sender
        message["To"] = customer_email
        message.set_content(
            f"Hello dear {customer_name}.\nYou buy ticket for {customer_ceremony}.\nIt holds in {ceremony_date} at {ceremony_time}.\nThanks for your trust."
        )

        try:
            with smtplib.SMTP_SSL(host, port_ssl) as server:

                server.login(sender, password)
                server.send_message(message)
                server.noop()
                print("Email sent.")
        except smtplib.SMTPAuthenticationError:
            print("Please check your email or password.")
        except Exception as e:
            print(f"An strange error: {e}")

# 6 27 24
# ['7', '19', '24']
# ['7', '31', '24']

# print(cust)
customer = Customer_data(path)
cust = customer.select()
cust.sort(key=lambda x: x[5])
host = "smtp.gmail.com"
sender = "send.maz.pro@gmail.com"
password = "wlua wcep xllo ktla"
port_ssl = 465
if bool(cust):

    for i in cust:
        today = date.today()
        tday = today.day
        tmonth = today.month
        tyear = str(today.year)[2:]
        cername = i[3]
        certime = i[4]
        d = i[5].split('/')
        cerdate = i[5]
        cday = int(d[1])
        cmonth = int(d[0])
        cyear = d[2]
        if tmonth == cmonth:
            r = cday - tday
        elif cmonth - tmonth != 0:
            r = 30 * (cmonth - tmonth) - tday + cday

        if r <= 7:
            message = EmailMessage()
            message["Subject"] = "Ticket"
            message["From"] = sender
            message["To"] = sender
            message.set_content(
                f"Hello dear manager.\nWe have a ceremony named {cername}.\nIt holds in {cerdate} at {certime}.\nBe ready.\nGoodbye."
            )

            try:
                with smtplib.SMTP_SSL(host, port_ssl) as server:

                    server.login(sender, password)
                    server.send_message(message)
                    server.noop()
                    print("Email sent.")
            except smtplib.SMTPAuthenticationError:
                print("Please check your email or password.")
            except Exception as e:
                print(f"An strange error: {e}")


        elif r > 7:
            x = 0
            while 1:
                today1 = date.today()
                day = today1.day
                month = today1.month
                r1 = 30 * (cmonth - month) - day + cday
                if r1 == 7:
                    message = EmailMessage()
                    message["Subject"] = "Ticket"
                    message["From"] = sender
                    message["To"] = sender
                    message.set_content(
                        f"Hello dear manager.\nWe have a ceremony named {cername}.\nIt holds in {cerdate} at {certime}.\nBe ready.\nGoodbye."
                    )

                    try:
                        with smtplib.SMTP_SSL(host, port_ssl) as server:

                            server.login(sender, password)
                            server.send_message(message)
                            server.noop()
                            print("Email sent.")
                    except smtplib.SMTPAuthenticationError:
                        print("Please check your email or password.")
                    except Exception as e:
                        print(f"An strange error: {e}")
                    x = 1
                    break
            if x == 1:
                continue


else:
    print("goodbye")
