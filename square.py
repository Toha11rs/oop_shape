from math import pi



class Circle():
    def __init__(self, radius):
        self.radius = radius

    def name(self):
        return self.__class__.__name__
    
    def square(self):
        """Функция нахождения площади круга"""
        return pi * self.radius**2 

class Triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def name(self):
        return self.__class__.__name__
    
    def square(self):
        """Функция нахождения площади треугольника"""
        semiperimeter = (self.side1 + self.side2 + self.side3)/2
        return (semiperimeter * (semiperimeter - self.side1) * (semiperimeter - self.side2) * (semiperimeter - self.side3))**0.5
    
    def right_triangle(self):
        """Функция нахождения прямоугольного треугольника"""
        if self.side3**2 == (self.side1 **2) + (self.side2**2):
            return True
        else:
            return False
        










