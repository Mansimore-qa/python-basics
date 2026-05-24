print('''
Date: 22nd Dec 2025
Conditional statement- if-elif-else
 1. if statement :  check if the condition is true .
 2. elif statement : check if the 'if statement' is false then execution is of elif.
 3. else statement :   if both "if and elif is false' then execution is of else.
''')

#Example:1 Basic If Statement
print("\n============================================")
print("Example:1 Basic If Statement")
print("============================================")

a = 10
b = 20

if a > b : # false
    print("Example 1: a is greater than b") # if statement is false this will not execute.

if a < b : # true
    print("Example 1: a is less than b")# if statement is true then and only then this will execute.


print("\n============================================")
print("Example:2 Basic If-else Statement")
print("============================================")

num1 = 10
if num1 > 0 : # True
    print(f"\nExample 2.1 : {num1} Number is positive") # this will execute
else: # it will not execute
    print(f"\nExample 2.1 : {num1} Number is negative") # it will not execute

num1 = -1
if num1 > 0:  # False
    print(f"\nExample 2.2 :{num1}  Number is positive")  # this will not execute
else:  # it will  execute
    print(f"\nExample 2.2 : {num1} Number is negative")  # it will  execute


karma= "Good"

print('G' in karma)

if 'G' in karma :  # True
    print(f"\nExample 2.2 : Your are good person, you will be in heaven")  # this will execute
else:  # it will not execute
    print(f"\nExample 2.2 : Karma karo, kand mat karo")  # it will not execute





print("\n============================================")
print("Example:3 if-elif-else Statement")
print("============================================")

num = 10
print(f"\n Example 3.1:  Number--> {num}")
if num > 0: # True
    print(f"\n Example 3.1:  Number--> {num} is positive.") # this block will execute.
elif num == 0 : # this will not execute.
    print(f"\n Example 3.1:  Number is zero.")  # this will not execute.
else:  # this will not execute.
    print(f"\n Example 3.1:  Number--> {num} is negative.")  # this will not execute.


num = 0
print(f"\n Example 3.2:  Number--> {num}")
if num > 0: #False
    print(f"\n Example 3.2:  Number--> {num} is positive.")  # this will not execute.
elif num == 0 : #True
    print(f"\n Example 3.2:  Number is zero.")  # this will execute.
else : # this will not execute.
    print(f"\n Example 3.2:  Number--> {num} is negative.")  # this will not execute.



num = -2
print(f"\n Example 3.3:  Number--> {num}")
if num > 0: # False
    print(f"\n Example 3.3:  Number--> {num} is positive.")   # this will not execute.
elif num == 0 : # False
    print(f"\n Example 3.3:  Number is zero.")   # this will not execute.
else: #  this will execute because if and elif both false
    print(f"\n Example 3.3:  Number--> {num} is negative.")  # this will not execute.




print("\n============================================")
print("Example:4 if-elif-else (multiple conditions)Statement")
print("============================================")


study_time = 7

print(f"\n Example 4.1:  study_time--> {study_time}")
if study_time > 6 : # True
    print(f"\n Example 4.1: if your study_time = {study_time} hrs, then you will get offer letter within 2 months.") # will execute
elif study_time > 4 : # will not execute
    print(f"\n Example 4.1: if your study_time = {study_time} hrs, then you will get offer letter within 4 months.")
elif study_time > 2 : # will not execute
    print(f"\n Example 4.1: if your study_time = {study_time} hrs, then you will get offer letter within 6 months.")
elif study_time == 2 : # will not execute
    print(f"\n Example 4.1: if your study_time = {study_time} hrs, then you will get offer letter within 6-8 months.")
else: # will not execute
    print(f"\n Example 4.1: You will be in market with Modiji in 2029")



study_time = 6

print(f"\n Example 4.2:  study_time--> {study_time}")
if study_time > 6 : # False
    print(f"\n Example 4.2: if your study_time = {study_time} hrs, then you will get offer letter within 2 months.") # will not execute
