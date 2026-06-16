# l=[1,2,[3,4]]
# import copy
# k = copy.deepcopy(l)
# from copy import deepcopy    # deep copy
# k = deepcopy(l)
# k[2].append(37)
# print(l)
# print(k)
# ------------------------------------------------------------------------
# k=l.copy()
# k[2].append(35)            # shallow copy
# print(l)
# print(k)
# ------------------------------------------------------------------------
# functions in python:

# def func(x):
#     print(x**x)
# func(3)
# ------------------------------------------------------------------------
# def details(name, age, branch):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Branch: {branch}")
# details(name="Nikhil", age=21, branch="CSE")
# ------------------------------------------------------------------------
# x=300
# def func4():
#     print(x)     #unbound local error
#     x=200
# func4()
# ------------------------------------------------------------------------
# def func5(x,y):
#     print("Sum of x:",sum(x))
#     print("Sum of y:",sum(y))
#     print("Sum of x and y:",sum(x)+sum(y))
# func5([1,2,3,4,5], [6,7,8,9,10])
# ------------------------------------------------------------------------
# Arbitary parameters in python:

# def func6(*args):
#     print(args)                               #Positional arguments
#     print(*args)                              #Unpacking the arguments
# func6(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# ------------------------------------------------------------------------
# def func7(**kwargs):
#     print(kwargs)                             #Keyvalue arguments
# func7(a=10, b=20, c=30, d=40, e=50)
# ------------------------------------------------------------------------
# def func8(a,b):
#     print(a,b)
# def func9(**kwargs):
#     print(kwargs)
#     func8(**kwargs)                             #Unpacking the keyvalue arguments
# func9(a=10, b=20)
# ------------------------------------------------------------------------
# def func10(*args, **kwargs):
#     print(args,kwargs,sep="\n")                                          #tuple
#     print(type(args), type(kwargs), sep="\n")                            #dicitonary
# func10(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,a=10,b=20,c=30,d=40,e=50,f=60)
# ------------------------------------------------------------------------
# def func11(*a):
#     s=0
#     for i in a:
#         s+=i
#     print(s)
# func11(7,8,6,5,2,3,9)
# ------------------------------------------------------------------------
# def func11(*a):
#     s=1
#     for i in a:
#         s*=i
#     print(s)
# func11(7,8,6,5,2,3,9)
# ------------------------------------------------------------------------
# return statement in python:
# def func12(a,b):
#     print(a+b)
#     return a+b
# print(func12(10,20))
# ------------------------------------------------------------------------
# def func13(a,b):
#     return a*b
# def func14(x,y):
#     return x+y
# print(func14(func13(23,53), func13(31,27)))    #2056 answer
# ------------------------------------------------------------------------
# question: f(x)= x^3 + 3x^2 + 53  g(y)= y^2 +2y + 1   v(x,y) : x*y  for this print(v(f(10),g(12)))
# def f(x):
#     return x*3 + 3*x*2 + 53
# def g(y):
#     return y**2 + 2*y + 1
# def v(x,y):
#     return x*y
# print(v(f(10),g(12)))         #228657 answer
# ------------------------------------------------------------------------
# a=5
# def f():
#     global a
#     a+=1
#     print(a)
# f()   #6
# ------------------------------------------------------------------------
# a=5
# def f():
#     a+=1
#     print(a)   #unbound local error
# f() 
# ------------------------------------------------------------------------
# memory management in python: threshold, count, referents, referrers, disable, enable
# import gc
# gc.collect()
# a = ["Hello", "Hi", 6000]
# # print(gc.get_referrers(10)) 
# print(gc.get_referents(a))
# print(gc.get_count())
# print(gc.get_threshold())
# print(gc.set_threshold(700,10,10))
# print(gc.get_threshold())
# print(gc.disable())
# print(gc.enable())
# --------------------------------------------------------------
#  Write a function called say_hello() that prints 'Welcome to Python!' 
# def say_hello():
#     print('Welcome to Python!')
# say_hello()
# ----------------------------------------------------------
#  Write a function called add(a, b) that returns the sum of two numbers. 
# def funcsum(a,b):
#     return a+b
# print(funcsum(12,20))
# ------------------------------------------------------------
#  What is the output of a function that has no return statement? Write a function to verify this.
# def func():
#     print("This function has no return statement.")
# func()
# ----------------------------------------------------------
#   Write a function area_of_rectangle(length, width) that returns length * width. Call it with values 6 and 4. 
# def rec(length, width):
#     return length * width
# print(rec(6,4))
# ---------------------------------------------------------
#  Create a function describe_pet(animal, name) that prints: 'My [animal] is named [name].' 
# def describe_pet(animal, name):
#     print(f"My {animal}'s name is {name}.")
# describe_pet('Lion', 'Simba')
# -----------------------------------------------------------
# What happens if you call a function with fewer arguments than parameters? Try it and note the error. 
# def func(a,b):
#     return a+b
# print(func(10))  #TypeError: func() missing 1 required positional argument: 'b'
# -------------------------------------------------------
#  Write a function power(base, exponent) that returns base raised to exponent using the ** operator. 
# def func(base, exponent):
#     return base ** exponent
# print(func(4, 6))
# ------------------------------------------------------------
#   Create a function full_name(first, middle, last) that returns the full name as a single string. 
# def full_name(first_name, middle_name, last_name):
#     return f"{first_name}{middle_name}{last_name}"
# print(full_name("Nikhil ", "Tejas ", "Bogawar"))
# --------------------------------------------------------------
# Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference. 
# def intro(name, city, hobby):
#     print(f"Myname is {name}, I live in {city} and my hobby is {hobby}.")
#     print(f"the {city} is so beautiful and {name} akfdh {hobby}")
# intro("Nikhil", "Hyderabad", "Making Arts")
# ------------------------------------------------------------
# Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)? 
# def subtract(a,b):
#     return a-b
# print(subtract(10,3))     # 7
# print(subtract(3,10))     # -7
# -----------------------------------------------------------------------
# Write a function bio(first_name, last_name, age) and call it correctly using positional arguments. 
# def bio(first_name, last_name, age):
#     print(f"My name is {first_name} {last_name} and I am {age} years old.")
# bio("Nikhil", "Bogawar", 21)
# ---------------------------------------------------------------
# Can you pass more positional arguments than there are parameters? What error do you get? 
# def pa(a,b,c):
#     print(a+b+c)
# pa(1,2,3,4) 
# ---------------------------------------------------------
# Call the function send_email(to, subject, body) using keyword arguments in any order. 
# def send_email(to, subject, body):
#     print(f"Sending email to: {to}")
#     print(f"Subject: {subject}")
#     print(f"Body: {body}")
# send_email(to= 'nikhil', subject= 'for testing', body= 'this is a text email')
# ---------------------------------------------------------------
# Write a function create_profile(username, email, age) and call it using keyword arguments. 
# def create_profile(username, email, age):
#     print(f"Username: {username}")
#     print(f"Email: {email}")
#     print(f"Age: {age}")
# create_profile(username="Nikhil", email="tejasnikhil72@gmail.com", age=21)
# ------------------------------------------------------------
# What is the error if you place a positional argument after a keyword argument? Test it. 
# def fun(a,b,c):
#     print(f"value of a,b,c: {a} {b} {c}")
# fun(a=23, 5, 3)  #SyntaxError: positional argument follows keyword argument
# -------------------------------------------------------
#   Write a function power(base, exponent=2) that returns base^exponent. Test with one and two arguments. 
# def power(base, exponent=2):
#     return base ** exponent
# print(power(4))
# --------------------------------------------------------
#   Create a function connect(host, port=3306, protocol='TCP') and call it with various combinations.
# def connect(host, port=3306, protocol='TCP'):
#     print(f"Connecting to {host} on port {port} using {protocol} protocol.")
# connect('localhost')
# connect('localhost', 8080, 'UDP')
# ------------------------------------------------------------------
# Write a function discount_price(price, discount=10) that returns the discounted price. Test with and without the discount argument. 
# def discount_price(price, discount=10):
#     discounted_price = price - (price * discount / 100)
#     return discounted_price
# print(discount_price(100))
# ------------------------------------------------------------------
#  Write a function multiply_all(*args) that returns the product of all numbers passed.
# def multiply_all(*args):
#     mul = 1
#     for i in args:
#         mul = mul * i
#     return mul
# print(multiply_all(1,2,3,4))
# ---------------------------------------------------------
#  Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line. 
# def display_tags(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# display_tags(name="Nikhil", age=21, branch="CSE", city="Hyderabad")
# -------------------------------------------------------------
# Higher order functions in python:
# def fun(x,y):
#     x(y)
# def fun2(z):
#     print(z*z)
# fun(fun2,10)
# -------------------------------------------------------------
# Higher order functions with lambda:
# Map() function -------->>>
# salary = [10000,24000,65000,14500,31000]
# def increment(x):
#     return x+2000
# updated_list=list(map(increment, salary))
# print(updated_list)   
# print(list(map(lambda x: x+2000, salary)))    #using labmda function with map() function (only this line code)
# ------------------------------------------------------------------------
# Filter() function -------->>>
# marks=[35,15,24,11,36,49,21,33,17,36]
# def check(m):
#     return m>=25
# print(list(filter(check, marks)))
# print(list(filter(lambda m: m>=25, marks))) #using lambda funtion with filter() function (only this line code)
# ------------------------------------------------------------------------
# Reduce() function -------->>>
# funds = [1500, 2500, 1400, 1000, 3200]
# def add(x,y):
#     return x+y
# from functools import reduce
# print(reduce(add, funds))
# print(reduce(lambda x,y: x+y, funds))  #using lambda function with reduce() function (only this line code)
# ------------------------------------------------------------------------
# Sorted() function -------->>>
# names = ["Nikhil", "Tejas", "Bharath", "Vishal", "Naresh", "Srikanth", "Ganesh"]
# print(sorted(names, key=len))
# print(sorted(names, key=lambda x: x[0])) #using lambda function with sorted() function (only this line code)
# ------------------------------------------------------------------------
# findng consonants
# k=input()
# for i in k:
#     if (lambda x:x not in "AEIOUaeiou")(i):
#         print(i)                                 # m chstnnv
# ------------------------------------------------------------------------
# Quiz question:
# k=[[1,2],[4,5],[6,7]]
# l=[]
# m=lambda x:x.append(25)
# for i in k:
#     l.append(m(i))
# print(k)              # [[1, 2, 25], [4, 5, 25], [6, 7, 25]]
# print(l)              # [None, None, None] because append() function returns None value
# ------------------------------------------------------------------------
# create python application where we use 4 functions with parameters and return types call them in single line
# add = lambda x: x + 5
# sum = lambda x: x - 2
# mul = lambda x: x * 4
# div = lambda x: x / 2
# final = add(sum(mul(div(99))))
# print(final)          #201.0

