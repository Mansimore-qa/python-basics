# Data Type - Dictionary - collection of items in particular order,
# which can be same or different data type, and it is having keys and vales


#01. Dictionary
print("01. Dictionary")
dict1 = {"name" : "Rahul", "age": 36, "city": "Pune"}
print(f"print dict1-->{dict1}")
print(f" Data type of dict1---> {type(dict1)}")
#keys --> "name", "age", "city"
#Values --> "rahul, "36", "Pune"

#02. Dictionary examples
print("02. Dictionary examples and operations")
dict2 = {"apple" : "red", "banana" : "yellow", "cheery": "dark red", "orange" : "orange" }
print(f"print dict2-->{dict2}")
dict3 = {1: "credence", 2: "Automation Testing", 3: "Python", 4: "selenium"}
print(f"print dict3-->{dict3}")

#03. Dictionary Accessing
print("03. Dictionary Accessing")
print(f"accessing the value form key-->{dict2["apple"]}")
print(f"accessing the value form key-->{dict2["banana"]}")
print(f"accessing the value form key-->{dict3[1]}")

# update the value in dict
dict2["banana"] ="black"
print(f"accessing the value form key banana-->{dict2["banana"]}")

dict3[1] ="Credence Institute"
print(f"accessing the value form key banana-->{dict3[1]}")
print(f"print dict3-->{dict3}")

# here we have added the new key and value in existing dict
dict3[5] ="API Automation"
print(f"print dict3 after adding the key 5-->{dict3}")

# To remove specific key
del dict3[5]
print(f"print dict3 after deleteing the key 5 -->{dict3}")

print(f"Display all keys of dict2-->{dict2.keys()}")
print(f"Display all keys of dict3->{dict3.keys()}")
print(f"Display all items of dict2->{dict2.items()}")
print(f"Display all items of dict3->{dict3.items()}")
print(f"Display all values of dict2->{dict2.values()}")
print(f"Display all values of dict3->{dict3.values()}")
dict1.clear()
print(f"Clear dict1->{dict1}")
print(f"get value from key dict2->{dict2.get("apple")}")

# membership
print("name" in dict2) # false
print("apple" in dict2) # true

# length
print(f"length of dict2 --> {len(dict2)}")
print(f"length of dict3 --> {len(dict3)}")
dict2.pop("orange")
print(f"length of dict2 --> {len(dict2)}")
print(f"print of dict2 --> {(dict2)}")