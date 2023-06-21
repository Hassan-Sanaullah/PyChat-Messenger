from client import Connect, Disconnect, communicate
import tkinter as tk

def estConnection():
    Connect()


def account(username, passwd, option):

    message = "-".join([str(option), str(username), str(passwd)])
    
    return communicate(str(message))

def get_inbox(option, username):
    message = "-".join([option, username])

    return communicate(str(message))


def get_message(option, username, selected_message):

    message = "-".join([str(option), str(username), str(selected_message)])
    
    return communicate(str(message))

def estDisconnect():
    Disconnect()