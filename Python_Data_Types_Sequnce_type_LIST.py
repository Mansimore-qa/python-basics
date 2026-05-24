# Data Type- List

# List : List is a collect of items in a particular order, which can be same or different data type.
# list is mutable.

# 01. List
print("\n 01. List")

list1 = [1,2,"a",True, 1.5]
print(list1)
print("The data typ", (type(list1)))

#02. List Examples
print("\n 02. List Examples")

list1 = [1,2,3,4,5, 5.5]
list2 = ["apple", "banana", "cherry"]
list3 = [True, False, True]
list4 = ["apple", 1, True ]

print(f"List1-->{list1}")
print(f"List2-->{list2}")
print(f"List3-->{list3}")
print(f"List4-->{list4}")

# 03. Operations with List
list1 = [3,1,2,3,4,5, 5.5]
list2 = ["apple", "banana", "cherry", "automation Testing", "credence is best", "ETL automation", "API Automation"]
print("\n03. Operations with List")
print(f"Concat list1 + list2-->{list1 + list2}")
print(f"Len list1 ->{len(list1)}")
print(f"Len list2 ->{len(list2)}")
print(f"Repetition of list2 ->{(list2*3)}")
list1.sort() # ascending order
print(f"Sort list1 ->{list1}")
list2.sort() # ascending order
print(f"Sort list2 ->{list2}")
list2.sort(reverse=True) # descending order
print(f"Reverse Sort list2 ->{list2}")
print(f"Membership: 1 in list1 :  ->{ 1 in list1}") # True
print(f"Membership: 1 in list2 :  ->{ 1 in list2}") # False
print(f"Membership: 'apple' in list2 :  ->{ 'apple' in list2}") # True
list1 = [3,1,2,3,4,5, 5.5]
list2 = ["apple", "banana", "cherry", "automation Testing", "credence is best", "ETL automation", "API Automation","apple"]

# "apple"--> 0, "banana" --> 1, "cherry"-->2, "automation Testing"-->3,
# "credence is best"-->4, "ETL automation"-->5, "API Automation"-->6,"apple"-->7

# "apple"--> -8, "banana" --> -7, "cherry"-->-6, "automation Testing"-->-5,
# "credence is best"-->-4, "ETL automation"-->-3, "API Automation"-->-2,"apple"-->-1

print(f"Index of 'apple' in list2 :{list2.index('apple')}")
print(f"Index of 'API Automation' in list2 :{list2.index('API Automation')}")
print(f"Count of 'apple' in list2 :{list2.count('apple')}")
print(f"Count of 3 in list1 :{list1.count(3)}")
print(f"Count of 1 in list1 :{list1.count(1)}")
print(f"Value at 2nd index of list2-->{list2[2]}")
print(f"Value at -4 index of list2-->{list2[-4]}")
print(f"Value at -6 index of list2-->{list2[-6]}")
print(f"Slice of list2-->{list2[3:5]}")
print(f"Slice of list2-->{list2[6:]}")
print(f"Slice of list2-->{list2[-2:]}")
print(f"Slice of list2-->{list2[7:]}")
print(f"Slice of list2-->{list2[-1:]}")
print(f"Slice of list2-->{list2[:]}") # whole list
print(f"Slice of list2-->{list2[:2]}") # stop at index 2
print(f"Slice of list2-->{list2[::2]}") # stepping same you can use for string also.
print(f"Reverse the list1 {list1[::-1]}") # reverse the list
print(f"Reverse the list2 {list2[::-1]}") # reverse the list
list2.reverse()
print(f"Reverse the list2 {list2}") # reverse the list




# 04. List Methods

list1 = [3,1,2,3,4,5, 5.5]
list2 = ["apple", "banana", "cherry", "automation Testing", "credence is best", "ETL automation", "API Automation"]
print("\n04. List Methods ")

list1.append(6)
print(f"append 6 in list1 -->{list1}")

list1.insert(2,5)
print(f"insert 5 at index 2 in list1 -->{list1}")

list1.remove(5.5) # removes the specific value
print(f"remove 5.5 from list1 -->{list1}")

list1.pop(3) # index 3 --> 2 will be removed from list, via pop we can pop value at specific index
print(f"pop at 3rd index from list1 -->{list1}")

list1.pop()
print(f"pop()--> last value from list1 -->{list1}")

list1.extend([6,7,8,9,10,11,12,13,14])
print(f"extend the list1 with new values -->{list1}")

list1.extend([15,16])
print(f"extend the list1 with new values -->{list1}")


list1.sort()
print(f"sort the list1 -->{list1}")

list1.sort(reverse=True)
print(f"Reverse sort the list1 -->{list1}")


##########################################################

list4 = list1 # direct copy
print(f"List list4-->{list4}")

list4.append(17)
print(f"List list4 after append-->{list4}")
print(f"List list1 after append-->{list1}")

list2 = [1,2,3,4]

list5 = list2.copy() # shallow copy
print(f"List list5-->{list5}")

list5.append(5)
print(f"List list5 after append-->{list5}")
print(f"List list2 after append-->{list2}")


# Covert list into string
print("\n============================")
print("05. Covert list into string")
print("============================")
list3 = ['apple', 'banana', 'cheery', 100, 500]

print(f"List to String--> {str(list3)}")

str1 = str(list3)
print(f"String--> {str1}")
print(f"Find l-->{str1.find('l')}")

# 06.Nested List
print("\n============================")
print("06.Nested List")
print("============================")

nlist1 = [[1,2,3], [4,5,6],[7,8,9]]
#list1 = [1,2,3]-->0, list3 = [4,5,6]-->1st, list3 = [7,8,9]-->2nd
print("Nest List : ", nlist1)
print("Print 1st number from 3rd list ", nlist1[2][0])
print("Print 2nd number from 2nd list ", nlist1[1][1])
print("Print 1st number from 1st list ", nlist1[0][0])
print("Print 2nd number from 1st list ", nlist1[0][1])