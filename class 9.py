#map() :- this mwthod is used to call each element form the list and gives to function.
#map() is an higher order function, which means function with calling other func
#Note map() menthod contains two args.. 1. function  2. sequence ..
#type 1.
i=[1,2,3,4,5]
def double_it(x):
    return 2*x
i1=list(map(double_it,i))
print(i1)

# type 2.
i2=list(map(lambda a:a*2,range(6)))
print(i2)


#reduce() :- to use reduce method we need to import it from functools
# this method is used to convert larger/no of elements into single element.. but homogenious only
from functools import reduce
a1=[12,20,11,33]
result=reduce(lambda x,y:y+x,a1)   #While using reduce we should use two args in lambda
print(result)

def fun_print():   
    print("hello")
print(fun_print)   # here we are printing the address of function
print(id(fun_print)) 
print(type(fun_print)) # class function

def print_function():
    '''hello this is nothing'''
    print("this is simple print")
print("using __doc__ : ")
print(print_function.__doc__)
print("using help")
help(print_function)

#modules :- collections of functions, classes.
# to use any module we use "import module_name"
#import random
#--------------------
#n=random.randint(0,100)
#print(n)
#from random import randint
#from random import *
import random as navii
m=navii.randint(0,100)
print(m)


#practice work
#-------------------------
f1=[234,45,45,56,67]
f2=[22,223,442,323]
f3=[]
f3.append(reduce(lambda x,y:x+y,f1))
f3.append(reduce(lambda x,y:x+y,f2))
print(f3)



#practice work (reduce())
#------------------------------
p1={2,5,8,0}      #here set is used so sequence will be {8025}, because set takes random
print(p1)
p2=reduce(lambda x,y:(x+y)*2,p1)   #--> o/p 82   
print(p2)

p3=[2,5,8,0]      #here list is used so sequence will be [2580]
print(p3)
p4=reduce(lambda x,y:(x+y)*2,p3)   #--> o/p 88
print(p3)

p5=["a","b"]
p6=reduce(lambda x,y:(x+y)*2,p5)   #--> o/p abab
print(p6)

p11=(0,8,1,2)
p12=reduce(lambda x,y:(x+y)*2,p11)   #--> o/p abab
print(p12)

p7=["a",0,1,3,4]
p8=reduce(lambda x,y:(x+y)*2,p7 )   #--> TypeError: can only concatenate str (not "int") to str, because homogenious is accepted
print(p8)
