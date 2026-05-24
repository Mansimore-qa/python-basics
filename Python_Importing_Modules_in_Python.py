print('''
Date: 30th Dec 2025
''')

import math
# Example 1 : Basic math module, for square root
print("============================================")
print("Example 1 : Basic math module, for square root")
print("============================================")
num = 25
print(f" Square root of {num} -->{math.sqrt(num)}")


# Example 2 : Basic math module, for factorial
print("============================================")
print("Example 2 : Basic math module, for factorial")
print("============================================")

num = 5
print(f"Factorial of {num} -->{math.factorial(num)}")


# Example 3 : Basic math module, for floor
print("============================================")
print("Example 3 :  Basic math module, for floor")
print("============================================")
num = 3.9
print(f"Factorial of {num} -->{math.floor(num)}")

# Example 4 : Basic math module, for log
print("============================================")
print("Example 4 :  Basic math module, for log")
print("============================================")
num = 10
print(f"Log of {num} -->{math.log10(num)}")


import time

# Example 5 : Basic time module, for sleep
print("============================================")
print("Example 5 : Basic time module, for sleep")
print("============================================")

time.sleep(0.2)
print("Im printing this after 5 secs hold")

import datetime
# Example 6 : Basic datetime module, for date
print("============================================")
print("Example 6 : Basic time module, for sleep")
print("============================================")

print(f"{datetime.date.today()}")

print(f"{datetime.datetime.today()}")


import random
# Example 7 : Basic random module, for random number
print("============================================")
print("Example 7 : Basic random module, for random number")
print("============================================")

print(f"{random.randint(1, 2000)}")


import os
# Example 7 : Basic os module, for
print("============================================")
print("Example 7 : Basic random module, for random number")
print("============================================")

print(f"{os.listdir()}")

