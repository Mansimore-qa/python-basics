# Operators in Python
print("Operators in Python")
print("\ni.Arithmetic Operators in Python : +, -, *, /, //, %, **")

value1 = 10 # int
value2 = 5 # int
value3 = 5.5 # float
value4 = "Credence is Best" # text/string
value5 = 3 #int

addition = value1 + value2 # 10 + 5
subtraction = value1 - value2 # 10 - 5
multiplication = value1 * value2 # 10 * 5
division = value1 / value2# 10 / 5
floor_division = value1 // value5 # 10 // 3
modulus = value1 % value2 # 10 % 5
exponent = value1 ** value5 # 10 ** 3

print("Addition of value1 and value2 is:\n", addition) # 15
print("Subtraction of value1 from value2 is:\n", subtraction) # 5
print("Multiplication of value1 and value2 is:\n", multiplication) # 50
print("Division of value1 and value2 is:\n", division) # 2
print("Floor_division of value1 and value5 is:\n", floor_division) # 3
print("Modulus of value1 and value2 is:\n", modulus) # 3
print("Exponent of value1 and value5 is:\n", exponent) # 1000

# f-string
print("\nf-string format")
print(f"Addition of {value1} + {value2} = {addition}")
# put variable in {}



print("\nii. Comparison Operators in Python :==, !=, >, <, >=, <=")
# single = --> assignment
# double == --> comparison

x = 10 # single = --> assignment
y = 20
z = 10

print(f"{x}=={y}:{x==y}") # == Equals to # Output: False # double == --> comparison
print(f"{x}=={z}:{x==z}") # == Equals to # Output: True
print(f"{x}!={y}:{x!=y}") # != Not equals to # Output: True
print(f"{x}>{y}:{x>y}") # > greater than # Output: False
print(f"{x}<{y}:{x<y}") # < less than # Output: True
print(f"{x}>={y}:{x>=y}") # >= greater than and equals to # Output: False
print(f"{x}<={y}:{x<=y}") # <= less than and equals to # Output: True

# shift +ctrl+alt for multiple cursors

print("\niii. Logical Operators in Python : and, or, not")
a = True
b = False
c = True
d = False

# and
print("\na. Logical Operators : and")
print(f"{a} and {b}: {a and b}") # False
print(f"{a} and {c}: {a and c}") # True
print(f"{b} and {d}: {b and d}") # False

# or
print("\nb. Logical Operators : or")
print(f"{a} or {b}: {a or b}") # True
print(f"{a} or {c}: {a or c}") # True
print(f"{b} or {d}: {b or d}") # False

# not
print("\nc. Logical Operators : not")
print(f" not {a}: { not a }") # False
print(f" not {b}: { not b }") # True


print("\niv. Assignment Operators in Python : =, +=,-=, *=, /=,//=, %=, **=")

x = 5
print(f"x= {x}")
print(f"Now the value of x is: {x}")

x += 3 # x = x+3
print(f"x += 3: {x}")
print(f"Now the value of x is: {x}")
# x= 8

x -= 3 # x = x-3
print(f"x -= 3: {x}")
print(f"Now the value of x is: {x}")
# x= 5

x *= 2 # x = x*3
print(f"x *= 2: {x}")
print(f"Now the value of x is: {x}")
# x= 10


x /= 2 # x = x/3
print(f"x /= 2: {x}")
print(f"Now the value of x is: {x}")
# x= 5.0



x //= 2 # x = x//3
print(f"x //= 2: {x}")
print(f"Now the value of x is: {x}")
# x= 2.0

y = 11
y %=3  # y = y%3
print(f"y %= : {y}")
print(f"Now the value of y is: {y}")
# y = 2


y **=3  # y = y%3
print(f"y **= : {y}")
print(f"Now the value of y is: {y}")
# y = 8



print("\nv. Membership Operators in Python : in, not in")

text1 = "Credence automation Testing: Web-UI, ETL, API"
text2 = "Credence is Best"


#IN
x = 'API' in text1
print(x)

print(f"'Web-UI' in text1:{ 'Web-UI' in text1}")
print(f"'Best' in text1:{ 'Best' in text1}")
print(f" 'w' in text1:{ 'w' in text1}")
print(f" 'W' in text1:{ 'W' in text1}")

# NOT IN
print(f" 'W' not in text1:{ 'W' not in text1}")
print(f" 'w' not in text1:{ 'w' not in text1}")


print("\nv. Identity Operators in Python : is, is not")
a = 10
b = 10
c = 11


# a is b # true
# a is not b # false


print(f"is a identical to b : {a is b }") # True
print(f"is a identical to b : {a is not b }") # False
print(f"is a identical to c : {a is not c }") # True
print(f"is b identical to c : {b is c }") # False
print(f"is a identical to c : {a is c }") # False
print(f"is a identical to c : {a is c }") # False
print(f"is a identical to c : {a is c }") # False
print(f"")



# List
# Tuple
