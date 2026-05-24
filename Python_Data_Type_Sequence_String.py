# Data type : String

# String(str): It is use to store the text/word or sentences.
print("\n1 String(str): It is use to store the text/word or sentences.")

#01. String
print("\n01. String")

a = "Credence"
print(a)
print(type(a))

b = 'Credence is best'
print(b)
print(type(b))

c = 'C'
print(c)
print(type(c))

d = """Creadence  institute
     python Automation
     Web Ui, API, ETL Testing"""

print(d)
print(type(d))


# 02. String Operations
print("\n02. String Operations")
#Concatenation
print("Concatenation")
print("Credence" + " " + "Python")

#Repetition
print("Repetition")
print("Credence" * 2)
print(b * 3)

#Membership
print("Membership")
print("Credence" in b) #True
print("Credence" not in b) #False

s1 = "Credence"
s2 = "Python"
s3 = 'automation'
print(s1 + s2)
print(s1 * 3)

# Indexing
print("Indexing")
'''
s1 = "Credence" 1:4
C--> 0, r--> 1, e--> 2, d--> 3, e--> 4, n--> 5, c--> 6, e--> 7
C--> -8, r--> -7, e--> -6, d--> -5, e--> -4, n--> -3, c--> -2, e--> -1

s2 = "Python"
P--> 0, y--> 1, t--> 2, h--> 3, o--> 4, n--> 5
P--> -6, y--> -5, t--> -4, h--> -3, o--> -2, n--> -1
'''

#on

print(s1[0])# C
print(s1[-1])# e
print(s1[3])# d
print(s1[-5])# d

#Slicing
print("\nSlicing")
print(s1[1:4]) #red
print(s1[-7:-4]) #red
print(s2[4:6]) #on
print(s2[4:]) #on
print(s2[-2:]) #on
print(s1[3:]) #on

# 03. String Functions
print("\n03. String Functions")
print(f"Length of s1 = {len(s1)}") # imp
print(f"Length of s2 = {len(s2)}") # imp
print(f"Upper of s1 = {s1.upper()}")
print(f"Lower of s2 = {s2.lower()}")
print(f"Title of s3 = {s3.title()}")
print(f"Swap case of s3 = {s3.swapcase()}")
print(f"Swap case of s2 = {s2.swapcase()}")
s4 = "Credence Is Best"
print(f"Capitalize of s4 = {s4.capitalize()}")
print("Replace")
print(s4.replace("Credence", "Credence Institute")) # imp
print(s4.replace("Best", "Good")) # imp
print(s1.replace("e", "x")) # imp

print(f"Find 'e' in s1 = {s1.find('e')}") # Index of e, first occurrence # imp
print(f"Find 'e' in s1 = {s1.rfind('e')}") # Index of e, last occurrence
print(f"Count 'e' in s1 = {s1.count('e')}") # Count of e # imp
print(f"Startswith 'C' in s1 = {s1.startswith('C')}")
print(f"Endswith 'e' in s1 = {s1.endswith('e')}")
print(f"Endswith 'e' in s1 = {s1.endswith('x')}")
print(f"Index of 'e' in s1 = {s1.index('e')}") # imp


# String Formatting
print("\nString Formatting")

name = "Rahul"
age = 30

print("My name is", name, "and I am", age, "years old") # concatenation
print(f"My name is {name} and I am {age} years old") # f-string
print("My name is {} and I am {} years old".format(name, age)) # format old way


###########################################################
# how to convert string into int/float
string1 = "100" # string
string2 = 100.5

sum =  int(string1) + string2
print(sum)

#########################################################
string1 = "100.5" # string
string2 = 100.5

sum =  float(string1) + string2
print(sum)

#########################################################
# How to reverse the string ?
print(string1[::-1])