# employee.py - Employee class

class Employee:
    def __init__(self,number,name,address,wage,hours):
        self.number = number
        self.name = name
        self.address = address
        self.wage = wage
        self.hours = hours

    def calcNetpay(self):
        if self.hours <= 40:
            straight = self.hours * self.wage
            overtime = 0.0
        else:
            straight = 40.0 * self.wage
            overtime = (self.hours - 40.0)* self.wage * 1.5
        tax = (straight + overtime) * (.20 + .075)
        return straight + overtime - tax

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address
