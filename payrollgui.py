# payrollgui.py

from tkinter import *
from payrolldata import PayrollData
from payrollemployee import Employee
class PayrollGUI:
    def __init__(self):
        self.data = PayrollData()
        self.employee = None
        self.root = Tk()
        self.root.title("Fluffshuffle Electronics")
        self.root.configure(background="gray")
        self.name = StringVar()
        self.address = StringVar()
        self.netPay = StringVar()
        self.buttonOpen = Button(self.root, text="Open", command=self.fileopen)
        self.buttonOpen.grid(row=0, column=0, padx=10, pady=10)
        Label(self.root, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.boxName = Entry(self.root, textvariable=self.name, width=25)
        self.boxName.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        Label(self.root, text="Address",).grid(row=2, column=0, padx=10, pady=10)
        self.boxAddress= Entry(self.root, textvariable=self.address, width=25)
        self.boxAddress.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        Label(self.root, text="Net Pay").grid(row=3, column=1, padx=10, pady=10)
        self.boxNetPay = Entry(self.root, textvariable=self.netPay)
        self.boxNetPay.grid(row=3, column=2, padx=10, pady=10)
        self.buttonPrevious = Button(self.root, text="Previous", command=self.dataprevious)
        self.buttonNext = Button(self.root, text="Next", command=self.datanext)
        self.buttonNext.grid(row=4, column=2, padx=10, pady=10)

    def fileopen(self):
        self.data.fileopen()
        self.setData()

    def setData(self):
        employee = self.data.getData()
        self.name.set(employee.getName())
        self.address.set(employee.getAddress())
        self.netPay.set(employee.calcNetPay())

    def dataprevious(self):
        self.data.dataprevious()
        self.setData()

    def datanext(self):
        self.data.datanext()
        self.setData()

def main():
    gui = PayrollGUI()
        

    
