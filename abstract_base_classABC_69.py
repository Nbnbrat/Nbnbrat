from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0

class rectangle(Shape):
    type = 'Rectangle'
    sides = 4
    def __init__(self):
        self.length = 4
        self.breadth = 5

    def area(self):                                                  #when we create a abstract base class then it is mandatory
        return self.length * self.breadth                             #to use its instance method in child class comment out
                                                                       # this child class method and see

rect1 = rectangle()                                                      #and we can't create object for ABC class
print(rect1.area())
