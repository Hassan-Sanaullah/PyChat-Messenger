# from client import socketCall
# import tkinter as tk


# def new(username, passwd):
#     text = 'Account'
#     socketCall(str(username), True)
#     socketCall(str(passwd), True)
#     socketCall('exit', False)
    
#     print(username, passwd)

from gui import Connect, Disconnect, communicate
import tkinter as tk

def estConnection():
    Connect()

def new(username, passwd):
    communicate(str(username))
    communicate(str(passwd))

def estDisconnect():
    Disconnect()