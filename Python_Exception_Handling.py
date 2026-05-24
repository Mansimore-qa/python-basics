
print('''
Date: 30th Dec 2025
#Exception handling:
# It is a way to manage the error and unexpected conditions in program.
# It will handle the code without crashing or throwing an error in program.
''')


# Example 1 :
print("============================================")
print(" Example 1 :")
print("============================================")


a = 5
b = 0

#print(a/b) # ZeroDivisionError: division by zero

try :
    print(a/b)
except:
    print(f"Example 1.1 : You cannot divide any number by zero")




a = 5
b = 2

#print(a/b) # ZeroDivisionError: division by zero

try :
    print(a/b)
except:
    print(f"Example 1.2 : You cannot divide any number by zero")

"""
No error --> try block will execute
error --> except block will execute
"""



print("============================================")
print("Example 2 :")
print("============================================")

x = "Hello"
y = 5

# z = x + y

try :
    x + y
except:
    print("Example 2.1 : You can't add string and integer")



a = "5"
b = 5


try :
    print(int(a) + b)
    print(type(int(a) + b))
except:
    print("Example 2.2 : You can't add string and integer")


try :
    print(a + str(b))
    print(type(a + str(b)))
except:
    print("Example 2.3 : You can't add string and integer")


print("============================================")
print("Example 3 :")
print("============================================")


list1 = [1,2,3,4,5]
index = 5
try:
    print(f"Value at index {index} is {list1[index]}")
except IndexError as err:
    print(f" Example 3  : {err}")






print("============================================")
print("Example 4 :")
print("============================================")

try :
    num = int(input("Enter the number : "))
    print(f"Example 4 :  The number is {num}")
except:
    print(f"Example 4 : Enter valid number")
else:  # optional block # execute when try block will not raise any error
    print(f"Example 4 : Else block :No error and you have entered valid number")
finally: # optional block # always execute
    print(f"Example 4 : Finally block : Code execution is completed")