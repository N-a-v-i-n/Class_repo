#while loop
#while condition :
    #----
    #----
    #Increment operator
a1=0
while True:
    if a1>6:
        break    # this will break when a1>6 and come out of while loop
    a1+=1
    print(a1)


while True:
    if a1>6:
        continue    # this will skip when a1>6 and goes like infinate but never print
    a1+=1
    print(a1)


cart=[10,20,30,500,40]
for items in cart:
    if items>=500:
        print("we cannot process")
        break
    print(items)
else: print("complete processed")   # this else_statement will skip when the loop is break, or once loop is successfull without break_state then else part also get print

for i in range (2):
    for j in range(1):
        print("i=",i ,"j=",j)
def add_func():
    pass             # if function declared with out any conditions OR logics then it will give error, to avoid we use PASS 
print("done")


assert cart[1]<100, "error not match"   # for checking any senario which is present or correct, for not_present this will give assertion error and it will print error message "error not match"

a={"a":"2","b":"3"}

for x in a.items():
    b=x
    print(type(b))
    print(type(x))  #--> why this is converted from {"a":"2"}  to ("a","2") & shows class 'tuple'  :-  For all dictionary loop items are stored in tuples & keys, values are in str.  
    print(b)
