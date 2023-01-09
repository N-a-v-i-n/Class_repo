#functions:-

# function declaration:
#----------------------------
# def function_name (arg1,arg2 OR *arg):
    #-----
    #-----
    #-----
    #return (var_name)    --> this will return the output once's function is called using variable ex:- a=function_name(par1,par2...)

# function calling:
#----------------------------
# functin_name (parameters1,parameter2..)

def wish():
    print("helle me !!")  

wish()
wish()
a=[]
print(type(a))
def wish(name,a):
    b=(f"helle {name}, {a} !!")
    a="navi"        # this will remains only with-in the function "local"
    return b


temp=wish("navii","haii")
print(temp)
print(a)


def add_sub(arg1,arg2):   # equal no of args ==equal no of parameters on function calling
    add=arg1+arg2
    sub=arg1-arg2
    return add,sub
add,sub=add_sub(30,20)
print(add,sub)

def add_sub(arg1,arg2):
    add=arg1+arg2
    sub=arg1-arg2
    return add,sub
add,sub=add_sub(30,20)
print(add,sub)
print(type(add))


#---------------------------------

def sum_fun(*arg):    # for unlimited no of arg's passing we can use *arg
    total=0
    for number in arg:
        total+=1
    print("The sum = ",total)
sum_fun()
sum_fun(1,2)
sum_fun(1,2,3)