# ------------------------------------------------------------------------
# Lambda Functions and Higher order functions using map() function
# def cel(x):
#     c=(x-32)*(5/9)
#     return c
# print(cel(29))

# k=[]
# for i in s:
#     k.append(ord(i))
#or
# s="Hello"
# print(list(map(ord,s)))  # [72, 101, 108, 108, 111]

# celsius to farenhit using funcitons:
# f=[0,-3,-8,2]
# c=list(map(lambda x:(x-32)*(5/9),f))
# print(c)            # [-17.77777777777778, -19.444444444444446, -22.22222222222222, -16.666666666666668]

#or

# f=[0,-3,-8,2]
# def fun(x):
#     return (x-32)*(5/9)
# print(list(map(fun,f)))

#farenhit to celcius using functions:
# c=[0,-3,-8,2]
# f=list(map(lambda x:((9*x/5)+32),c))
# print(f)                 # [32.0, 26.6, 17.6, 35.6]

# another example in map functions:
# l1=[1,2,3,4,5]
# l2=[10,11,12,13,14]
# l3=[25,26,27,28,29]
# k=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
# print(k)   # [36, 39, 42, 45, 48]
# ------------------------------------------------------------------------
# Removing Vowels from a List of Strings Using map()
# l = ["Hello", "hii", " will ','you", "be"]
# def rv(word):
#     cw = ""                      
#     for char in word:                      
#         if char not in "AEIOUaeiou":       
#             cw = cw + char  
#     return cw                   
# res = list(map(rv, l))
# print(res)
# ------------------------------------------------------------------------

# l=["Hello", 'Hii', "Who','are", "you?"]
# k=[]
# def fun(x):
#     if x not in "AEIOUaeiou":
#         return x
#     return ""
# for i in l:
#     s=list(map(fun,i))
#     s="".join(s)
#     k.append(s)
# print(k)           # ['Hll', 'H', "Wh','r", 'y?']
# def fun2(y):
#     s=0
#     for i in y:
#         s+=ord(i)
#     return s
# A=list(map(fun2,k))
# print(A)           # [288, 72, 427, 184]

