l1=[1,2,3,4]
l2=[2,3,4,5]
print(l1 is l2)  # identity operator   'is' and 'is not'
print(3 in l1)  # membership operator  'in' and 'not in'
print(3 not in l1)
#if condition
a=10
b=100
if (b>a):
    print("b is bigger")
print("out of the if statement")
# if..... else condition
if (b<a):
    print("b is bigger")
else:
    print("b is bigger")
print("out of the if statement")
# if ...elif conditon

#
brand = input("enter your favourite brand : ")

if brand=="xy":
    print("it is childeren brand")
elif brand=="ab":
    print("it is women's brand")
elif brand=="pq":
    print("it is men's brand")

else:
    print("other brands are not available")

#for loop

l1=[1,2,4,5]
for x in l1:
    print(x**2)

l3=list(range(1,11))
print(l3)
temp=[]
for i in l1:
    temp.append(i**2)
print(temp)
