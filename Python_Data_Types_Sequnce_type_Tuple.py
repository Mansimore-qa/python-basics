# Data Type -  Tuple

# Tuple is collect of items in a particular order,
# which can be of same or difference data types.
# ALl operators are similar with list, but it is immutable. (cannot change anything once placed in tuple)

print("Sunday session 7am to 10:30am, 1s half new topic, 2nd revision")
print("Admission date : 24, 25 Dec")
print("Working candidate meet up 3rd Jan")
print("Non-working, Candidate meet up 29th dec to 2nd Jan (10:30 am to 7:00pm --> Offline workshop, Katraj, Pune")

#01. Tuple
print("\n==========================")
print("01. Tuple")
print("============================")
tuple1 = (1,2,3,4,5)
print(f"tuple1--> {tuple1}")
print(f" The data type of tuple1 is {type(tuple1)}")


#02. Tuple examples
print("\n==========================")
print(" Tuple examples")
print("============================")

tuple1 = (1,2,3,4,5, 5.5)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (True, False, True)
tuple4 = ("apple", 1, True )

print(f"Tuple1-->{tuple1}")
print(f"Tuple2-->{tuple2}")
print(f"Tuple3-->{tuple3}")
print(f"Tuple4-->{tuple4}")

print(f"Len tuple1 ->{len(tuple1)}")

'''
tuple1.append(6)
print(f"append 6 in list1 -->{tuple1}")

tuple1.insert(2,5)
print(f"insert 5 at index 2 in list1 -->{tuple1}")

tuple1.remove(5.5) # removes the specific value
print(f"remove 5.5 from list1 -->{tuple1}")

tuple1.pop(3) # index 3 --> 2 will be removed from list, via pop we can pop value at specific index
print(f"pop at 3rd index from list1 -->{tuple1}")

tuple1.pop()
print(f"pop()--> last value from list1 -->{tuple1}")

tuple1.extend([6,7,8,9,10,11,12,13,14])
print(f"extend the list1 with new values -->{tuple1}")
'''

#02. Tuple Operations
print("\n==========================")
print("02. Tuple Operations")
print("============================")
print(f"Count of 'apple' in tuple2 :{tuple2.count('apple')}")
print(f"Count of 3 in tuple1 :{tuple1.count(3)}")
print(f"Count of 1 in tuple1 :{tuple1.count(1)}")
print(f"Value at 2nd index of tuple2-->{tuple2[2]}")
print(f"Value at -1 index of tuple2-->{tuple2[-1]}")
print(f"Value at -1 index of tuple2-->{tuple2[-1]}")
print(f"Slice of tuple2-->{tuple2[3:5]}")
print(f"Slice of tuple2-->{tuple2[6:]}")
print(f"Slice of tuple2-->{tuple2[-2:]}")
print(f"Slice of tuple2-->{tuple2[7:]}")
print(f"Slice of tuple2-->{tuple2[-1:]}")
print(f"Slice of tuple2-->{tuple2[:]}") # whole tuple
print(f"Slice of tuple2-->{tuple2[:2]}") # stop at index 2
print(f"Slice of tuple2-->{tuple2[::2]}") # stepping same you can use for string also.
print(f"Reverse the tuple1 {tuple1[::-1]}") # reverse the tuple
print(f"Reverse the tuple2 {tuple2[::-1]}") # reverse the tuple
print(f"Index the tuple2 {tuple2.index('apple')}")



#03. Tuple to list, list to tuple, tuple to string, string tuple, tuple to int, float, int float to tuple.


# List
tuple2 = (1,2, 'apple', True)
# convert it into the list
list1 = list(tuple2)

list1.append(False)
print(f"List1 print-->{list1}")

conv_tuple1 = tuple(list1)

print(f"conv_tuple1 print-->{conv_tuple1}")


# String
tuple2 = (1,2, 'apple', True)
# convert it into the string
str1 = str(tuple2)
print(f"string print-->{str1}")