elif study_time > 4 : # True
    print(f"\n Example 4.2: if your study_time = {study_time} hrs, then you will get offer letter within 4 months.") # will execute
elif study_time > 2 : # will not execute
    print(f"\n Example 4.2: if your study_time = {study_time} hrs, then you will get offer letter within 6 months.")
elif study_time == 2 : # will not execute
    print(f"\n Example 4.2: if your study_time = {study_time} hrs, then you will get offer letter within 6-8 months.")
else: # will not execute
    print(f"\n Example 4.2: You will be in market with Modiji in 2029")



study_time = 3

print(f"\n Example 4.3:  study_time--> {study_time}")
if study_time > 6 : # False
    print(f"\n Example 4.3: if your study_time = {study_time} hrs, then you will get offer letter within 2 months.") # will not execute
elif study_time > 4 : # False
    print(f"\n Example 4.3: if your study_time = {study_time} hrs, then you will get offer letter within 4 months.") # will not execute
elif study_time > 2 : #  True
    print(f"\n Example 4.3: if your study_time = {study_time} hrs, then you will get offer letter within 6 months.") # will execute
elif study_time == 2 : # will not execute
    print(f"\n Example 4.3: if your study_time = {study_time} hrs, then you will get offer letter within 6-8 months.")
else: # will not execute
    print(f"\n Example 4.3: You will be in market with Modiji in 2029")



study_time = 2

print(f"\n Example 4.4:  study_time--> {study_time}")
if study_time > 6 : # False
    print(f"\n Example 4.4: if your study_time = {study_time} hrs, then you will get offer letter within 2 months.") # will not execute
elif study_time > 4 : # False
    print(f"\n Example 4.4: if your study_time = {study_time} hrs, then you will get offer letter within 4 months.") # will not execute
elif study_time > 2 : #  False
    print(f"\n Example 4.4: if your study_time = {study_time} hrs, then you will get offer letter within 6 months.") # will not execute
elif study_time == 2 : # will execute
    print(f"\n Example 4.4: if your study_time = {study_time} hrs, then you will get offer letter within 6-8 months.") # will execute
else: # will not execute
    print(f"\n Example 4.4: You will be in market with Modiji in 2029")

study_time = 1

print(f"\n Example 4.5:  study_time--> {study_time}")
if study_time > 6:  # False
    print(f"\n Example 4.5: if your study_time = {study_time} hrs, then you will get offer letter within 2 months."
          )  # will not execute
elif study_time > 4:  # False
    print(f"\n Example 4.5: if your study_time = {study_time} hrs, then you will get offer letter within 4 months."
          )  # will not execute
elif study_time > 2:  # False
    print(f"\n Example 4.5: if your study_time = {study_time} hrs, then you will get offer letter within 6 months."
          )  # will not execute
elif study_time == 2:  # False
    print(f"\n Example 4.5: if your study_time = {study_time} hrs, then you will get offer letter within 6-8 months."
          )  # will not execute
else:  # will execute
    print(f"\n Example 4.5: You will be in market with Modiji in 2029") # will execute





print("\n============================================")
print("Example:5 if-elif-else (multiple conditions)Statement")
print("============================================")


marks = 55

print(f"\n Example 5:  Marks--> {marks}")
if marks >= 80:
    print(f"\n Example 5: You have {marks} marks and You got 'A+' grade.")
elif marks >= 60:
    print(f"\n Example 5: You have {marks} marks and You got 'A' grade.")
elif marks >= 50:
    print(f"\n Example 5: You have {marks} marks and You got 'B' grade. ")
elif marks >= 40:
    print(f"\n Example 5: You have {marks} marks and You got 'C' grade. ")
else:
    print(f"\n Example 5: You have {marks} marks and You are failed.")


print("\n============================================")
print("Example:6 if-elif-else (multiple conditions)Statement")
print("============================================")


