#!/usr/bin/env python3
#

# x = '4'
# print(type(x))
# x = 4
# print(type(x))
# x = 5.0
# print(type(x))
# x = 2j
# print(type(x))


# twice line
# input('\n\n Press the enter key to exist')

# diff type
# counter = 100
# miles = 100.0
# name = 'iti'
# print(type(counter))
# print(type(miles))
# print(type(name))

'''
variables
'''
# multi assign
# a=b=c=1
# a,b,c = 'ahmed', 'iti', 41

# x = 'ITI'
# print('welcome ' + x)
# #
# y = ' 41'
#
# z = x + y
# #
# print(z)
#
#
# x = 5
# y = 10
# print(x+y)
#
# # make error
# x = 5
# y = "python"
# print(x+y)

# x = 5
# print(x)
# del x
# print(x)

# Numbers
# x = 1
# y = 2.8
# z = 1j
# print(type(x))
# print(type(y))
# print(type(z))

# casting numbers

# x = int(1)
# y = int(2.8)
# z = int("3")

# # float
# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)
#
# # casting string
# x = str("s1")
# y = str(2)
# z = str(3.0)
# print(type(x))
# print(type(y))
# print(type(z))
# some built-in method

# print(pow(2, 2))
# print(abs(-1))
# print(max(3, 2))
# print(min(3, 2))
# print(round(3.2))
# print(round(3.5))

# string
# welcome = "Welcome Python Course"
# print(welcome)
# print(welcome[0])
# print(welcome[1:5])

# updating strings

# print(welcome[:15] + 'python')


# special operators in string

# x = '***ITI***'
# print(x*3)
#
# print('a' in 'ahmed')
# print('a' not in 'ahmed')
# print('a' is 'a')
# print('a' == 'a')
# print(str(4))

# string formatting (embded string)
#%s -> string, %d -> integer

# print('My name is %s and age is %d years old' % ('Ahmed', 32))
# print('My name is {0} and age is {1} years old'.format('Ahmed', 32))
# name = 'Ahmed'
# age=32
# print(f'My name is {name} and age is {age} years old')
#https://realpython.com/python-f-strings/

# docs = """Hello ITI
# this test doc string
# """
# print(docs)

#string operator

# x = eval(input('Enter any Thing \n'))
# print(x)
# my_str = 'ITI pythonTEM admin'
# print(len(my_str))
# print(my_str.lower())
# print(my_str.upper())
# print(my_str.isalpha())
# print(my_str.isdigit())

#
# '''
# collection
# '''
# # list
# my_list = []
# my_list = [10, 'ahmed', ['iti', 'python'] ]
# my_list2 = [1, 2, 3, 4, 7, 6]
# print(my_list[0])
# print(my_list2[1:5])
# print(my_list[2][0])
# my_list2 = [1, 2, 3, 4, 7, 6]
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# print(my_list2[3:])
# a[:stop]       # items from the beginning through stop-1
# print(my_list2[:4])
# a[:]           # a copy of the whole arra
# print(my_list2[:])
# a[start:stop:step] # start through not past stop, by step
# print(my_list2[2:5:2])

# a[-1]    # last item in the array
# print(my_list2[-1])
# print(my_list2[-2:])
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# print(my_list2[:-2])
# a[::-1]    # all items in the array, reversed
# print(my_list2[::-1])
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, re
# l =  ['P', 'Y', 'T', 'H', 'O', 'N']
# l.append('H')
# print(l)
 # l.extend('H')
 # l -> ox27
 # +---+---+---+---+---+---+
 # | P | y | t | h | o | n |
 # +---+---+---+---+---+---+
 # 0   1   2   3   4   5   6
 #   0   1   2    3  4    5   6
# -6  -5  -4  -3  -2  -1
# Slice position: 0   1   2   3   4   5   6
# Index position:   0   1   2   3   4   5

# # updating list
# lis = ['apple', 'banana', 'cherry']
# # print('before', lis)
# # lis[1] = 'blue-berry'
# # print('after', lis)
# print('before', lis)
# del lis[1]
# print('after', lis)
# print(lis[1])

# #list operation
# my_list = [10, 'ahmed', ['iti', 'python'] ]

# print(len(my_list))
# l = [1,2,3,4] + [1, 5,6,7]
# print(l)
# print(['hi'] * 4)
# print(4 in [1, 2, 3])
# # iteration
# # for loop
# my_list = [10, 'ahmed', ['iti', 'python'] ]
# for v in my_list:
#     print(v)
# x = 2
#counter=0 -> 2
# my_list = [1, 4, 1]

# my_list.append(x)
# print(my_list)
# print(my_list.count(4))
# my_list = [1, 2]
# li = [1, 5, 3]
# my_list.extend(li)
# print(my_list)
#
# my_list = ['a', 'b', 'c']
# my_list.insert(1, 10)
# print(my_list)
# print(my_list)

# my_list.pop()
# x = my_list.pop()
# print(my_list)
# print(x)

# x = my_list.pop() # remove last element from list
# print(my_list)
# print(x)


