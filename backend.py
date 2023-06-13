from client import Connect, Disconnect, communicate
import tkinter as tk

def estConnection():
    Connect()


def account(username, passwd, option):

    message = "-".join([str(option), str(username), str(passwd)])
    communicate(str(message))
    # communicate(str(username))
    # communicate(str(passwd))

def estDisconnect():
    Disconnect()