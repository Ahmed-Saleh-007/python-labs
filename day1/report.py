
#==================================================================================================#
#==================================================================================================#

#Python function enumerate()
#enumerate(iterable, start=0)
#How it works
#It takes the given input as a collection or tuples and returns it as an enumerate object. 
#The enumerate() method adds counter to an iterable and returns it (the enumerate object)
#You can convert enumerate objects to list and tuple using list() and tuple() method.

#example problem 6 again using enumerate

# def find_all_indexes(str, ch):
#     #make string as counter and value
#     for i, ltr in enumerate(str):
#         if ltr == ch:
#             #return answer then again contiue the excution
#             yield i


# print(list(find_all_indexes("Google",'o')))

#another example

# mylist = ['A', 'B' ,'C', 'D']
# e_list = enumerate(mylist)
# print(list(e_list))

# Output:
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]

#==================================================================================================#
#==================================================================================================#

#lambda functions in Python

#In Python, an anonymous function is a function that is defined without a name.
#While normal functions are defined using the def keyword in Python,
#anonymous functions are defined using the lambda keyword.
#Hence, anonymous functions are also called lambda functions.

#Syntax of Lambda Function in python
# lambda arguments: expression

#Examples of Lambda Function in python

#Program to filter out only the even items from a list

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# print(new_list)

# Program to double each item in a list using map()

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(map(lambda x: x * 2 , my_list))

# print(new_list)

#==================================================================================================#
#==================================================================================================#

#Operator module
#Purpose:	Functional interface to built-in operators.

# from operator import *

# print("Logical Operations")
# a = -1
# b = 5

# print ('a =', a)
# print ('b =', b)

# print ('not_(a)     :', not_(a))
# print ('truth(a)    :', truth(a))
# print ('is_(a, b)   :', is_(a,b))
# print ('is_not(a, b):', is_not(a,b))

# print("Comparison Operators")

# a = 1
# b = 5.0
# print

# print ('a =', a)
# print ('b =', b)
# for func in (lt, le, eq, ne, ge, gt):
#     print ('%s(a, b):' % func.__name__, func(a, b))

# print("Arithmetic Operators")
# a = -1
# b = 5.0
# c = 2
# d = 6

# print ('a =', a)
# print ('b =', b)
# print ('c =', c)
# print ('d =', d)

# print ('\nPositive/Negative:')
# print ('abs(a):', abs(a))
# print ('neg(a):', neg(a))
# print ('neg(b):', neg(b))
# print ('pos(a):', pos(a))
# print ('pos(b):', pos(b))

# print ('\nArithmetic:')
# print ('add(a, b)     :', add(a, b))
# print ('div(a, b)     :', floordiv(a, b))
# print ('div(d, c)     :', truediv(d, c))
# print ('floordiv(a, b):', floordiv(a, b))
# print ('floordiv(d, c):', floordiv(d, c))
# print ('mod(a, b)     :', mod(a, b))
# print ('mul(a, b)     :', mul(a, b))
# print ('pow(c, d)     :', pow(c, d))
# print ('sub(b, a)     :', sub(b, a))
# print ('truediv(a, b) :', truediv(a, b))
# print ('truediv(d, c) :', truediv(d, c))

# print ('\nBitwise:')
# print ('and_(c, d)  :', and_(c, d))
# print ('invert(c)   :', invert(c))
# print ('lshift(c, d):', lshift(c, d))
# print ('or_(c, d)   :', or_(c, d))
# print ('rshift(d, c):', rshift(d, c))
# print ('xor(c, d)   :', xor(c, d))

#==================================================================================================#
#==================================================================================================#
