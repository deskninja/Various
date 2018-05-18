from tkinter import *
from tkinter import ttk
    

def main():
    root = Tk()
    tetra = Canvas(root, width = 100, height = 100)
    tetra.grid(row=1, column=1)

    hexa = Canvas(root, width = 100, height = 100)
    hexa.grid(row=1, column=2, padx=5, pady=5)

    octa = Canvas(root, width = 100, height = 100)
    octa.grid(row=1, column=3, padx=5, pady=5)
    
    dodeca = Canvas(root, width = 100, height = 100)
    dodeca.grid(row=2, column=2, padx=5, pady=5)

    icosa = Canvas(root, width = 100, height = 100)
    icosa.grid(row=2, column=3, padx=5, pady=5)
    
    tetra.create_polygon(20,10, 35,35, 10,90,  fill= "blue")
    tetra.create_polygon(20,10, 35,35, 90,60, fill= "lightyellow")
    tetra.create_polygon(10,90, 35,35, 90,60, fill= "magenta")

#The variables help with perspective shift
    z= 65,25
    y= 65,81
    hexa.create_polygon(10,20, z, y, 10,75, fill= "red")
    hexa.create_polygon(z, y, 90,65, 90,10, fill= "blue")
    hexa.create_polygon(10,20, z, 90,10, 35,5, fill= "yellow")


    octa.create_polygon(40,5, 10,55, 45,50, fill= "green")
    octa.create_polygon(10,55, 45,50, 60,90, fill= "blue")
    octa.create_polygon(60,90, 45,50, 90,35, fill= "yellow")
    octa.create_polygon(45,50, 40,5, 90,35, fill= "red")

#These variables isolate the middle pentagon for a perspective shift
    a= 13,43
    b= 47,15
    c= 80,37
    d= 70,78
    e= 24,81
    dodeca.create_polygon(a, b, c, d, e, fill= "yellow")
    dodeca.create_polygon(a, b, 50,5, 20,10, 5,35, fill= "blue")
    dodeca.create_polygon(c, b, 50,5, 80,10, 95,35, fill= "orange")
    dodeca.create_polygon(95,35, c, d, 80,90, 95,60, fill= "red")
    dodeca.create_polygon(5,35, a, e, 20,90, 5,60, fill= "green")
    dodeca.create_polygon(20,90, e, d, 80,90, 50,95, fill= "purple")

    icosa.create_polygon(5,40, 35,5, 10,45, fill="green")
    icosa.create_polygon(10,45, 70,40, 35,5, fill="blue")
    icosa.create_polygon(35,5, 70,40, 75,30, fill="red")
    icosa.create_polygon(5,40, 10,45, 8,75, fill="yellow")
    icosa.create_polygon(70,40,75,30, 78,70, fill="purple")
    icosa.create_polygon(43,80, 8,75, 10,45, fill="lightblue")
    icosa.create_polygon(43,80, 78,70, 70,40, fill="gold")
    icosa.create_polygon(10,45, 43,80, 70,40, fill="silver")
    icosa.create_polygon(8,75, 43,80, 45,85,fill="red")
    icosa.create_polygon(43,80, 78,70, 45,85, fill="brown")
    
main()

