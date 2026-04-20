'''
John Detloff
Module 1
Python Review
'''
from abc import ABC, abstractmethod

class shape(ABC):

    def __init__(self, color = 'red'):
        self.__color = color        

    def getType(self):
        pass

    def calcArea(self):
        pass

    def calcVolume(self):
        pass

    def setColor(new):
        self.__color = new

    def getColor(self):
        return self.__color

    def display(self):
        print("Shape Color: ", self.getColor())

class circle(shape):

    def __init__(self, radius = 1):
        self.__rad = radius

    def getType(self):
        return "Circle"

    def getRad(self):
        return self.__rad

    def setRad(self, new):
        self.__rad = new

    def calcArea(self):
        return (3.142 * self.getRad() * self.getRad())

    def calcVolume(self):
        pass
    
    def display(self):

        print("Geometry Type:", self.getType())
        print("Radius:", self.getRad())
        x = self.calcArea()
        print("Area: ", format(x, '.2f'))

class square(shape):

    def __init__(self, length = 2.3):
        self.__len = length

    def getLen(self):
        return self.__len

    def getType(self):
        return "Square"

    def setLen(self, new):
        self.__len = new

    def calcArea(self):
        return (self.getLen() * self.getLen())

    def calcVolume(self):
        pass

    def display(self):
        print("Geometry Type: " ,self.getType())
        print("Length: ", self.getLen())
        x = self.calcArea()
        print("Area: ", format(x, '.2f'))


class cube(shape):

    def __init__(self, length = 1, width = 1, height = 1):
        self.__len = length
        self.__wid = width
        self.__height = height

    def getType(self):
        return "Cube"

    
    def getLen(self):
        return self.__len

    def setLen(self, new):
        self.__len = new

    def getWidth(self):
        return self.__wid

    def setWidth(self, new):
        self.__wid = new

    def getHeight(self):
        return self.__height

    def setHeight(self, new):
        self.__height = new

    def calcArea(self):
        pass

    def calcVolume(self):
        return 2 * ((self.getWidth() * self.getHeight()) + (self.getHeight() * self.getLen()) + (self.getHeight() * self.getWidth()))

    def display(self):
        print("Geometry Type:", self.getType())
        print("Length: ", self.getLen())
        print("Width: ", self.getWidth())
        print("Height: ", self.getHeight())
        x = self.calcVolume()
        print("Area: ", format(x, '.2f'))

