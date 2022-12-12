#  OOPS CONCEPTS

class Employees:
    no_of_leaves = 8
    a = 5
    _b = 6
    __c= 7

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The employee name is {self.name}, salary is {self.salary} and the role is {self.role}"

    @classmethod
    def changeleaves(cls,newleave):                 # used to change the no_of_leave class variable
        cls.no_of_leaves = newleave

    @classmethod
    def from_slash(cls,strng):                      #  alternative for above constructer
        # param = strng.split('/')
        # print(param)
        # return cls(param[0],param[1],param[2])
        return cls(*strng.split('/'))

    @staticmethod
    def printgood(strr):
        print("This is good " + strr)

    def __add__(self, other):                           #dunder methods
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
       return f"The employee name is {self.name}, salary is {self.salary} and the role is {self.role}"

    def __str__(self):
        return f"The employee detail is : name:{self.name}, salary:{self.salary} , role:{self.role}"


bhoosh = Employees("Bhoosh",55000,"Instructor")
sam = Employees("Sam",25000,"Trainee")
param = Employees.from_slash("Param/80000/software")
print(param.printdetails())
print(param.role)
param.printgood("Param")
Employees.printgood("Sam")
print(sam.salary+bhoosh.salary)                  #try to comment out dunder method and check
print(sam.salary/bhoosh.salary)
print(bhoosh)                                    #repr method and str method comment out this method and see
# print(bhoosh.salary)
# print(bhoosh.no_of_leaves)
# print(sam.no_of_leaves)
# Employees.no_of_leaves = 50
# print(Employees.no_of_leaves)
#bhoosh.no_of_leaves = 15
#print(bhoosh.no_of_leaves)
# print(sam.printdetails())

# sam.changeleaves(25)
# print(bhoosh.no_of_leaves)
# print(sam.no_of_leaves)
print(sam.a)   #public
print(sam._b)   #protected
print(sam._Employees__c) #private  variable access