num = 10.5

if num >=0 and num <11:
    print(f"\n Example 6: The number is between 0 to 10")
elif num >=11 and num <21:
    print(f"\n Example 6: The number is between 11 to 20")
elif 21 <= num <= 100:
    print(f"\n Example 6: The number is between 21 to 100")
elif num > 100 :
    print(f"\n Example 6: The number is greater than 100")




print("\n============================================")
print("Example:7 Nested if-elif-else Statement")
print("============================================")


age = 21

if age >=18:
    print(f"\n Example 7: You are is {age} and You are adult")
    if age >= 21:
        print(f"\n Example 7: You are is {age} and You are eligible for marriage")
    else: # executed
        print(f"\n Example 7: You are is {age} and You are not eligible for marriage")
else:
    print(f"\n Example 7: You are is {age} and Your are under age")




print("\n============================================")
print("Example:8 Nested if-elif-else Statement")
print("============================================")


num = 9

if 10 <= num <=50:
    print(f"\n Example 7: Number-->{num} ,is between 10-50.")
    if num % 2 == 0:
        print(f"\n Example 7: It is even number.")
    else:
        print(f"\n Example 7: It is odd number.")
else:
    print(f"\n Example 7: Number-->{num} is out of range")




print("\n============================================")
print("Example:8  if-elif-else Statement with list")
print("============================================")


list1 = [1, 2, 3, "apple"]

#value  = 'apple'
value  = 'banana'
if value in list1:
    print(f"\n Example 8 : Value-{value} is in the list")
else:
    print(f"\n Example 8 : Value-{value} is not in the list")



print("\n============================================")
print("Example:9  if-elif-else Statement with list")
print("============================================")


list1 = [1, 2, 3, "apple"]

value  = 'banana'
if value in list1:
    print(f"\n Example 9 : Value-{value} is in the list")
else:
    list1.append(value)
    print(f"\n Example 9 : Value-{value} is added in the list")
    print(f"\n Example 9 : List1 --> {list1}")




print("\n============================================")
print("Example:10  if-elif-else Statement with string")
print("============================================")


text1 = "Credence is Best"


if "Best" in text1:
    print(f"\n Example 10.1 : Best is present in text")
    if "Credence" in text1:
        print(f"\n Example 10.1  : Credence is also present in text")
    else :
        print(f"\n Example 10.1  : Credence is not  present in text")
else:
    print(f"\n Example 10.1 : Best is not present in text")


text1 = "abc is Best"


if "Best" in text1:
    print(f"\n Example 10.2  : Best is present in text")
    if "Credence" in text1:
        print(f"\n Example 10.2  : Credence is also present in text")
    else :
        print(f"\n Example 10.2  : Credence is not  present in text")
else:
    print(f"\n Example 10.2  : Best is not present in text")


text1 = "xyz is good"


if "Best" in text1:
    print(f"\n Example 10.3 : Best is present in text")
    if "Credence" in text1:
        print(f"\n Example 10.3: Credence is also present in text")
    else :
        print(f"\n Example 10.3 : Credence is not present in text")
else:
    print(f"\n Example 10.3 : Best is not present in text")




print("\n============================================")
print("Example:11 if-elif-else (multiple conditions)Statement")
print("============================================")


marks = float(input("Enter marks:"))
print(f"\n Example 5:  Marks--> {marks}")
if marks >= 80:
    print(f"\n Example 5: You have {marks} marks and You got 'A+' grade.")
elif marks >= 60:
    print(f"\n Example 5: You have {marks} marks and You got 'A' grade.")
elif marks >= 50:
    print(f"\n Example 5: You have {marks} marks and You got 'B' grade. ")
elif marks >= 40:
    print(f"\n Example 5: You have {marks} marks and You got 'C' grade. ")
else:
    print(f"\n Example 5: You have {marks} marks and You are failed.")


print(f"\n Example : \"I am learning \\\"Python\\\" programming!" )