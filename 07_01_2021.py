#35:Functions with no args and no return val
"""def add():
	a,b=10,20
	print(a+b)
add()"""
#36:Functions with no args and return val
"""def add():
    a,b=10,20
    return a+b
print(add())"""
#37:Functions with args and no return val
"""def add(x,y):
    return x+y
print(add(10,20))"""
#38:Functions with args and return val
"""def add(x,y):
    return x+y
a=10;b=20
print(add(10,b))"""
#39:reuired arguments
"""def add(x,y):
    print(x+y)
a=2;b=3
add(a,b)#actual arg/parameters"""
#40:keyword args
"""def add(a,b):
    print(a+b)
#add(a=2,b=5)
add(b=7,a=8)"""
#41:default args
"""def add(a,b=3):
    print(a+b)
add(3,6)"""
#42:variable length
"""def sum(*x):
    total=0
    for n in x:
        total=total+n
    print(total)
sum(10,20,30,40,50)
sum(10,20)
sum(20)
sum(1,23)"""
#43:Recursive function
"""def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
n=int(input("enter a no:"))
print(fact(n))"""
#44:fibonacci
"""def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
x=int(input("enter a no:"))
print(fib(x))"""
#0 1 1 2 3 5 8 13 21 34
#45:
