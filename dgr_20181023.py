Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> str1='Hello'
>>> str2='there'
>>> bob=str1+str2
>>> print(bob)
Hellothere
>>> str3='123'
>>> str3=str3+1

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str3=str3+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x=int(str3)+1
>>> print(x)
124
>>> name=input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> name=input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> name=input('Enter:')
Enter: Chuck\

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1
    Chuck\
         ^
SyntaxError: unexpected character after line continuation character
>>> name=input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> apple=input('Enter:')
Enter:100
>>> x=apple-10
>>> apple=input('Enter:')
Enter:100
>>> x=apple-10
>>> x=int(apple)-10
>>> print(x)
90
>>> name=input('Enter:')
Enter:chuck

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'chuck' is not defined
>>> fruit='banana'
>>> letter=fruit[1]
>>> print(letter)
a
>>> fruit='banana'
>>> letter=fruit[3]
>>> print(letter)
a
>>> fruit='banana'
>>> letter=fruit[2]
>>> print(letter)
n
>>> fruit='štrawbery'
>>> letter=fruit[5]
>>> print(letter)
w
>>> zot='abc'
>>> print(zot[5])

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> fruit='banana'
>>> print(len(fruit))
6
>>> fruit='qwerty'
>>> print(len(fruit))
6
>>> fruit='štrawbery'
>>> print(len(fruit))
10
>>> fruit='banana'
>>> x=len(fruit)
>>> print(x)
6
>>> fruit='strawbery'
>>> x=len(fruit)
>>> print(x)
9
>>> fruit='banana'
>>> index=0
>>> while index<len(fruit):
	letter=fruit[index]
	print(index,letter)
	index=index+1

	
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> while index<len(strawbery):
	letter=fruit[index]
	print(index,letter)
	index=index+1

	

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    while index<len(strawbery):
NameError: name 'strawbery' is not defined
>>> while index<len(123):
	letter=number[index]
	print(index,letter)
	index=index+1

	

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    while index<len(123):
TypeError: object of type 'int' has no len()
>>> number='123'
>>> index=0
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')

Traceback (most recent call last):
  File "/home/user/rtr105/test_20181023_1_string.py", line 11, in <module>
    letter=fruit[index]
IndexError: string index out of range
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
(0, '\xc5')
(1, '\xa1')
(2, 't')
(3, 'r')
(4, 'a')
(5, 'w')
(6, 'b')
(7, 'e')
(8, 'r')
(9, 'y')
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
(0, '\xc5')
(1, '\xa1')
(2, 't')
(3, 'r')
(4, 'a')
(5, 'w')
(6, 'b')
(7, 'e')
(8, 'r')
(9, 'y')
(0, 's')
(1, 't')
(2, 'r')
(3, 'a')
(4, 'w')
(5, 'b')
(6, 'e')
(7, 'r')
(8, 'y')
>>> 
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
(0, '\xc5')
(1, '\xa1')
(2, 't')
(3, 'r')
(4, 'a')
(5, 'w')
(6, 'b')
(7, 'e')
(8, 'r')
(9, 'y')
(0, 's')
(1, 't')
(2, 'r')
(3, 'a')
(4, 'w')
(5, 'b')
(6, 'e')
(7, 'r')
(8, 'y')
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> 
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
(0, '\xc5')
(1, '\xa1')
(2, 't')
(3, 'r')
(4, 'a')
(5, 'w')
(6, 'b')
(7, 'e')
(8, 'r')
(9, 'y')
(0, 's')
(1, 't')
(2, 'r')
(3, 'a')
(4, 'w')
(5, 'b')
(6, 'e')
(7, 'r')
(8, 'y')
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 's')
(1, 't')
(2, 'r')
(3, 'a')
(4, 'w')
(5, 'b')
(6, 'e')
(7, 'r')
(8, 'y')
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> 
============ RESTART: /home/user/rtr105/test_20181023_1_string.py ============
(0, 's')
(1, 't')
(2, 'r')
(3, 'a')
(4, 'w')
(5, 'b')
(6, 'e')
(7, 'r')
(8, 'y')
>>> 


