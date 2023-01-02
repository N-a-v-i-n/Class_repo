#Tuples :- This could be immutable, never uses insertion,clear,sort..etc, all types of date is accepted, indexing is possible, enclosed with () but not mandatory
ab=tuple()
abc=(1,2,3)
print(abc)

l2=(111)  # this will consider as class int 
print(l2)
print(type(l2))

l= 111,   # to create single value tuple we need to give value and comma
print(l)
print(type(l))


#packing
a=20
b=30
c=40
pack=a,b,c

print(pack)
7

#unpacking
x,y,z=pack    #doubt what if value in tuple is more and i given limited variable :_- this can be done by using logic and loops, first get length of packed varible, and create no of values using loops 
print(x,y,z )

#dictionary
#-------------------

d ={}
print(type(d))

d=dict()
print(type(d))

d3={"name":"naveen","age":25}
print(d3)

#to add values

d3["salary"]=2000
print(d3)
 # to access value we use key

print(d3["name"])

#how to update any value in dict
d3["name"]="kumnar"
print(d3)
# to access every value in dict using loops  -->
for key,value in d3.items() :
    print(key,value)
print(d3.items())
print(d3.keys())
print(d3.values())
print(len(d3))
#print(d3["address"])  --> trying to access whoes key is present error --keyerror
# if we dont want any keyerror we can use get() 
value = d3.get("age")
print(value)
print(d3.get("address"))
# or we can give default value instead of none
print(d3.get("address","no value"))

