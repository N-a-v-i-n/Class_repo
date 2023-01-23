#exception handling
#-------------------------

try:
    print("hello")
    print(10/0)
    print("haii")
except ZeroDivisionError:
    print(10/2)

    
try :
    x=int(input("Enter First Number : "))
    y=int(input("Enter Second Number : "))
    print(x/y)
except ZeroDivisionError:
    print("Cant Divide with ZEro")
#except ValueError:
#    print("please provide int value only")
except:
    print("server crash")

#finally block: - For Handling error, we can go with try-except block
try :  #Risky codes can be entered inside try block
    print("try")
except: # Handling code can be return inside except block
    print("except")
finally: # this finally block will always execute after try-except block done
    print("finally")
#else block with try-except
#-------------------------------
try : 
    print("try")
    print(10/0)
except:
    print("except")
else: # Else block will execute whenever try block get executed, on execute of except block, this else will not ge execute
    print("else")
finally:
    print("finally")
#raise :- this is use to create user_defined errors
# raise Exception(“user text”)
#------------------------------------------------------
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
        #print("self.msg")
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg
        #print("self.msg")
age=int(input("age : "))
if age<18:
    raise TooYoungException("Not Eligible")
elif age>18 :
    raise TooOldException("Eligible")
else:
    print("you will get email !!")


    
        
