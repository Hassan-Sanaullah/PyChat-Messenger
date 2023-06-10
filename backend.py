from client import Connect, Disconnect, communicate
import tkinter as tk

def estConnection():
    Connect()

def new(username, passwd):
    communicate(str(username))
    communicate(str(passwd))

def estDisconnect():
    Disconnect()