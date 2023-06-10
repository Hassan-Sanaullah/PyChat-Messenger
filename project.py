import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from backend import estConnection, new, estDisconnect

#Main window
root = tk.Tk()
root.title("PyChat")
root.geometry("1100x800+800+50")
root.iconbitmap(r"c:\Users\DELL\Documents\Lab_work\python\icon1.ico")
root.configure(bg="#525461")

#grid configure for main root window
row_num = 5
col_num = 6

for row in range(row_num):
    root.rowconfigure(row, weight=1)
for col in range(col_num):
    root.columnconfigure(col, weight=1)

# making frame
fr = tk.Frame(root, width = '800', height = '700', background="#272B37")
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

# All GUI Icons and Images
login_btn_photo = tk.PhotoImage(file='python\log_in_button.png')
signup_btn_photo = tk.PhotoImage(file='python\sign_up_button.png')
back_btn_photo = tk.PhotoImage(file="python\eback_button.png")
logo = tk.PhotoImage(file="python\logo.PNG")


def clear_frame():
    # Destroy all widgets inside the frame
    for widget in fr.winfo_children():
        widget.destroy()

def signup_func(event):
    clear_frame()

    username_label = ttk.Label(fr, text="Username ", font=("Lucida Sans", 12), background="#272B37", foreground="White")
    username_label.grid(row=1, column=0)

    passwd_label = ttk.Label(fr, text='Password', font=("Lucida Sans", 12), background="#272B37", foreground="White")
    passwd_label.grid(row=2, column=0)

    
    user = tk.Entry(fr, background="#525461", foreground="White" )
    user.grid(row=1, column=1, sticky=tk.W)
    user.focus()

    password = tk.Entry(fr, show="●", background="#525461", foreground="White")
    password.grid(row=2, column=1, sticky=tk.W)

    btn = tk.Button(fr, image=signup_btn_photo,bg='#272B37', bd ="1")
    btn["border"] = "0"
    btn.bind("<Button>", lambda event: save(user, password))
    btn.grid(row=3, column=0, columnspan=2, sticky=tk.S)

    back_btn = tk.Button(fr, image=back_btn_photo, bg="#272B37")
    back_btn["border"] = "0"
    back_btn.bind("<Button>", main)
    back_btn.grid(row=4, column=0, columnspan=2)


def login_func(event):
    clear_frame()

    username_label = ttk.Label(fr, text="Username ", font=("Lucida Sans", 12), background="#272B37", foreground="White")
    username_label.grid(row=1, column=0)

    passwd_label = ttk.Label(fr, text='Password', font=("Lucida Sans", 12), background="#272B37", foreground="White")
    passwd_label.grid(row=2, column=0)

    username = tk.StringVar()
    user = tk.Entry(fr, textvariable=username, background="#525461", foreground="White" )
    username.get()
    user.grid(row=1, column=1, sticky=tk.W)
    user.focus()

    passwd = tk.StringVar()
    password = tk.Entry(fr, textvariable=passwd, show="●", background="#525461", foreground="White")
    passwd.get()
    password.grid(row=2, column=1, sticky=tk.W)

    btn = tk.Button(fr, image=login_btn_photo,bg='#272B37', bd ="1")
    btn["border"] = "0"
    btn.bind("<Button>")
    btn.grid(row=3, column=0, columnspan=2, sticky=tk.S)

    back_btn = tk.Button(fr, image=back_btn_photo, bg="#272B37")
    back_btn["border"] = "0"
    back_btn.bind("<Button>", main)
    back_btn.grid(row=4, column=0, columnspan=2)


def main(event):
    clear_frame()

    

    title = ttk.Label(fr, image=logo, background="#272B37")
    title.grid(row=0, column=1, columnspan=4)

    # main Login button
    login_btn = tk.Button(fr, image=login_btn_photo, bg="#272B37", bd ="1")
    login_btn["border"] = "0"
    login_btn.bind("<Button>", login_func)
    login_btn.grid(row=2, column=1, columnspan=4)

    
    signup_btn = tk.Button(fr, image=signup_btn_photo, bg="#272B37", bd ="1")
    signup_btn["border"] = "0"
    signup_btn.bind("<Button>", signup_func)
    signup_btn.grid(row=3, column=1,  columnspan=4)

    root.mainloop()

estConnection()

event = 1
main(event)