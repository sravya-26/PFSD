#51.Python Program to demonstrate class and object
"""class Employee:
    id=1539
    name="KLU"
    def display(e):
        print("Employee Id:",e.id,"Employee Name",e.name)
emp = Employee()#to create an object
emp.display()"""

#52.Python Program to demonstrate Class and Object using __init__method
"""class Employee:
    def __init__(e,id,name):
        e.id = id
        e.name = name
    def display(e):
        print("Employee Id:",e.id,"Employee Name",e.name)
emp = Employee(1539,"KLU")
emp.display()"""

#53.Python Program to demonstrate non parameterized constructor
"""class Employee:
    def __init__(e):
        print("Non Parameteraised Constructor")
emp=Employee()"""

#54.Python Program to demonstrate parameterized constructor
"""class Employee:
    def __init__(e,id,name):
        print("Parameteraised Constructor")
        print("Employee Id:",id,"Employee Name:",name)
emp=Employee(19,"Covid")"""
        
"""#55.Python Program to demonstrate single inheritance
class A:
    def view(a):
        print("Class A method")
class B(A):
    def display(b):
        print("Class B method")
obj1=A()
obj1.view()
obj2=B()
obj2.display()
obj2.view()"""

#56.Python Program to demonstrate multi level inheritance
"""class A:
    def display1(a):
        print("Class A method")
class B(A):
    def display2(b):
        print("Class B method")
class C(B):
    def display3(c):
        print("Class C method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj2.display1()
obj3.display2()
obj3.display1()"""


#57.Python Program to demonstrate multiple inheritance
"""class A:
    def display1(a):
        print("Class A method")
class B:
    def display2(b):
        print("Class B method")
class C(A,B):
    def display3(c):
        print("Class C method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj3.display2()
obj3.display1()"""

#58.Python Program to demonstrate heirarchal inheritance
"""class A:
    def display1(a):
        print("Class A method")
class B(A):
    def display2(b):
        print("Class B method")
class C(A):
    def display3(c):
        print("Class C method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj2.display1()
obj3.display1()"""

#59.Python Program to demonstrate hybrid inheritance
"""class A:
    def display1(a):
        print("Class A method")
class B(A):
    def display2(b):
        print("Class B method")
class C(B):
    def display3(c):
        print("Class C method")
class D(B,A):
    def display4(d):
        print("Class D method")
obj1=A()
obj2=B()
obj3=C()
obj4=D()
obj1.display1()
obj2.display2()
obj3.display3()
obj4.display4()
obj2.display1()
obj3.display2()
obj4.display1()
obj4.display2()
obj3.display1()"""

#60.Python Program to demonstrate Polymorphism(Method Overloading)
"""class Shape:
    def area(s,a=None,b=None):
        if a!=None and b!=None:
            print("Area",a*b)
        elif a!=None:
            print("Area",a*a)
        else:
            print("Area",0)
s=Shape()
s.area()
s.area(5)
s.area(5,10)"""

#61.Python Program to demonstrate Method Overriding
"""class A:
    def display(a):
        print("Class A Method")
class B(A):
    def display(b):
        print("Class B Method")     
obj1=A()
obj2=B()
obj1.display()
obj2.display()"""

#62.Python Program to count no of instances created
"""class Student:
    count=0
    def __init__(s,name,age):
        s.name=name
        s.age=age
        Student.count = Student.count + 1
    def display(s):
        print("Name: ",s.name,"Age:",s.age)
obj1=Student("KLU",40)
obj2=Student("KLEF",20)
obj3=Student("COVID",2)
print("Total No of Obj Created = ",Student.count)"""

#63.Python Program to demonstrate super() method
"""class College():
    def __init__(self,id,cname,location):
        self.id=id
        self.cname=cname
        self.location=location
class Department(College):
    def __init__(self,id,cname,location,dname):
        super().__init__(id,cname,location)
        self.dname=dname
cse = Department(1539,"KLU","VJA","CSE")
print(cse.id, cse.cname, cse.location, cse.dname)"""

#64.Python Program to demonstrate Exception Handling-1
"""try:
     a = int(input("Enter First Value: "))
     b = int(input("Enter Second Value: "))
     print(a/b)
except:
    print("divisible by zero exception")"""

#65.Python Program to demonstrate Exception Handling-2
"""try:
     l = [10,20,30]
     print(l[2])
except:
    print("Exception Occured")
else:
    print("No Exception raised")"""

#66.Python Program to demonstrate Exception Handling-3
"""try:
     #x='sravya'
     print(x)
except NameError:
    print("Variable is not defined")
else:
    print("No Exception raised")"""

#67.Python Program to demonstrate Exception Handling-4
"""try:
     l = [10,20,30,40,50]
     #print(l[2])
     print(l[5])
except IndexError:
    print("Index Bound of Exception")
else:
    print("No Exception raised")"""

#68.Python Program to demonstrate multiple Exception
"""try:
     l = [10,20,30,40,50]
     print(l[5])
except IndexError:
    print("Index Bound of Exception")
except ZeroDivisionError:
        print("divided by Zero Exception")
else:
    print("No Exception raised")"""

#69.Python Program to demonstrate finally keyword
"""try:
     l = [10,20,30,40,50]
     print(l[4])
except IndexError:
    print("Index Bound of Exception")
finally:
    print("End of Program")"""

#70.Python Program to demonstrate raise block
"""try:
     raise IndexError
except IndexError:
    print("Index Bound of Exception")
except ZeroDivisionError:
        print("divided by Zero Exception")
else:
    print("NO Exception")"""

#71.Python Program to demonstrate custom exception/ user defined exception
"""n = int(input("Enter Number: "))
if(n<0):
     raise Exception("Raised an Exception")
else:
    print("NO Exception Occured")"""



#----------------------------------------------------------
def find_area(base, height):
    return (0.5)*base*height
if __name__=='__main__':
    print("in 21_01_2021.py")
    a = find_area(5,6)
    print("Area: ",a)




