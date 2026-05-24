# Data Type -  Set
# Set is unordered collection of items.
# Set is mutable.
# Set is un-indexed.


#01 Set
print("\n#01 Set")

set1 = {'banana',2,3,4,5,6,6,6, True, "apple", "Credence is best", False, True}
print(f"print set1 -->{set1}")
print("The data of set1 is", type(set1))


#02. Set example
print("\n==========================")
print("02.  Set example")
print("============================")
set1 = {1,2,3,4,5,5,56,7,7,7}
set2 = {'apple', "banana", "cherry"}
set3 = {True, False, True}
set4 = {1,2,3,4,4, True, False, "apple", "banana", "cherry", "credence"}
print(f"print set1 -->{set1}")
print(f"print set2 -->{set2}")
print(f"print set3 -->{set3}")
print(f"print set4 -->{set4}")




#03. Set operations
print("\n==========================")
print("03.  Set operations")
print("============================")

set5 = {1,2,3,4}

set5.add(5)
print(f" print set5 after adding 5 value {set5}")

set5.remove(5)
print(f" print set5 after removing 5 value {set5}")

set5.discard(4)
print(f" print set5 after discard 4 value {set5}")

########################################
# set5.remove(10) # will show an error if the value is not in set.
# print(f" print set5 after removing 5 value {set5}")

set5.discard(10) # remove value in set # wont throw any error if value is not in set
print(f" print set5 after discard 10 value {set5}")
#######################################

set5.clear()
print(f" print set5 after clearing {set5}")





#04. Set- advance operations
print("\n==========================")
print("04.  Set - advance operations")
print("============================")

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = {9,10,11}
set4 = {9,10,11}
set5 = {1,2,3,4,5,6,7,8, 9,10,11}

print("Union of set1 and set2 :", set1.union(set2)) # output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Intersection of set1 and set2 :", set1.intersection(set2)) # output: {4, 5}
print("Difference of set1 and set2 :", set1.difference(set2)) # {1, 2, 3} only the values in set1, not common value with set 2 and not in set 2
print("Difference of set2 and set1 :", set2.difference(set1)) # {8, 6, 7} only the values in set2, not common value wih set 1 and not in set 1
print("symmetric_difference of set1 and set2 :", set2.symmetric_difference(set1)) #  # output: {1, 2, 3, 6, 7, 8}
print("=============================================================================")

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = {9,10,11}
set4 = {9,10,11}
set5 = {1,2,3,4,5,6,7,8, 9,10,11}

print("==============================isdisjoint=========================================")
print("Isdisjoint of set1 and set2 :", set1.isdisjoint(set2)) # output:False,  (true if no common values between 2 sets.)
print("Isdisjoint of set1 and set3 :", set1.isdisjoint(set3)) # output:True,  (true if no common values between 2 sets.)
print("==============================issubset=========================================")
print("issubset of set1 and set2 :", set1.issubset(set3)) # output: False
print("issubset of set1 and set5 :", set1.issubset(set5)) # output: True
print("issubset of set2 and set5 :", set2.issubset(set5)) # output: True
print("issubset of set3 and set5 :", set3.issubset(set5)) # output: True
print("==============================issuperset=========================================")
print("issuperset of set3 and set5 :", set3.issuperset(set5)) # output: False
print("issuperset of set3 and set4 :", set3.issuperset(set4)) # output: True


# 05. Frozen Set
print("\n==========================")
print("05. Frozen Set (immutable)")
print("============================")

fset1 = frozenset({1,2,3,"apple"})
print(f" frozen set print --> {fset1}")

#fset1.add(6) # AttributeError: 'frozenset' object has no attribute 'add'
#fset1.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'


# 05. Covert list to  Set
print("\n==========================")
print("05. Covert list to  Set")
print("============================")
list1 = [1,2,3, "apple"]
set1 = set(list1)
print("print the converted list", set1)
print(type(set1))


# 06. Covert tuple to  Set
print("\n==========================")
print("05. Covert list to  Set")
print("============================")
tuple1 = (1,2,3, "apple")
set1 = set(tuple1)
print("print the converted list", set1)
print(type(set1))

set1={1,2,3,4, "apple"}
tuple1 = tuple(set1)
list1 = list(set1)
print(tuple1)
print(list1)


