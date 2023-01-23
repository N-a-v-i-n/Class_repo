class Test:
    def m1 (self):
        a=1000
        print(a)
    def m2 (self):
        b=2000
        print(b)
t=Test()
t.m1()
t.m2()

class Student:
    def __init__(self,a):
        self.a=a
    def disp(self):
        a=200  #Local variable
        print(self.a)
        print(a)
t2=Student(100)
t2.disp()

# class method

class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs ...!".format(name,cls.legs))
Animal.walk("DOG")
Animal.walk("CAT")


#Static method



class CustomMethod:
    @staticmethod
    def add(x,y):
        print("addtion of x and y is : ",x+y)
    @staticmethod
    def sub (x,y):
        print("sub of x & Y is : ",x-y)

CustomMethod.add(20,30)
CustomMethod.sub(30,20)

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        print (other)
        return self.pages + other.pages
   
b1=Book(100)
b2=Book(200)
b3 = b1+b2
print(b3)
