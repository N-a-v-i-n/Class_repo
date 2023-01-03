cn={"name":"naveen","age":25,"weight":105}
d=cn     # copy of cn is stored in "d"
cn.popitem()  # this will randomly delete any elemet from dictionary
print(cn)
d2=d.copy() # or we can use copy() func to store value 
print(d2)
del cn["name"]
#print(cn)
cn.pop("age")  #or we can do
#print(cn)


#setdefault(key,if key is not available then return default_value), also it will add the element only if that element not exist !!!
d3={1:23,2:45}
#v=d3.setdefault(1,111)
#print(v)
v=d3.setdefault(5,111)  # Element is not present in 'd3', so that element is added in that dictionry.
print(v)
print(d3) 
#update()  
d4={"name":"naveen"}
d3.update(d4)  # this will update d4 elements in d3
print(d3)

# set dataType:-
# enclosed with {}, heterogenious, mutable, indexing is not possible, insertion, ordering is not possible, duplicates are not allowed

s=set(range(0,11,2))   # s={0,2,4,6,8,10}
print(s)
s1=set([12,3,434,5435,1,1,12])
print(s1)
s2={12,3,434,5435,1,1}
print(s2)
#print(s2[4])  because indexing is ot possible 
s2.add(111)
print(s2)
#s2.add(list(range(3)))
print(s2)
t1=[1,2,3,5]
t2={1,2,4,6}
t3=(1,2,554,324,345)
t4=set()
t4.update(t1,t2,t3)  # this will return by skiping duplicates 
print(t4)
s3=set([1,2,3,54,656,3434,24,64,245,23,"s",1])
print(s3)

