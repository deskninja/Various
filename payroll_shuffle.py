#Joshua Wells
#Payroll_Shuffle
#April 19, 2018
#CS 1400
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile
from os import path

class Employee:
    MINIMUM_WAGE = 7
    AVERAGE_TAX = .2
    DEFAULT_HOURS = 40
    
    def __init__(self, number = "-1", name = "", address = "", tax = AVERAGE_TAX, wage = MINIMUM_WAGE, hours = DEFAULT_HOURS):
        self.number = number
        self.name = name
        self.address = address
        self.tax = float(tax)
        self.wage = float(wage)
        self.hours = float(hours)
        print(self.number)

    def calcNetPay(self):
        if self.hours <= 40:
            straight = self.hours * self.wage
            overtime = 0.0
        else:
            straight = 40.0 * self.wage
            overtime = (self.hours - 40.0)* self.wage * 1.5
        tax = (straight + overtime) * (self.tax)
        return straight + overtime - tax

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getWage(self):
        return self.wage

    def getHours(self):
        return self.hours

    def getTax(self):
        return self.tax
    
    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setWage(self, wage):
        self.wage = float(wage)

    def setHours(self, hours):
        self.hours = float(hours)

    def setTax(self, tax):
        self.tax = float(tax)
    
    def __str__(self):
        # Write the Employee as a record for storage in a file.
        return "\n".join([str(f).rstrip() for f in [self.number, self.name, self.address, self.tax, str(self.wage) + " " + str(self.hours)]]) + "\n"


class PayrollData:
    def __init__(self):
        self.reset()

    def reset(self):
        # Get the users home directory.
        self.filePath = path.expanduser("~/")
        self.employees = []

    def fileOpen(self):
        # Reset data since we are opening a new file.
        self.reset()
        self.filePath = askopenfilename()

        fileLines = open(self.filePath, "r").readlines()
        linesPerRecord = 5
        columnData = [[l.rstrip() for l in fileLines[i::linesPerRecord]] for i in range(linesPerRecord)]
        records = zip(*columnData)
        for number, name, address, tax, timesheet in records:
            wage, hours = [x for x in timesheet.split(" ")]
            self.addEmployee(Employee(number, name, address, tax, wage, hours))

    def fileSave(self):
        with asksaveasfile(mode='w', initialfile=path.basename(self.filePath), initialdir=path.dirname(self.filePath), defaultextension='.txt') as file:
            if file is None:
                return
            file.writelines([str(e) for e in self.employees])
            self.filePath = file.name

    def addEmployee(self, employee=None):
        employee = employee or Employee(len(self.employees) + 1)
        self.employees.append(employee)


class PayrollGUI:
    def __init__(self):
        self.data = PayrollData()
        self.data.addEmployee()
        self.employee = self.data.employees[0]
        self.root = Tk()
        self.root.title("Fluffshuffle Electronics")
        self.root.configure(background="gray")
        self.name = StringVar()
        self.address = StringVar()
        self.wage = StringVar()
        self.hours = StringVar()
        self.netPay = StringVar()
        self.tax = StringVar()
        
        Label(self.root, text="Name").grid(row=1, column=0, padx=10, pady=10)
        self.boxName = Entry(self.root, textvariable=self.name, width=25)
        self.boxName.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        Label(self.root, text="Address",).grid(row=2, column=0, padx=10, pady=10)
        self.boxAddress = Entry(self.root, textvariable=self.address, width=25)
        self.boxAddress.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        Label(self.root, text="Wage").grid(row=3, column=0)
        self.boxWage = Entry(self.root, textvariable=self.wage, width=5)
        self.boxWage.grid(row=3, column=1, padx=10, pady=10)
        Label(self.root, text="Hours").grid(row=3, column=2)
        self.boxHours = Entry(self.root, textvariable=self.hours, width=5)
        self.boxHours.grid(row=3, column=3, padx=10, pady=10)
        Label(self.root, text="Tax Rate").grid(row=4, column=0)
        self.boxTaxRate = Entry(self.root, textvariable=self.tax, width=5)
        self.boxTaxRate.grid(row=4, column=1, padx=10, pady=10)
        Label(self.root, text="Net Pay").grid(row=5, column=1, padx=10, pady=10)
        self.boxNetPay = Entry(self.root, textvariable=self.netPay)
        self.boxNetPay.grid(row=5, column=2, padx=10, pady=10)
        
        self.buttonOpen = Button(self.root, text="Open", command=self.fileOpen)
        self.buttonOpen.grid(row=0, column=0, padx=10, pady=10)
        self.buttonPrevious = Button(self.root, text="Previous", command=self.dataPrevious)
        self.buttonPrevious.grid(row=6, column=1, padx=10, pady=10)
        self.buttonNext = Button(self.root, text="Next", command=self.dataNext)
        self.buttonNext.grid(row=6, column=2, padx=10, pady=10)
        self.addEmployee = Button(self.root, text="Add Employee", command=self.addEmployee)
        self.addEmployee.grid(row=0, column=1, padx=10, pady=10)
        self.saveNew = Button(self.root, text="Save", command=self.fileSave)
        self.saveNew.grid(row=0, column=2, padx=10, pady=10)

    def fileOpen(self):
        self.data.fileOpen()
        self.employee = self.data.employees[0]
        self.readData()

    def fileSave(self):
        self.writeData()
        self.data.fileSave()

    def dataPrevious(self):
        self.writeData()
        self.employee = self.data.employees[(self.data.employees.index(self.employee) - 1) % len(self.data.employees)]
        self.readData()

    def dataNext(self):
        self.writeData()
        self.employee = self.data.employees[(self.data.employees.index(self.employee) + 1) % len(self.data.employees)]
        self.readData()

    def addEmployee(self):
        self.data.addEmployee()
        self.employee = self.data.employees[-1]
        self.readData()

    def readData(self):
        e = self.employee
        self.name.set(e.getName())
        self.address.set(e.getAddress())
        self.wage.set(e.getWage())
        self.hours.set(e.getHours())
        self.netPay.set(e.calcNetPay())
        self.tax.set(e.getTax())

    def writeData(self):
        e = self.employee
        e.setName(self.name.get())
        e.setAddress(self.address.get())
        e.setWage(self.wage.get())
        e.setHours(self.hours.get())
        e.setTax(self.tax.get())
        # TODO: Maybe not needed?
        self.data.employees[self.data.employees.index(self.employee)] = e

        
def main():
    gui = PayrollGUI()

if __name__ == '__main__':
    main()
