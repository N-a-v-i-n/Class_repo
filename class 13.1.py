
#super()Method:- this method is used for accessing other class method, constructors in current class 
class Persons:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("Name : ", self.name)
        print("Ages : ", self.age)
    def display(self1):
        print("Name : ", self1.name)
        print("Age : ", self1.age)
    def display1(self1):
        print("Names : ", self1.name)
        print("Ages : ", self1.age)

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name : ", self.name)
        print("Ages : ", self.age)
    def display(self1):
        print("Name : ", self1.name)
        print("Age : ", self1.age)
    def display(self1):
        print("Names : ", self1.name)
        print("Age : ", self1.age)
class Student(Person,Persons): #method resolution order
    def __init__(self,name,age,rollno,marks):
        super().__init__()
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display1()
        print("Roll NO : ", self.rollno)
        print("Marks : ", self.marks)
c1=Student("NAvii",25,66,67)
c1.display()
