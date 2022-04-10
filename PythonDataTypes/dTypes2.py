# Python Data Types

"""Data types are variables used to reserve memory space.
In python programming an explicit varaiable initialisation is not required to reserve memory space. This 
happens automatically when you initialised a value to a variable."""
"""
List is a flexible data type that can contain items with one or more data types in an ordered sequence, which
can also be modify."""
# Initialise a list called myList with values that are of different data types using square braces
myList = [10, 20, 40, 50, 102.5, "Karim", 50, 102.5, "Amina"]
print(type(myList))
print(myList)  # prints all items in the list
print(myList[3])  # print item by index postion

"""
 Tuple is similar to list in python as items can be accessed by index
 because it stores items as an ordered list. Hpwever, it is faster than
 list and used to create write protect data, but items cannot be modify
"""

# Initialise a tuples myTpl1 and myTpl2 with values that are of different data types using parethesis
myTpl1 = (10, 20, 40, 50, 102.5, "Karim", 50, 102.5, "Amina")
myTpl2 = (
    "Tuple2",
)  # a tuple must be initialised with one comma even if it only contains one item

print(type(myTpl1))
print(type(myTpl2))
print(myTpl2)
print(myTpl1[3])
"""
Unlike list and tuple, set is collection of items that are not in order and cannot be accessed
via index. Also, duplicate items initialised in a set are eliminated. 
"""

# declare a set an assign diffrent dattypes
mySet = {10, 20, 40, 50, 102.5, "Karim", 50, 102.5, "Amina"}
print(type(mySet))
print(mySet)  # print all items in a set
# print(set1[3]) # items in a set cannot be access by index as it is an unordered data type

# In dictionary, data is store as key value pairs
# The key is used to retrieve a value
"              key:value"
myDictionary = {1: "Hawa", 2: "Shaffique", "name": "Sudais"}
print(type(myDictionary))
print(myDictionary)
print(myDictionary["name"])
