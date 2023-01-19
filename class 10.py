

#functional
#------------
def TV_fun(model,operation): 
    print("model is : ",model)
    print("operation is : ",operation)
def fridge_fun(model,operation):
    print("model is : ",model)
    print("operation is : ",operation)
TV_fun("samsung","vedio")
fridge_fun("LG","Cooling")
TV_fun("videocon","make ice")
fridge_fun("bpl","audiosong")

#OOPS
#-------

class tvFun:         # class is a blue_print to create object 
    def TV_FUN(self,model,operation):  # inside class statement we call func as method
        print("model is : ", model)
        print("operation is : ",operation)
class fridgeFun:
    def fridge_fun(self,model,operation):
        print("model is : ", model)
        print("operation is : ",operation)

t1=tvFun()    # create object 
t2=fridgeFun()

t1.TV_FUN("samsung","vidoesong") # calling method through object name
t2.fridge_fun("bpl","cooling")
#t1.fridge_fun("bpl","cooling") # this will give error "AttributeError: 'tvFun' object has no attribute 'fridge_fun'"
