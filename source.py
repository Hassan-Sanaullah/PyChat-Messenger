import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from backend import estConnection, account, estDisconnect, get_inbox, get_message

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

base_dir = 'C:\\Users\\DELL\\Documents\\Lab_work\\python\\' # Specify the base directory
# All GUI Icons and Images
login_btn_photo = tk.PhotoImage(file=base_dir+'log_in_button.png')
signup_btn_photo = tk.PhotoImage(file=base_dir+'sign_up_button.png')
back_btn_photo = tk.PhotoImage(file=base_dir+'eback_button.png')
logo = tk.PhotoImage(file=base_dir+'logo.PNG')
logout_btn_photo = tk.PhotoImage(file=base_dir+'logout_button.png')
newmessage_btn_photo = tk.PhotoImage(file=base_dir+'new_message_button.PNG')

# gets name when you click name in inbox and sends it to backend file
def message_backend(message_name, username, option):
    selected_items = message_name.curselection()
    if selected_items:
        index = selected_items[0]
        selected_message = message_name.get(index)

    response = get_message(str(option), str(username), str(selected_message))
    

#gets username and password from entry box and sends it to backend file
def account_backend(user, password, option):

    username = user.get()
    passwd = password.get()

    response = account(username, passwd, option) #CHANGE THE ORDER HERE PLEASE

    if response == 'loginTrue':
        inbox_screen(username)
    elif response == 'loginFalse':
        login_fail = tk.Label(fr, text='Incorrect credentials.Try again')
        login_fail.grid(row=5, column = 2, columnspan=2, bg='#272B37')


def clear_frame():
    # Destroy all widgets inside the frame
    for widget in fr.winfo_children():
        widget.destroy()

def chatting_screen(username):

    # selected_indices = message_name.curselection()
    # selected_message = message_name.get()

    clear_frame()
    print('opened message')
    
    messages = []
    var = tk.Variable(value = messages)
    messages_box = tk.Listbox(fr, listvariable=var, height=6, selectmode=tk.SINGLE, 
    background="#272B37",  foreground="White", font="Roboto")
    messages_box.grid(row=1, column=0, columnspan=6, rowspan=3, sticky=tk.NSEW)

    message_enter = tk.Entry(fr, background="#525461", foreground="White" )
    message_enter.grid(row=4, column=3, columnspan=2, ipadx=12, sticky=tk.E)
    recepient.focus()

    send_btn = tk.Button(fr, text='Send')
    send_btn.bind('<Return', lambda event: message_backend(username, message_enter, 'sendMessage'))
    


def inbox_screen(username):
    clear_frame()
    print('logged in')

    #inbox label on top
    inbox_label = tk.Label(fr, text="Inbox", background="#272B37", foreground="white", font=('Lucida Sans', 20))
    inbox_label.grid(row=0, column=0, columnspan=6, sticky=tk.NS)

    #list of names to display in inbox
    names = get_inbox('inbox', username).split('-')
    var = tk.Variable(value = names)

    #listbox for inbox names
    message_name = tk.Listbox(fr, listvariable=var, height = 6, selectmode=tk.SINGLE, 
    background="#272B37",  foreground="White", font="Roboto")
    message_name.grid(row=1, column=0, columnspan=6, rowspan=3, sticky=tk.NSEW)

    message_name.bind('<<ListboxSelect>>', lambda event : message_backend(message_name, username, 'getMessages'))
    
    #logout button
    logout_btn = tk.Button(fr, image=logout_btn_photo, bg='#272B37', bd ="1")
    logout_btn["border"] = "0"
    logout_btn.bind('<Button>', main)
    logout_btn.grid(row=4, column=5)

    #new message button
    new_message_btn = tk.Button(fr, image=newmessage_btn_photo, bg='#272B37', bd ="1")
    new_message_btn["border"] = "0"
    new_message_btn.bind('<Button>', lambda event: chatting_screen(username))
    new_message_btn.grid(row=4, column=4)

def func_login_signup(option):
    clear_frame()

    username_label = ttk.Label(fr, text="Username:   ", font=("Lucida Sans", 15), background="#272B37", foreground="White")
    username_label.grid(row=1, column=1, columnspan=2, sticky=tk.E)

    passwd_label = ttk.Label(fr, text='Password:  ', font=("Lucida Sans", 15), background="#272B37", foreground="White")
    passwd_label.grid(row=2, column=1, columnspan=2, sticky=tk.E)

    user = tk.Entry(fr, background="#525461", foreground="White" )
    user.grid(row=1, column=2, columnspan=2, ipadx=12, sticky=tk.E)
    user.focus()

    password = tk.Entry(fr, show="●", background="#525461", foreground="White")
    password.grid(row=2, column=3, columnspan=2, ipadx=10, sticky=tk.W)

    # decides the login/ Sign up button to display
    if option == 'signup':
        btn = tk.Button(fr, image=signup_btn_photo,bg='#272B37', bd ="1")
    elif option == 'login':
        btn = tk.Button(fr, image=login_btn_photo,bg='#272B37', bd ="1")
        
    btn["border"] = "0"
    btn.bind("<Button>", lambda event: account_backend(user, password, option))
    btn.grid(row=3, column=2, columnspan=2, sticky=tk.S)
    
    back_btn = tk.Button(fr, image=back_btn_photo, bg="#272B37")
    back_btn["border"] = "0"
    back_btn.bind("<Button>", main)
    back_btn.grid(row=4, column=2, columnspan=2)

def main(event):
    clear_frame()

    

    title = ttk.Label(fr, image=logo, background="#272B37")
    title.grid(row=0, column=1, columnspan=4)

    # main Login button
    login_btn = tk.Button(fr, image=login_btn_photo, bg="#272B37", bd ="1")
    login_btn["border"] = "0"
    login_btn.bind("<Button>", lambda event: func_login_signup('login'))
    login_btn.grid(row=2, column=1, columnspan=4)

    # main sign up button
    signup_btn = tk.Button(fr, image=signup_btn_photo, bg="#272B37", bd ="1")
    signup_btn["border"] = "0"
    signup_btn.bind("<Button>", lambda event: func_login_signup('signup'))
    signup_btn.grid(row=3, column=1,  columnspan=4)
    
    root.mainloop()

#calls function from backend to establish connection
estConnection()

event = 1
main(event)
