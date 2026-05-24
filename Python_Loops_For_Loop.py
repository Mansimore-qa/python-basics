print('''
Date: 26th Dec 2025
1. Loop in python are use to run block of code multiple times.
2. Loop help us to reduce repetition, efficient and readable code.
3. There are two type of loops in python
    a. For Loop
    b. While Loop
''')


print("\n============================================")
print("1.For Loop")
print("============================================")
print("""
1. It is used to iterate over sequence (like range, list, tuple, dict, set, string)
2. Use for loop when you know the number of iteration(how much time you have to execute the code).
""")


#Example:1 Basic For Loop
print("\n============================================")
print("Example:1 Basic For Loop")
print("============================================")

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)


for i in range(1,7) : # i --> Iterator/ Loop variable # range-->(1,7)--> sequence how many times loop should run
    print(f"Example:1 --> {i}") # This code will run 6 times if the range is (1,7)

# 1st loop --> i = 1
# 2nd loop --> i = 2
# 3rd loop --> i = 3
# 4th loop --> i = 4
# 5th loop --> i = 5
# 6th loop --> i = 6


#Example:2 Basic For Loop with list
print("\n============================================")
print("Example:2 Basic For Loop with list")
print("============================================")

list1 = [1,2,3,"a", "apple", True]
for item in list1: # len(list) = 6, then it will run 6 times
    print(f"Example 2 : {item}")


#Example:3 Basic For Loop : print the squares of number from 1 to 10
print("\n============================================")
print("Example:3 Basic For Loop : print the squares of number from 1 to 10")
print("============================================")


for num in range (1,11): # how many times we have to run the code will be decided by this statement.
    print(f"Example 3 : Square of {num} is :  {num**2}") # Code


#Example:4 Basic For Loop : print the cubes of number from 1 to 10
print("\n============================================")
print("Example:4 Basic For Loop : print the cubes of number from 1 to 10")
print("============================================")

for num in range (1,11): # how many times we have to run the code will be decided by this statement.
    print(f"Example 4 : Cube of {num} is :  {num**3}") # Code


#Example:5 Basic For Loop : print the square root of number from 1 to 10
print("\n============================================")
print("Example:5 Basic For Loop : print the square root of number from 1 to 10")
print("============================================")

for num in range (1,11): # how many times we have to run the code will be decided by this statement.
    print(f"Example 5 : Square root of {num} is :  {num**(1/2)}") # Code



#Example:6 Basic For Loop : String
print("\n============================================")
print("Example:5 Basic For Loop : String")
print("============================================")

text = "Credence is Best"
for i in text: # how many times we have to run the code will be decided by this statement.
    print(f"Example 6 : {i}") # Code


#Example:7 Basic For Loop : If statement
print("\n============================================")
print("Example:7 Basic For Loop : If statement")
print("============================================")

list1 = [100,1,2,3,4,5,6,7,8,9,10,111,323,4355]

for i in list1: # for variable in sequence
    if i % 2 == 0:
        print(f"Example 7 : {i} is even.")
    elif i % 2 == 1:
        print(f"Example 7 : {i} is odd.")


#Example:8 For loop with break statement
print("\n============================================")
print("Example:8 For loop with break statement (find number 10 is list and stop the loop)")
print("============================================")

list1 = [100,1,2,3,4,5,6,7,8,9,10,111,323,4355]

for item in list1:
    if item == 10 : # condition true
        break # it will break th loop means will stop or exit the loop.
    print(f"Example 8 : {item}")


companies = ["TCS", "Infosys" , "Cognizant", "Nagarro" ]

for company in companies :
    print(f"Cleared the interview in {company}")
    if company == "Cognizant":
        print("Offer letter received from Cognizant, reject the offers from other companies")
        break


# Example:9 For loop with continue statement
print("\n============================================")
print("Example:9 For loop with continue statement ()")
print("============================================")

list1 = [100,1,2,3,4,5,6,7,8,9,10,111,323,4355]

for item in list1:
    if item == 10 : # condition true
        continue #  for item 10, loop will skip that iteration and continue for next items.
    print(f"Example 9 : {item}")