# my_list = ['a', 'b', 'c']
# my_list.append('a')
# print(my_list)
# my_list.remove('a')
# #
# print(my_list)


# my_list.reverse()
# print(my_list)
#
# my_list = [10, 2, 3, 9, 8, 7, 0]
# my_list.sort()
# print(my_list)

# self study check what is diff between sort() and sorted()
# lambda
# iter

# len(my_list)
# constructor list()
#
#
# '''
# Tuples
# '''
#immutable
# tup = ('ahmed', 'iti', 'python')
# print(tup)
# print(tup[1])
# tup[0] = 100
# print(tup)
# del tup[0]
# print(tup)
# del tup
# print(tup)
# tup = ()
#
# x = ("2", "3", "4",)
# # print(x)
# y = tuple(('e'))
# print(y)
# cmp(x, y)

# print(len(x))
# x = (3, 4, 10, )
# # print(max(x))
# # min((2, 5))
# # x = [3]
# # x = ("2", "3", "4",)
# x = list(x)
# # print(x)
# x.append('a')
# x[1] = 100
# # print(x)
# x = tuple(x)
# print(x)
# tuple(x)
# print(tuple(x))
#
# x = (1, 2, [2], 1)
# x[2][0] = 100
# '''
# Set
# '''
# sets = {'ahmed', '2', 2}
# print(sets[0])
# for s in sets:
#     print(s)
# acccess by looping
# can not change but can add new item by add
# sets.add('ITI') # one item
# print(sets)
# sets.update({'2', 'ax', 'az'}) # more item
# print(sets)

#
# print(len(sets))
# #
# sets.remove('2')
# sets.discard('2')
# print(sets)
# st -
# st = {'12', '13', '14'}
# st.clear()
# print(st)
# set()
# x = [/, 3, 4, 5,5,5,5,5,5 ]
# print(set(x))

# dict
# dic = {'key': 'value'}
# dict = {
#     'Track': 'python',
#     'Course': 'Python',
#     'Intake': '41',
# }

# dict['Intake2']
# # dict.get('Track')
# #
# dict['Intake'] = 42
# print(dict)
# #
# print(dict.get('Intake'))
# dict = {
#     '1':'noha',
#     '2': [1, 2,3, 4,],
#     'result':{
#         'k': 'v',
#         'k2': ['v', 'Ref']
#     }
# }
# # print(dict['result']['k2'][1])
# dict.clear()
# print(dict)
# d1 = dict.copy()

# print(dict.items())
# print(dict.keys())
# print(dict.values())
# for k, v in dict.items():
#     print(k, v)
# print('dict before update', dict)
# print('----------------------------------')
# l = []
# dict = {
#     'Track': 'python',
#     'Course': 'Python',
#     'Intake': '41',
# }
# dict = {
#     'Track': ['python', 'node'],
#
# }
# dict = {}
# dict.update({'Track1': 'Mearn',
#              'Course': 'Node',
#              'Intake': '42'})
# print(dict)
# dict.update({'Track1': 'Python',
#              'Course': 'Python',
#              'Intake': '43'})
# print('after', dict)
# dic = [{'name': 'ahmed'}, {'name': 'mohmed'}]
# l.append({
#     'Track': 'python',
#     'Course': 'Python',
#     'Intake': '41',
# })
# l.append({'Track1': 'Mearn',
#              'Course': 'Node',
#              'Intake': '42'})
# # dict.popitem()
# # print(dict)
# print(l[1])
# copy, deepcopy() read about it

# in case assignment
# +-----+
# | d{} | -> 0x23
# +-----+
# +-----+             +------+
# | d{} | -> 0x23 <-  | d1{} |
# +-----+             +------+
#
# # in case copy
# +-----+             +------+
# | d{} | -> 0x23     | d1{} | -> 0x24
# +-----+             +------+
# d = {'Name': 'Ahmed'}
# # d1 = d
# d1 = d.copy()
# d1['Name'] = 'Mohamed'
# print('d ==', d)
# print('d1', d1)
# +---+
# | 3 | 0x1
# +---+
# x = 3
# a = x
#

# coopy dic without copy
# self study
# from array import array
# array('i', [1, 2, 3])

# control flow
# if exp
# elif exp
# else
# exp


# x = True
# # short
# # if a > b: print('yes')
# # print('A') if a > b else print('B')
# a = 5 if x else 0
# print(a)
#
#try it
# # 3 conditions in one line
# print('A') if a > b else print('=') if a == b else print('b')

# and or
# if a > b and c > a:
#     print('both')
# if a > b or a > c:
#     print('at least')
#
# lis = ['a', 'v', 'c', 1, ['s', 'x'], {'k': 'v'}]

# for value in lis:
#     print(value)
# dic = {'k': 'v', 'k1':'v1'}
# looping
# for value in lis:
#     print(value)
# for key, value in dic.items():
#     print('key = ', key, 'value = ', value)
# for k , v in dict:
#     print(k, v)
# lis = [1, 2, 'a', 'v', 'b', '7']
# for v in range():
#     print('idx', v, 'value', lis[v])
# # range(start, end, step)
#
# for x in range(4):
#     print(x)
# else:
#     print('f')
# for x in range(5):
#     print('x', x)
#     print('------------')
#     for y in range(3):
#         print('y', y)

