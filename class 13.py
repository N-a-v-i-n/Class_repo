class B:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print("Becant instance_method")
    @classmethod
    def m2(cls):
        print("Besant class_method")
    @staticmethod
    def m3():
        print("Besant static_method")
class C(B):
    pass

c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()


#single inheritance

class D:
    def m1(self):
        print("Besant Method")
class E(D):
    def m2(self):
        print("Child_class")
    def m1(self):
        print("first it will check m1_method is inside the child class, if exist then it will proceed, else it will check on parent class")
c1=E()
c1.m1()
c1.m2()

#Multi_Level_inheritance

class D1:
    def m1(self):
        print("Besant Method")
class E1(D1):
    def m2(self):
        print("Child_class")
    def m3(self):
        print("first it will check m1_method is inside the child class, if exist then it will proceed, else it will check on parent class")
class F1(E1):
    def m4(self):
        print("GOT it ")

c1=F1()
c1.m1()
c1.m2()
c1.m3()
c1.m4()

#hierarchical
class P:
    def m1(self):
        print("Besant_Method")
class C1(P):
    def m2(self):
        print("Child_Method")
class C2(P):
    def m3(self):
        print("Child_Method")

t=c1()
t.m1()
t.m2()
t1=c2()
t1.m1()
t1.m3()
#t1.m2()

#Multi parent one child hierarchical

class P:
    def m1(self):
        print("Besant_Method")
class C1:
    def m2(self):
        print("Child_Method")
class C2(C1,P):
    def m3(self):
        print("Child_Method")

q=c2()
q.m1()
q.m2()
q.m3()












  
