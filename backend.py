from client import Connect, Disconnect, communicate
import tkinter as tk

def estConnection():
    Connect()


def account(username, passwd, option):
    communicate(str(option))
    communicate(str(username))
    communicate(str(passwd))

def estDisconnect():
    Disconnect()