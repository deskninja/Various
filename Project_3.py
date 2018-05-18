#Farmer John's feild
#by Joshua Wells

from tkinter import *
from tkinter import ttk


def square():
    root= Tk()
    radius = int(input("what is the radius of the square? "))

    length = radius * 2 + 10

    win = Canvas(root, width = 400, height = 400)
    win.grid()
    win.create_oval(10,10, length,length, fill= "blue")
    win.create_oval(10,length, low,low, fill="blue")


def main():
    square()
main()