# flag = True
# x = 5
# i = 1
# lis = ['a', 'v', 'c']
# while i <= len(lis): # condition
#     print(lis[i])
#     i+=1
# li = ['sara', 'nahla', 'mohamed', 'salem',]
#
# for idx, value in enumerate(li):
#     print(idx, value)


# rev list

# li = []
# li = [1, 'a', [1.0, {'key1': 'val1'}]]
# li.append('ahmed')
# li.insert(0, 'sobhy')
# li2 = (['1', 1], ('a', 'b'),  {'key1': 'val1'})
# # li2.append('ahmed')
# # li2.insert(0, 'sobhy')
# # li2[0] = 'sobhy2'
# li2 = list(li2)
# li2.append('ahmed')
# li2 = tuple(li2)
# print(li2)
# #


'''
function
'''
# +-----+
# |code | <- greeting ->  0x7f4ff66131f0
# +-----+
# def greeting():
#     # print('Hello')
#     return 'Hello'
# #
# greetin() -> invoke or call
# x = greeting()
# print(x)
# x = 3
# x()
# print(x)
# def take_input_from_user(dispaly_message):
#     take_input = input(dispaly_message + '\n')
#     return take_input
#
# print(take_input_from_user('please enter number'))
# print(take_input_from_user('please enter your name'))

# def func():
#     #path = 'file'
#     # chmod -> file
#     # os.remove(path)
#     #os.createfile()
#     print('ex')

#path
# def my_func(x=0):
#
#     return x + 5
# result = my_func(4)
# print(result)

# def add(x, y):
#     z = x + y
#     # x = 5
#     return z
# # more dynamic

# def my_func(*args):
#     for val in args:
#         print(val)
# # #
# my_func(2, 3,4,5,6,7)
# def my_func(var, *args):
#     print(var)
#     print(args)
    # for val in args:
    #     print(val)

# def is_even(i) :
#     return i%2 == 0

# def get_data_from_file(has_data, *args):
#     if has_data:
#         for v in args:
#             # do something
#             pass
#     return

# get_data_from_file(True, r65765876, 87878978)
# def test_fun(var, *args, **kwrgs):
#     print(var)
#     print(args)
#     print(kwrgs)
# test_fun(1, 3,4,5,6,76)
# def my_func(*args):
#     # print(var)
#     print(args)
#     for val in args:
#         print(val)
# my_func('2')
# my_func(5, 'tet', 'ooo', 'hhh', {'Track':'ITI'})
# def add(x, y):
# #     return x+y
# def send_email(email, message):
#     send(f'Sending email to {email} with messgae {message}')
# def send_email(emails):
#     message = 'invite'
#     for email in emails:
#         print(f"hi {email} you {message} to our web site")

# x = ['ahmed', 'iti']
# def fun(x):
#     print(x)
# fun(('tet', 'jjj'))
# send_email('elmahdy30@gmail.com', 'Hello')

# def name_of_func(): -> no return -> excute command
# def name_of_func(2): -> no return -> some logic on argument
# def fun(args)- > return args -> login ex. take 2 args return result , is_event -> take arg checl if is event return true or false
# def fun(*args) -> invoke function has dynamic args fun(1,2,3,4567)
# def fun(*args) -> invoke function has dynamic args fun(1,2,3,4567)
# def fun(**kwrgs) -> invoke function has dynamic args fun(1,2,3,4567) as dict -> k=3

# def f(**x):
#     print(x)
#
# f(l=[1,2 ,3,4,5,6,3,4,56], k1=3455,k2=6,k3=3)




# scope

# x = 5
# def f(x):
# #     # x = 1
#     x +=1
#     print('insie f', x)
#     return x
#
# x = 5
# f(x)
# print(x)
# print('outside f', x)
# def f( x ):
#     x = x + 1
#     print('in f(x): x =', x)
#     return x
#
# x = 3
# f(x)
# print(x)
# z = f( x )
# def f(x):
#     # x = 1
#     x+=1
#     print(x)
# #
# x = 5
# f(x)
# print(x)

# def g(y):
#     print(x)
#     print(x + 1)
# x = 5
# g(x)
# print(x)

# def h(y):
#     x += 1
# x = 5
# h(x)
# print(x)


# def func_a () :
#     print('inside func_a')
#
# def func_b(y):
#     # y = 2
#     print('inside func_b')
#     return y
#
# def func_c (z) :
#     # create local variable z = func_a
#     print('inside func_c')
#     return z
#
# print(type(func_a))
# print(5 + func_b(2))
# print('function, ', )
# print('function c ========',func_c(func_a))











#--------------------
# def f(y):
#     # y = 5
#     x = 1
#     x +=1
#     print(x)
#
# x = 5
# f(x)

# print(x)
# def g(y):
# #     # y = 5
#     print(x) # global
#     print( x + 1) # gloabl
# #
# x = 5
# g(x)
# print(x) # global
#
#
# def h(y):
#     #y = 5
#     x +=1
# x = 5
# h(x)
# print(x)
