#Farmer John's feild
#by Joshua Wells
#Course CS 1400
#Due February 17, 2018
#I was helped by my teacher in class and his example code
#Note that I recognize resising the graphic serves no purpose to the user, but it was simply an exercise for me.
#Note the windowSize function does not preform its desired funtion in some instances
#Note a Bare Bones version will be included at the bottom in triple quotes because this first example does not work
#   with all input values
"""from math import *
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    user_input = float(getInput())
    unit = unitofMeasure()
    size = round(user_input * 3)
    length = windowSize(size)
    feild = Canvas(root, width = length, height = size * 1.25)
    feild.grid()
    visual(feild, user_input)
    if user_input != None:
        answer(feild, user_input, unit)
        
        
#functions to form the visual
def visual(feild, user_input):
    cent = round(user_input * 1.5)
    center = cent, cent
    ui = user_input / 2
    rectangle(feild, center, ui)
    circles(feild, center, user_input)
    lines(feild, center, ui)\

#this was supposed to make it so that you could always read the answer text reguardless of the size of the window
def windowSize(size):
    length = size
    if length < 200:
        length = 200
        return length
    else:
        return length
    
def rectangle(feild, center, ui):
    feild.create_rectangle((center[0] - ui,center[1] - ui), (center[0] + ui,center[1] + ui), fill="grey")

def circles(feild, center, user_input):
    mid = center[0]
    topRight = mid + user_input, mid - user_input
    topLeft = mid - user_input, mid + user_input
    bottomRight = mid + user_input, mid + user_input
    bottomLeft = mid - user_input, mid - user_input
    
    circle(feild, topRight, center)
    circle(feild, bottomRight, center)
    circle(feild, center, bottomLeft)
    circle(feild, center, topLeft)
    
def circle(feild, a, b):
    feild.create_oval(a, b, fill="white")

def lines(feild, center, ui):
    mid = center[0]
    topRight = mid + ui, mid - ui
    topLeft = mid - ui, mid - ui
    bottomRight = mid + ui, mid + ui
    bottomLeft = mid - ui, mid + ui

    line(feild, topRight, topLeft)
    line(feild, topLeft, bottomLeft)
    line(feild, bottomLeft, bottomRight)
    line(feild, bottomRight, topRight)

def line(feild, a, b):
    feild.create_line(a, b)
    
#function to handle input
def getInput():
    user_input = input("What is the length of one side of the square? The value should be under 300: ")
    try:
        return float(user_input)
    except ValueError:
        print("The value ", user_input, " was not a valid entry")
        main()

def unitofMeasure():
    unit = input("What is your unit of measure? ")
    if unit != None:
        try:
            return str(unit)
        except:
            print("something went wrong with your unit of measure!")
    else:
        print("Please enter a value for your unit of measure.")
    
#function to find the answer
def calcArea(user_input):
    squareArea = user_input * user_input
    circleArea = pi * (user_input / 2) ** 2
    area = squareArea - circleArea
    return area

#function to print the answer
def answer(feild, user_input, unit):
    center = user_input * 1.5
    area = calcArea(user_input)
    areaAnswer = "    The area is {:0.2f} square ".format(area)
    unitAnswer = areaAnswer + unit
    feild.create_text(center, center * 2, text = unitAnswer)
main()

"""
from math import *
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    user_input = getInput()
    unit = unitofMeasure()
    feild = Canvas(root, width = 400, height = 300)
    feild.grid()
    visual(feild)
    if user_input != None:
        answer(feild, user_input, unit)
        
        
#functions to form the visual
def visual(feild):
    center = 150, 150
    user_input = 50
    ui = 25
    rectangle(feild, center, ui)
    circles(feild, center, user_input)
    lines(feild, center, ui)
    
def rectangle(feild, center, ui):
    feild.create_rectangle((center[0] - ui, center[1] - ui), (center[0] + ui,center[1] + ui), fill="grey")

def circles(feild, center, user_input):
    mid = center[0]
    topRight = mid + user_input, mid - user_input
    topLeft = mid - user_input, mid + user_input
    bottomRight = mid + user_input, mid + user_input
    bottomLeft = mid - user_input, mid - user_input
    
    circle(feild, topRight, center)
    circle(feild, bottomRight, center)
    circle(feild, center, bottomLeft)
    circle(feild, center, topLeft)
    
    
def circle(feild, a, b):
    feild.create_oval(a, b, fill="white")

def lines(feild, center, ui):
    mid = center[0]
    topRight = mid + ui, mid - ui
    topLeft = mid - ui, mid - ui
    bottomRight = mid + ui, mid + ui
    bottomLeft = mid - ui, mid + ui

    line(feild, topRight, topLeft)
    line(feild, topLeft, bottomLeft)
    line(feild, bottomLeft, bottomRight)
    line(feild, bottomRight, topRight)

def line(feild, a, b):
    feild.create_line(a, b)
    
#function to handle input
def getInput():
    user_input = input("What is the length of one side of the square? ")
    try:
        return float(user_input)
    except ValueError:
        print("The value ", user_input, " was not a valid entry")
        sys.exit()

def unitofMeasure():
    unit = input("What is your unit of measure? ")
    try:
        return str(unit)
    except ValueError:
        print("Your entry of ", unit," was invalid.")
        sys.exit()
    
#function to find the answer
def calcArea(user_input):
    squareArea = user_input * user_input
    circleArea = pi * (user_input / 2) ** 2
    area = squareArea - circleArea
    return area

#function to print the answer
def answer(feild, user_input, unit):
    ptA = 125
    area = calcArea(user_input)
    areaAnswer = "    The area is {:0.2f} square ".format(area)
    unitAnswer = areaAnswer + unit
    feild.create_text(150 , ptA * 2, text = unitAnswer, font = "16")
main()

