# Notes:-
# Basic DataTypes are :- This Data types in Python are immutable by default because they can’t be changed in place, 
#                        but they can be copied and modified as needed.
# Integer --> All whole numbers
# FLoat --> Numbers with Decimal points
# String --> Alphanumerical Characters
# Boolen --> True/False
#    Note:- There are falsy Of boolen are {0,[],None,"",False} Data containing this are consider as FAlSE 
# Complex --> real & Imaginary (2+3j) 
# Type Conversion :- Changing of any data with one dataType to Other DataType Example shown below
 
print(type(123.45)) # This is Class 'float'
print(int(123.45)) # Type changing form float to integer
print(int("22")) # o/p --> 22
# print(int("ajdncn")) # Error, because value contain in string and cannot be changed
print(int(True))  # o/p --> 1 , Since in boolen True = 1 & False = 0
# print(int("10.30")) # o/p --> error, because it converts values with base-10 only


print(float(22)) # o/p --> 22.0
print(float("10.30")) # o/p --> 10.30
print(float(True))  #o/p --> 1.0

print(str(True))  # o/p --> 'True'
print(str(22))  # o/p --> '22'

print(bool(-22))  # o/p --> True
# Note:- There are falsy Of boolen are {0,[],None,"",False} Data containing this are consider as FAlSE 
print(bool(0))   # o/p --> False
print(bool([]))  # o/p --> False
a=22
print(bool(a))  # o/p --> True

print(complex(2)) # o/p --> 2+0j