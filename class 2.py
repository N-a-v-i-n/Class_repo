import keyword
print(keyword.kwlist)   # This will return, the list of all pre-defind keyword in python 
print(len(keyword.kwlist)) # Return length of keywords

# Non-Primitive dataType
# ------------------------
# 1. list:-
#----------
# 1. List always enclosed with square_brackets []
# 2. It can accept heterogeniuos values like int,string,boolen,float,list,tuple,set,dict etc...
# 3. List can mutable, i.e we can change any values which are done by using indexes
# 4. Removal,Insertion of data is possible
# 5. syntax :- a=[1,2,3,'a',"string",True]

l=list()
print(l)  # O/p :- []
print(type(l))  # O/p :- class 'list'
a=[] 
print(a) # O/p :- []

b=[1,2,3,'a','b','c',"bengaluru",True]   
print(b)   # O/p :- [1,2,3,'a','b','c',"bengaluru",True]
print(b[4])  # O/p :- b
for x in b: 
    print(x)    # O/p :- 
                #   1
                #   2
                #   3
                #   a
                #   b
                #   c
                #   bengaluru
                #   True
a1=list(range(1,11))     
print(a1)       # O/p :- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2=(list(range(0,11,2)))
print(l2)       # O/p :- [0, 2, 4, 6, 8, 10]

l2.clear()
print(l2)       # O/p :- []
del(l2)
#print(l2)

del(b)
#print(b)

l=[1,2,3,4]
print(l)
l.append(10)  # this will add additional data to the existing list
print(l)
#l.insert(1,22)
print(l)

b=[1,2,3,'a','b','c',"bengaluru",True]
l.extend(b)
print(l)      # O/p :- [1, 2, 3, 4, 10, 1, 2, 3, 'a', 'b', 'c', 'bengaluru', True]

l.remove("bengaluru")  # O/p :- [1, 2, 3, 4, 10, 1, 2, 3, 'a', 'b', 'c', True]
print(l)

l.pop()        
print(l)         # By default it will remove from end O/p :- [1, 2, 3, 4, 10, 1, 2, 3, 'a', 'b', 'c', True]
temp = [1,34,3,9]

b=temp.reverse()   #-->  doubt
print(b)






