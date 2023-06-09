import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from backend import new

#Main window
root = tk.Tk()
root.title("Messenger")
root.geometry("1100x800+800+50")
root.iconbitmap(r"c:\Users\DELL\Documents\Lab_work\python\icon.ico")
root.configure(bg="#525461")

#grid configure for main root window
row_num = 5
col_num = 6

for row in range(row_num):
    root.rowconfigure(row, weight=1)
for col in range(col_num):
    root.columnconfigure(col, weight=1)


fr = tk.Frame(root, width = '800', height = '700', background='#272B37')
fr.grid( row=1, column=1, rowspan=3, columnspan=4, sticky=tk.NSEW)

#grid configure for frame
for row in range(row_num):
    fr.rowconfigure(row, weight=1)
for col in range(col_num):
    fr.columnconfigure(col, weight=1)

def save(user, password):
    username = user.get()
    passwd = password.get()

    new(username, passwd)

def signup_func(event):
    login_btn.destroy()
    signup_btn.destroy()
    title.destroy()

    username_label = ttk.Label(fr, text="Username ", font=("Roboto", 12), background="#272B37", foreground="White")
    username_label.grid(row=1, column=0)

    passwd_label = ttk.Label(fr, text='Password', font=("Roboto", 12), background="#272B37", foreground="White")
    passwd_label.grid(row=2, column=0)

    
    user = tk.Entry(fr, background="#525461", foreground="White" )
    user.grid(row=1, column=1, sticky=tk.W)

    password = tk.Entry(fr, show="●", background="#525461", foreground="White")
    password.grid(row=2, column=1, sticky=tk.W)

    btn = tk.Button(fr, image=signup_btn_photo,font="Roboto",bg='#272B37', fg="White", bd ="1")
    btn["border"] = "0"
    btn.bind("<Button>", lambda event: save(user, password))
    btn.grid(row=3, column=0, columnspan=2, ipadx=60)


def login_func(event):
    login_btn.destroy()
    signup_btn.destroy()
    title.destroy()

    username_label = ttk.Label(fr, text="Username ", font=("Roboto", 12), background="#272B37", foreground="White")
    username_label.grid(row=1, column=0)

    passwd_label = ttk.Label(fr, text='Password', font=("Roboto", 12), background="#272B37", foreground="White")
    passwd_label.grid(row=2, column=0)

    username = tk.StringVar()
    user = tk.Entry(fr, textvariable=username, background="#525461", foreground="White" )
    username.get()
    user.grid(row=1, column=1, sticky=tk.W)

    passwd = tk.StringVar()
    password = tk.Entry(fr, textvariable=passwd, show="●", background="#525461", foreground="White")
    passwd.get()
    password.grid(row=2, column=1, sticky=tk.W)

    btn = tk.Button(fr, image=login_btn_photo,font="Roboto",bg='#272B37', fg="White", bd ="1")
    btn["border"] = "0"
    btn.bind("<Button>")
    btn.grid(row=3, column=0, columnspan=2, ipadx=60)

    
    # l = ttk.Label(root, text = username).pack()


title = ttk.Label(fr, text="Messenger", font=("Roboto", 30), background="#272B37", foreground="White")
title.grid(row=0, column=1)

# main Login button
login_btn_photo = tk.PhotoImage(file='python\log_in_button.png')
login_btn = tk.Button(fr, image=login_btn_photo,font="Roboto", bg="#272B37", fg="White", bd ="1")
login_btn["border"] = "0"
login_btn.bind("<Button>", login_func)
login_btn.grid(row=2, column=1)

signup_btn_photo = tk.PhotoImage(file='python\sign_up_button.png')
signup_btn = tk.Button(fr, image=signup_btn_photo,font="Roboto", bg="#272B37", fg="White", bd ="1")
signup_btn["border"] = "0"
signup_btn.bind("<Button>", signup_func)
signup_btn.grid(row=3, column=1)

root.mainloop()