Hobbies = ["SQL", "Manual Testing" , "Instagram", "Whats app", "Python", "Snap chat", "Selenium"]

for item in Hobbies :
    if item in ["Instagram", "Whats app", "Snap chat"]:
        print(f"skipping : {item}")
        continue
    print(item)


# Example:10 For loop with pass statement
print("\n============================================")
print("Example:9 For loop with pass statement")
print("============================================")

list1 = [100,1,2,3,4,5,6,7,8,9,10,111,323,4355]

for item in list1:
    if item == 10 :
        print("You will received the offer letter")
        pass  # do nothing why ? reasons : not decided yet what should be the logic and dont want to error because on incomplete code


# Example:11 For loop with dict
print("\n============================================")
print("11 For loop with dict")
print("============================================")

dict1 = {1: "Apple", 2: "banana", 3 : "cherry"}

for key in dict1:
    print(f"Example 11 --> ({key} : {dict1[key]})")



# Example:12 Nested For loop
print("\n==============27th-Dec-2025====================")
print("\n============================================")
print("11 Nested For loop")
print("============================================")


for i in range (1,4): # Outer for loop, run--> 3 times
    for j in range (1,4):# Inner for loop, run--> 3 times
        print(f"Example 12 : {i},{j} ")

"""
First :
outer loop--> i=1, inner loop--> j=1
outer loop--> i=1,  inner loop--> j=2
outer loop--> i=1,  inner loop--> j=3
exit the inner loop

go to outer loop:
outer loop--> i=2, inner loop--> j=1
outer loop--> i=2, inner loop--> j=2
outer loop--> i=2, inner loop--> j=3
exit from inner loop

go to outer loop
outer loop--> i=3, inner loop--> j=1
outer loop--> i=3, inner loop--> j=2
outer loop--> i=3, inner loop--> j=3
exit the inner loop
exit the outer loop

"""

# Example:13 Nested For loop to create tables from 2 to 10
print("\n============================================")
print("Example:13 Nested For loop to create tables from 2 to 10")
print("============================================")

for i in range(2,11):
    for j in range(1,11):
        print(f"Example:13 Table of {i}-->{i}*{j} = {i*j}")

# Example:14 Nested For loop with lists
print("\n============================================")
print(" Example:14 Nested For loop with lists")
print("============================================")

list1 =[1,2,3]
list2 = ["a", "b", "c" ]


for i in list1:
    print(f"Example:14 Outer Loop no {i}")
    for j in list2:
        print(f"Example:14 Inner Loop no {j}")
        print(f"Example:14  (i, j)-->({i}, {j})")



# Example:15 Nested For loop with lists and break
print("\n============================================")
print(" Example:15 Nested For loop with lists")
print("============================================")

list1 =[1,2,3]
list2 = ["a", "b", "c", "d" , "e" ]


for i in list1:
    print(f"Example:15 Outer Loop no {i}")
    for j in list2:
        if j == "e":
            break
        print(f"Example:15 Inner Loop no {j}")
        print(f"Example:15  (i, j)-->({i}, {j})")


# Example:16 Nested For loop to stars
print("\n============================================")
print("Example:16 Nested For loop to stars")
print("============================================")

print("Apple")
print("Banana")
print("Cherry")
###############
print("Apple", end= " ")
print("Banana", end= " ")
print("Cherry" )
print("")
for i in range(1,4):
    for j in range(1,4):
        print("*", end=" ")
    print("")


# Example:17 Nested For loop to print right angle triangle
print("\n============================================")
print("Example:17 Nested For loop to print right angle triangle")
print("============================================")

for i in range(1,10):
    for j in range(i):
        print("*", end=" ")
    print("")


# Example:18 Enumerate function, enumerate--> (index, value)
print("\n============================================")
print("Example:18 Enumerate function enumerate--> (index, value")
print("============================================")


list1 = ["Red", "Blue", "Green", "White", "Black"]

for index, colour in enumerate(list1):
    print(f"Example 18 : index -->{index}, colour -- > {colour}")

#
# list1 = ["Red", "Blue", "Green", "White", "Black"]
# i = 0
# for name in list1:
#     print(f"{i}--> {name}")
#     i +=1
