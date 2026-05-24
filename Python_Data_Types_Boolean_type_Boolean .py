# Data Type - Boolean  is data type which is either true or false.

#01 Boolean
print("01 Boolean")
bool1 = True
bool2 = False
print(f"boo1 type-->{type(bool1)}, bool2 type-->{type(bool2)}")

#02 Boolean- Example and operations
print("02  Boolean- Example and operations")
bool1 = True
bool2 = False

print(f"bool1 and bool2--> {bool1 and bool2}") # for AND--> both conditions should be true
print(f"bool1 or bool2--> {bool1 or bool2}") # for Or--> any one condition should be true
print(f" not bool1-> {not bool1}")   #true--> false, false--> true
print(f" not bool1-> {not bool2}")

# all and any

# all --> returns true if all items in list is true.
# any --> returns true if any item in list is true.


print(all([True, False, True, True])) # False
print(all([True, True, True, True])) # True

print(any([True, False, True, True])) # True
print(any([True, True, True, True])) # True
print(any([False, False, False, False])) # False


print(f"any empty string-->{bool("")}") # False
print(f"any non empty string-->{bool("Credence")}") # True
print(f"for value 1 ->{bool(1)}") # True
print(f"for value -2 ->{bool(-2)}") # True
print(f"for value 0 ->{bool(0)}") # False for 0--> False and for any other value --> True