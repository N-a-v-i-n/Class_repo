class Student: # class name, Pascal case
    def __init__(self): # constructor :- when ever we declar any fun_name = " __init__ " called as constructor, and through this fun calling is not required,
                        #   and to pass any parameter we can pass it through object ex: t1=class_name(parameters)
        self.name = "Vishnu Akash" # instance variable :- whenever we use self.variable_name, here we are creating instances of variable 
        self.age = 24
        self.mark = 99
        print("Inside: ", id(self)) # self :- which will store the address of current object, so that self address and object created address are same
    def talk(self): # object reference
        print(self.name)  # method2, as no args passed.. and while calling also no parameters are passed.. but here, we are using data of method1 through self concept.
        print(self.age)
        print(self.mark)

st1=Student()
st1.talk()
print("Outside: ",id(st1))

########################################
class Student: 
    def __init__(self,name,age,mark): # constructor
        self.name = name # instance variable
        self.age = age
        self.mark = mark
    def talk(self): # object reference
        print(self.name)
        print(self.age)
        print(self.mark)

st1=Student("Akash",24,100)  # Here, we are passing the parameters through object to constructor
st1.talk()
st2=Student("Vishnu", 25,95)
st2.talk()
######################################

class Employee:
    def __init__(self):
        self.eno=100
        self.ename="Vakash"
        self.esal=200000

e=Employee()
print(e.__dict__)  # we are converting data whatever inside the class, to dictionary format

################################
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t=Test()
t.m1()
print(t.__dict__)

#################################
class Student:
    school_name="SKV"   # Class variable :- whatever variable created inside the class but outside of all methods called and class level variable, which can be access to all inside class methods

    def __init__(self):
        self.a=100

    def display(self):
        a = 200
        print(self.a)
        print(a)

std1=Student()
std1.display()
print(std1.__dict__)
print(Student.__dict__)
print(std1.school_name)
