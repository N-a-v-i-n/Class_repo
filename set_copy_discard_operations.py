a={1,2,343}
b={4,5646,767}
print(a)
c=a.copy() # copy() func
print(c)
removed_valu=a.pop()   # this will remove and store in variable
print(removed_valu)
print(a)
a.remove(2) 
#a.remove(100)  # this will remove paricular element from set
print(a)
ab={1,34,54,665,343,34}
ab.discard(100)
print(ab)
#operations
x=22
y=33
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x%y)
print(-5//2)
print([1,2,3]*2)
print(x==22) #relational operation --> this will always return bool result
# shorthand operators
total=0
total=total+100
print(total)
total+=100
print(total)
total*=2
print(total)
total/=100
print(total)
total%=100
print(total)
tupl=(1,2,3,4)
print(list(tupl))
x2={(1,2,3):[1,23,4],"name":[]}
for x in x2.items():
    print(x)
   
    x2["name"].append(10)
    print(x2)

import sys
import random
import timeit
t1="string"
t2={}
t3={12:12}
t4=[]
t5=(1,2,3,32,43,543,5,545,4645,4545)
t3[12]=100
print(t3)
print(sys.getsizeof(t1))
print(sys.getsizeof(t2))
print(sys.getsizeof(t3))
print(sys.getsizeof(t4))
print(sys.getsizeof(t5))



