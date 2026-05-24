
# List comprehension is the way of creating a new list based
# on logic or expression for item in iterables.

print('''
Date: 30th Dec 2025
''')

# 01. List Compression -squares
# Syntax : new_list = [expression for item in iterable]
print("==========02. List Compression - squares ===========")

squares = [x**2 for x in range(11)]
print(f"{squares}")


# 03. List Compression -
print("==========03. List Compression - odd number squares ===========")

odd = [x**2 for x in range (20) if x%2==1]
print(f"{odd}")

import math
# 04. List Compression -Factorial
print("==========04. List Compression - Factorial ===========")

Factorial = [math.factorial(x) for x in range(10)]
print(f"{Factorial}")


