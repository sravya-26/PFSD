Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[10,20,30]
>>> l
[10, 20, 30]
>>> l[0]
10
>>> l1=[40,50,60]
>>> l1
[40, 50, 60]
>>> l.append(l1)
>>> l
[10, 20, 30, [40, 50, 60]]
>>> l.insert(4,70)
>>> l
[10, 20, 30, [40, 50, 60], 70]
>>> l.insert(5,[1,2])
>>> l
[10, 20, 30, [40, 50, 60], 70, [1, 2]]
>>> l1
[40, 50, 60]
>>> l1=l+l1
>>> l1
[10, 20, 30, [40, 50, 60], 70, [1, 2], 40, 50, 60]
>>> l2=[1,2,3,4]
>>> l
[10, 20, 30, [40, 50, 60], 70, [1, 2]]
>>> l1
[10, 20, 30, [40, 50, 60], 70, [1, 2], 40, 50, 60]
>>> l2
[1, 2, 3, 4]
>>> l2*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> l3=[8,9]
>>> l2.extend(l3)
>>> l2
[1, 2, 3, 4, 8, 9]
>>> l2.pop()
9
>>> l2.append(l)
>>> l2
[1, 2, 3, 4, 8, [10, 20, 30, [40, 50, 60], 70, [1, 2]]]
>>> l2.remove(l)
>>> l2
[1, 2, 3, 4, 8]
>>> l2.count(4)
1
>>> l
[10, 20, 30, [40, 50, 60], 70, [1, 2]]
>>> l2.append(4)
>>> l2.append([5,6])
>>> l2
[1, 2, 3, 4, 8, 4, [5, 6]]
>>> l2.count(4)
2
>>> l2.append(7)
>>> l2
[1, 2, 3, 4, 8, 4, [5, 6], 7]
>>> l2.index(3)
2
>>> l2.index(6)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l2.index(6)
ValueError: 6 is not in list
>>> l3
[8, 9]
>>> l3.extend({1,2,3,4,5])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> l3.extend([1,2,3,4,5])
>>> l3
[8, 9, 1, 2, 3, 4, 5]
>>> l3.sort()
>>> l3
[1, 2, 3, 4, 5, 8, 9]
>>> l3.reverse()
>>> l3
[9, 8, 5, 4, 3, 2, 1]
>>> l2
[1, 2, 3, 4, 8, 4, [5, 6], 7]
>>> l2.clear()
>>> l2
[]
>>> l3
[9, 8, 5, 4, 3, 2, 1]
>>> sum(l3)
32
>>> min(l3)
1
>>> max(l3)
9
>>> l
[10, 20, 30, [40, 50, 60], 70, [1, 2]]
>>> l1
[10, 20, 30, [40, 50, 60], 70, [1, 2], 40, 50, 60]
>>> l2
[]
>>> l3
[9, 8, 5, 4, 3, 2, 1]
>>> len(l3)
7
>>> list1=[]
>>> list2=[1,2,3]
>>> list1=list2.copy()
>>> list1
[1, 2, 3]
>>> l3
[9, 8, 5, 4, 3, 2, 1]
>>> del l3[2]
>>> l3
[9, 8, 4, 3, 2, 1]
>>> list1.extend({4,5,6])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> list1.extend([4,5,6])
>>> list1
[1, 2, 3, 4, 5, 6]
>>> list1[::]
[1, 2, 3, 4, 5, 6]
>>> list1[1:2]
[2]
>>> list1[1:4]
[2, 3, 4]
>>> list1[0:4]
[1, 2, 3, 4]
>>> list2=[1,2,5]
>>> list2
[1, 2, 5]
>>> list2[::]
[1, 2, 5]
>>> list2[0:3:1]
[1, 2, 5]
>>> list2[1:2:1]
[2]
>>> list2
[1, 2, 5]
>>> list2[0]
1
>>> list2[-3]
1
>>> list2[-2]
2
>>> list2[1]
2
>>> list2.extend([3,4])
>>> list2
[1, 2, 5, 3, 4]
>>> list2[1:2]
[2]
>>> list2[2:4]
[5, 3]
>>> list2[-1:]
[4]
>>> list2.extend([6,7])
>>> list2
[1, 2, 5, 3, 4, 6, 7]
>>> list2[:-1:2]
[1, 5, 4]
>>> list2[-5:-2]
[5, 3, 4]
>>> del list2[3]
>>> list2
[1, 2, 5, 4, 6, 7]
>>> del list2[0:2]
>>> list2
[5, 4, 6, 7]
>>> 
================================ RESTART: Shell ================================
>>> d={}
>>> d
{}
>>> d={'id':1539,'name':'sravya',1:101}
>>> d
{'id': 1539, 'name': 'sravya', 1: 101}
>>> type(d)
<class 'dict'>
>>> d.keys()
dict_keys(['id', 'name', 1])
>>> d.values()
dict_values([1539, 'sravya', 101])
>>> len(d)
3
>>> d.items()
dict_items([('id', 1539), ('name', 'sravya'), (1, 101)])
>>> d['id']
1539
>>> d['name']
'sravya'
>>> d[1]
101
>>> d.get('id')
1539
>>> d.get('name')
'sravya'
>>> d.get(1)
101
>>> d.get('loc')
>>> d['loc']
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    d['loc']
KeyError: 'loc'
>>> d1={}
>>> d1=d.copy()
>>> d1
{'id': 1539, 'name': 'sravya', 1: 101}
>>> d
{'id': 1539, 'name': 'sravya', 1: 101}
>>> d1.clear()
>>> d
{'id': 1539, 'name': 'sravya', 1: 101}
>>> d1
{}
>>> d.setdefault('gender')
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': None}
>>> d['gender']='female'
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': 'female'}
>>> d.update(loc='vja')
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': 'female', 'loc': 'vja'}
>>> d.update(102=1593;lang='telugu')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> d.update(lang='telugu')
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': 'female', 'loc': 'vja', 'lang': 'telugu'}
>>> d.update(dob='25/03/2002')
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': 'female', 'loc': 'vja', 'lang': 'telugu', 'dob': '25/03/2002'}
>>> d.update(branch='cse','c'=1593)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> d.update(branch='cse',c=1593)
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': 'female', 'loc': 'vja', 'lang': 'telugu', 'dob': '25/03/2002', 'branch': 'cse', 'c': 1593}
>>> d.update(prof='student',hobbies='music')
>>> d
{'id': 1539, 'name': 'sravya', 1: 101, 'gender': 'female', 'loc': 'vja', 'lang': 'telugu', 'dob': '25/03/2002', 'branch': 'cse', 'c': 1593, 'prof': 'student', 'hobbies': 'music'}
>>> d.update(1539=1697,one='abcd')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> d.update(1539==1697)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    d.update(1539==1697)
TypeError: 'bool' object is not iterable
>>> 
================================ RESTART: Shell ================================
>>> d={}
>>> d.update(a=101,b=102)
>>> d
{'a': 101, 'b': 102}
>>> d.setdefault('female')
>>> d
{'a': 101, 'b': 102, 'female': None}
>>> d['female']='gender'
>>> d
{'a': 101, 'b': 102, 'female': 'gender'}
>>> d.update([(4012,4013)])
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013}
>>> d.keys()
dict_keys(['a', 'b', 'female', 4012])
>>> d.values()
dict_values([101, 102, 'gender', 4013])
>>> d.update(loc='vja',dob='25/03/2002')
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013, 'loc': 'vja', 'dob': '25/03/2002'}
>>> d.pop(loc)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    d.pop(loc)
NameError: name 'loc' is not defined
>>> d.pop('loc')
'vja'
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013, 'dob': '25/03/2002'}
>>> del d['dob']
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013}
>>> d.pop('dept')
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    d.pop('dept')
KeyError: 'dept'
>>> del d['dept']
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    del d['dept']
KeyError: 'dept'
>>> keys={1,2,3,4,5}
>>> keys
{1, 2, 3, 4, 5}
>>> type(keys)
<class 'set'>
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013}
>>> d.update(x=101,y=102)
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013, 'x': 101, 'y': 102}
>>> d.update([(4654,100)])
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013, 'x': 101, 'y': 102, 4654: 100}
>>> d.update([(101,102),('loc','vja')])
>>> d
{'a': 101, 'b': 102, 'female': 'gender', 4012: 4013, 'x': 101, 'y': 102, 4654: 100, 101: 102, 'loc': 'vja'}
>>> 
================================ RESTART: Shell ================================
>>> t=(1,2,3)
>>> t1=()
>>> t
(1, 2, 3)
>>> t
(1, 2, 3)
>>> t1
()
>>> type(t)
<class 'tuple'>
>>> len(t)
3
>>> str(t)
'(1, 2, 3)'
>>> t1=(10,20,30,10)
>>> t1
(10, 20, 30, 10)
>>> t
(1, 2, 3)
>>> len(t1)
4
>>> t1.count(10)
2
>>> t1.index(10)
0
>>> t1.index(10)
0
>>> t1.index(20)
1
>>> t1*3
(10, 20, 30, 10, 10, 20, 30, 10, 10, 20, 30, 10)
>>> t1+t1
(10, 20, 30, 10, 10, 20, 30, 10)
>>> t2=t1+t1
>>> t2
(10, 20, 30, 10, 10, 20, 30, 10)
>>> t1
(10, 20, 30, 10)
>>> list(t1)
[10, 20, 30, 10]
>>> dict(t1)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    dict(t1)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> t1
(10, 20, 30, 10)
>>> sorted(t1)
[10, 10, 20, 30]
>>> set(t1)
{10, 20, 30}
>>> t1
(10, 20, 30, 10)
>>> t1[3]
10
>>> t1[-2]
30
>>> t1[1:2]
(20,)
>>> t1[1:3]
(20, 30)
>>> t1[1:4]
(20, 30, 10)
>>> t1[-1:0]
()
>>> t1[::-1]
(10, 30, 20, 10)
>>> t1
(10, 20, 30, 10)
>>> l=[1,2,3]
>>> l[::-1]
[3, 2, 1]
>>> sorted(t)
[1, 2, 3]
>>> sorted(t1)
[10, 10, 20, 30]
>>> t2
(10, 20, 30, 10, 10, 20, 30, 10)
>>> t1
(10, 20, 30, 10)
>>> t3=(50,51,53)
>>> t3[4]
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    t3[4]
IndexError: tuple index out of range
>>> t3[2]
53
>>> t3[2]="klu"
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    t3[2]="klu"
TypeError: 'tuple' object does not support item assignment
>>> t3
(50, 51, 53)
>>> sum(t3)
154
>>> min(t3)
50
>>> 
================================ RESTART: Shell ================================
>>> s={}
>>> s1={1,2,3,4,3}
>>> s1
{1, 2, 3, 4}
>>> len(s1)
4
>>> str(s1)
'{1, 2, 3, 4}'
>>> list(s1)
[1, 2, 3, 4]
>>> type(s1)
<class 'set'>
>>> s2={1,2,3}
>>> s1
{1, 2, 3, 4}
>>> s2
{1, 2, 3}
>>> s1.add(5)
>>> s1
{1, 2, 3, 4, 5}
>>> s
{}
>>> s.add({1,2})
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    s.add({1,2})
AttributeError: 'dict' object has no attribute 'add'
>>> s
{}
>>> s1
{1, 2, 3, 4, 5}
>>> s2
{1, 2, 3}
>>> len(s)
0
>>> len(s1)
5
>>> len(s2)
3
>>> s2.add(4)
>>> s2
{1, 2, 3, 4}
>>> s2.add(6)
>>> s2
{1, 2, 3, 4, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s1.intersection(s2)
{1, 2, 3, 4}
>>> s1.difference(s2)
{5}
>>> s2.difference(s1)
{6}
>>> s1.intersection_update(s2)
>>> s1
{1, 2, 3, 4}
>>> s2
{1, 2, 3, 4, 6}
>>> s2.intersection_update(s1)
>>> s2
{1, 2, 3, 4}
>>> s1
{1, 2, 3, 4}
>>> s1.difference_update(s2)
>>> s1
set()
>>> s2
{1, 2, 3, 4}
>>> s2.difference_update(s1)
>>> s2
{1, 2, 3, 4}
>>> s1
set()
>>> s2
{1, 2, 3, 4}
>>> s=set()
>>> s
set()
>>> s.add(10)
>>> s.add(20)
>>> s
{10, 20}
>>> s.add(30)
>>> s
{10, 20, 30}
>>> s1.add(1,12)
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    s1.add(1,12)
TypeError: set.add() takes exactly one argument (2 given)
>>> s1.add(1)
>>> s1.add(12)
>>> s1
{1, 12}
>>> s2
{1, 2, 3, 4}
>>> s2.add(23)
>>> s2.add(35)
>>> s
{10, 20, 30}
>>> s1
{1, 12}
>>> s2
{1, 2, 3, 4, 35, 23}
>>> s.remove(35)
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    s.remove(35)
KeyError: 35
>>> s.discard(35)
>>> s.discard(10)
>>> s
{20, 30}
>>> s.update({10,50})
>>> s
{50, 20, 10, 30}
>>> min(s)
10
>>> max(s)
50
>>> sum(s)
110
>>> a=set([1,2,3])
>>> type([1,2,3])
<class 'list'>
>>> type(a)
<class 'set'>
>>> s
{50, 20, 10, 30}
s
>>> 1
1
>>> s
{50, 20, 10, 30}
>>> s1
{1, 12}
>>> s2
{1, 2, 3, 4, 35, 23}
>>> s3
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    s3
NameError: name 's3' is not defined
>>> s1.isdisjoint(s2)
False
>>> s.update({1,12})
>>> s
{1, 50, 20, 10, 12, 30}
>>> s1
{1, 12}
>>> s2
{1, 2, 3, 4, 35, 23}
>>> s.isdisjoint(s1)
False
>>> s.pop()
1
>>> s
{50, 20, 10, 12, 30}
>>> s1.pop()
1
s
>>> 1
1
>>> s1
{12}
>>> s.symmetric_difference(s1)
{10, 50, 20, 30}
>>> 
================================ RESTART: Shell ================================
>>> #Functions with no args and no return val
>>> def add():
	a,b=10,20
	print(a+b)
     add()
     
SyntaxError: unindent does not match any outer indentation level
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
30
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
30
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
30
30
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
30
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
5
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
15
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
9
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
Traceback (most recent call last):
  File "D:/2 2/TS/Module 1/07_01_2021.py", line 37, in <module>
    sum(10,20,30,40,50)
TypeError: sum() takes 3 positional arguments but 5 were given
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
150
30
20
24
>>> 
================================ RESTART: Shell ================================
>>> #Functions with no args and no return val
def add():
	a,b=10,20
	print(a+b)
add()
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
enter a no:5
120
>>> 
=================== RESTART: D:/2 2/TS/Module 1/07_01_2021.py ==================
enter a no:5
5
>>> 