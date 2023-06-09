from client import socketCall
import tkinter as tk


def new(username, passwd):
    text = 'Account'
    socketCall(str(username), True)
    socketCall(str(passwd), True)
    socketCall('exit', False)
    
    print(username, passwd)
