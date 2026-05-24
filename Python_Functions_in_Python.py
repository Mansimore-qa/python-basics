print('''
Date: 28th Dec 2025
Function : It is a block of code, which is used to perform specific task, 
and to organize the code, to reuse it and make it more reliable, efficient and maintainable.
''')

# Example 1 : Basic Functions
print("\n==========================================")
print("Example 1 : Basic Functions")
print("============================================")

x = 10
y = 11
sum = x + y
print(f"Example 1 : Sum of {x} + {y} = {sum}")

#def --> define a function
def sum(a,b): # function name = sum, (x,y) = function's parameter
    sum = a + b
    print(f"Function Example 1 : Sum of {a} + {b} = {sum}")

# call the function (execution the code which is defined in function)

sum(10,11)
sum(101,11)
sum(200,11)

# Example 2 : Basic Functions without parameters
print("\n==========================================")
print("Example 2 : Basic Functions without parameters")
print("============================================")

def func1():
    print("Example 2: You have defined the function without parameters")

func1()


# Example 3 : Basic Functions with default parameter
print("\n==========================================")
print("Example 3 : Basic Functions default parameters")
print("============================================")

def Welcome_message(name= "User"):
    print(f"Hello, {name}")


Welcome_message("Credence") # func will take user define value
Welcome_message() # if parameter not pass, then it will take default parameter
Welcome_message("Rahul")
Welcome_message("Pooja")




# Example 4 : Basic Functions with default parameter
print("\n==========================================")
print("Example 4 : Basic Functions default parameters")
print("============================================")

def sum(a,b,c=10):
    sum = a + b + c
    print(f" Exmaple 4 : Sum of {a} + {b} + {c} = {sum}")

sum(5,5,11)
sum(5,5)


# Example 5 : Basic Functions with default parameter and return
print("\n==========================================")
print("Example 5 : Basic Functions default parameter and return")
print("============================================")

def Welcome_message(name= "User"):
    return f"Example 5 : Hello, {name}"


print(Welcome_message("Credence")) # func will take user define value
print(Welcome_message()) # if parameter not pass, then it will take default parameter
print(Welcome_message("Rahul"))
print(Welcome_message("Pooja"))

def add(a,b):
    sum = a + b
    return sum



print(add(2,8))
print(add(a=2, b=10))
print(add(b=2, a=10))

# Example 6 : Basic Functions with variable length parameter
print("\n==========================================")
print("Example 6 : Basic Functions with variable length parameter")
print("============================================")

def add(*args):
    sum = 0 # local variable
    for i in args:
        sum = sum + i
    return f" Sum all all values : {sum}"

print(add(1,2,3))
print(add(10,20,30,40,50))
print(add(1,2,3,4))
print(add(4, 14))


# Example 7 : Nested Functions for sum and sub
print("\n==========================================")
print("Example 7 : Nested Functions for sum and sub")
print("============================================")


def add (x, y):
    sum = x + y
    return sum

def sub (x, y) :
    sub = x - y
    return sub

print(f"Example 7.1 :  Sum of two values is {add(20,10)} ")
print(f"Example 7.1 :  Sub of two values is {sub(20,10)} ")

def Calculator(a,b):  # outer function
     def add(): # inner function
         return f" Sum of {a} + {b} = {a+b}"

     def sub():  # inner function
         return f" Sub of {a} - {b} = {a-b}"

     def mul():  # inner function
         return f" Mul of {a} * {b} = {a*b}"

     return add(), sub(), mul()# here outer function is calling inner functions

print(Calculator(20,10))
print(Calculator(100,5))
print(Calculator(100,5000))


# Example 8 : Global variable in functions
print("\n==========================================")
print("Example 8 : Global variable in functions")
print("============================================")

"""
Global variable :
1. It the variable which is define outside the function.
2. We can access it inside or outside the function
3. it is like normal variable , which is use to store the data.
"""

score = 50 # Global variable which is defined outside the function.

def increase_score():
    global score
    score = score + 10
    return f"increased score {score}"

def decrease_score():
    global score
    score = score - 10
    return f"decreased score {score}"

print (increase_score())
print(decrease_score())


# Example 8 : Local and Non-Local variable in functions
print("\n==========================================")
print("Example 8 : Local and Non-Local variable in functions")
print("============================================")
def outer_func():
    x = 10 # it is defined in outer func
    def inner_func():
        nonlocal x # used in inner func
        x = x + 100
        return x
    return inner_func()


print(outer_func())


# Example 9 : Recursive Function
print("\n==========================================")
print("Example 9 : Recursive Function")
print("============================================")

# Recursive Function--> Functions which call itself is called recursive function.

"""
5 ! = 5 * 4 * 3 * 2 * 1 = 120
4 ! = 4 * 3 * 2 * 1 = 24
3 !  = 3 * 2 * 1 = 6
2 !  = 2 * 1 = 2
1 !  =  1 = 1
"""


def factorial(num):
    if num == 1:
        return 1
    else :
        return num * factorial(num-1)

"""
factorial(5)
-->5 * factorial(4)
factorial(4)
4 * factorial(3)
factorial(3)
3 * factorial(2)
factorial(2)
2 * factorial(1)
factorial(1)
1
"""


print(factorial(10))



# Example 10 : lambda function
print("\n==========================================")
print("Example 10 : lambda function")
print("============================================")
# lambda functions are simple, short, short logic, small small
# it is used to create small function.

# syntax =
# lambda arguments : expression

def add (a,b):
    return a+b

print(add(10,20))


add_lambda = lambda a,b : a + b

print(f"lambda function output --> {add_lambda(5,10)}")


# Example 11 : lambda function
print("\n==========================================")
print("Example 11 : lambda function")
print("============================================")

# function_name = lambda arguments : expression


squares = lambda x : x**2

print(squares(5))

# Example 12 : lambda function with if
print("\n==========================================")
print("Example 12 : lambda function with if")
print("============================================")


def num_compare1(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(f"compare two number and show largest number: {num_compare1(100,111)}")


num_compare2 = lambda num1, num2 : num1 if num1 > num2 else num2
print(f"compare two number and show largest number: {num_compare2(20,21)}")


# Example 13 : lambda function to check even nmumber
print("\n==========================================")
print("Example 13 : lambda function to check even nmumber")
print("============================================")


check_even = lambda num : True if num %2==0 else False

print(f"Is the number even ? -- > {check_even(50)}")