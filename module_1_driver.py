'''
John Detloff
Module 1
Python Review
'''

from module1 import *
import random
import sys
import pickle
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

def main():

    x = int(input("Enter Number of Random Objects to Create: "))
    lst = []
    i = 0
    circleCount = 0
    squareCount = 0
    cubeCount = 0
    while i < x:
        ran = random.randint(1, 3)
        if ran == 1:
            n = circle()
            lst.append(n)
            circleCount += 1
        elif ran == 2:
            n = square()
            lst.append(n)
            squareCount += 1
        else:
            n = cube()
            lst.append(n)
            cubeCount += 1
        i += 1

    print()
    print("Results:")
    print("--------------")
    for i in lst:
        i.calcArea()
        i.display()
        print()

    results = [circleCount, squareCount, cubeCount]
    results_labels = ['# of Circle Objects', '#of Square Objects', '# of Cube Objects']
    plt.pie(results, labels = results_labels)
    plt.title("Results")
    plt.show()

    print()
    print("MENU:")
    print("____________________")
    print("1) Save Results into a File")
    print('2) Print Results')
    print('3) Display in GUI')
    print('4) Exit')
    print()

    choice = int(input("Enter Choice: "))
    while(choice < 1 or choice > 4):
        print("Error: Invalid Choice")
        choice = int(input("Enter Choice: "))

    if choice  == 1:
        name = str(input("Enter Name of File: "))
        file = open(name, "wb")
        pickle.dump(lst, file)
        file.close()
        print("File Saved")
        sys.exit()        
    elif choice == 2:
        for i in lst:
            i.display()
            print()
        sys.exit()
    elif choice == 3:
        gui(lst)
        sys.exit()
    else:
        sys.exit()



def gui(results):
    '''
    window = Tk()
    window.title("Final Project Results")
    window.geometry("500x800")

    for x in results:
        label = Label(window, text = str(x.getType()))
        label.pack()
        if x.getType() == 'Circle':
            label2 = Label(window, text = "Radius: " + str(x.getRad()))
            label2.pack()
        elif x.getType() == 'Square':
            label2 = Label(window, text = "Length: " + str(x.getLen()))
            label2.pack()
        else:
            label2 = Label(window, text = "Length: " + str(x.getLen()))
            label2.pack()
            label3 = Label(window, text = "Width: " + str(x.getWidth()))
            label3.pack()
            label4 = Label(window, text = "Height: " + str(x.getHeight()))
            label4.pack()
        area = Label(window, text = "Area: " + str(x.calcArea()))
        area.pack()
        space = Label(window, text = "___________")
        space.pack()
        '''
    new = []
    for x in results:
        new.append(str(x.getType()) + str(": "))
        if x.getType() == "Cube":
            new.append(str("Length: ") + str(x.getLen()))
            new.append(str("Width: ") + str(x.getWidth()))
            new.append(str("Height: ") + str(x.getHeight()))
            new.append(str("Volume: ") + str(format(x.calcVolume(), '.2f')) +str('\n'))
        elif x.getType() == "Square":
            new.append(str("Length: ") + str(x.getLen()))
            new.append(str("Area: ") + str(format(x.calcArea(), '.2f')) + str('\n'))
        else:
            new.append(str("Radius: ") +str(x.getRad()))
            new.append(str("Area: ") + str(format(x.calcArea(), '.2f')) + str('\n'))
            
    
    new = [str(x) for x in new]

    message = '\n'.join(new)
    messagebox.showinfo("Results", message)

        
main()
