print('''
Date: 27th Dec 2025
1. Loop in python are use to run block of code multiple times.
2. Loop help us to reduce repetition, efficient and readable code.
3. There are two type of loops in python
    a. For Loop
    b. While Loop
''')

# Example 1 : Basic While loop to print number from 1 to 6
print("\n============================================")
print("Example 1 : Basic While loop to print number from 1 to 6")
print("============================================")
print("""
 Use for loop when you dont know the number of iteration.
""")

i = 0 # i --> loop variable/iterator, loop value starting from 0 ,
while i <= 6: # when i = 7 , loop exit
    print(f"Example 1 : {i}")
    i +=1


# Example 2 : Basic While loop  with list
print("\n============================================")
print(" Example 2 : Basic While loop  with list")
print("============================================")

list1 = [1,2,3,4,5]

num = 0
while num <= len(list1)-1 : #len(list1) --> 5
    print(f"Example 2 : {list1[num]}")
    num = num +1


# Example 3 : Basic While loop
print("\n============================================")
print(" Example 3 : Basic While loop ")
print("============================================")

while True:
    num = int(input("Enter a Number:"))
    if num%2 ==0:
        print(f"Exmaple 3 : {num} is even.")
        break
    else:
        print(f"Exmaple 3 : {num} is odd, Enter even number")
