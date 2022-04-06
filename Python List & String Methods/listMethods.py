# declare a myListNames1 variable and initialised it with values of different datatypes

myListOfNames1 = []
print(myListOfNames1)
"index:     0  , 1"
myListOfNames2 = ["Abu", "Umar"]
print(type(myListOfNames1))
print(myListOfNames2)
# To insert item in a list use insert function, followed by the position to insert the item and the item to be inserted
"          index position, value"
myListOfNames2.insert(0, "Nur")
print(myListOfNames2)

# Append items to the end of myListOfNames
myListOfNames2.append("Daud")
myListOfNames2.append("Adam")
myListOfNames2.append("Issa")
myListOfNames2.append("Abdul")
print(myListOfNames2)

# Access myListOfNames items by index position
"index:   0,      1,     2,      3,      4,       5,      6   "
#        [Nur', 'Abu', 'Umar', 'Daud', 'Adam', 'Issa', 'Abdul']
print(myListOfNames2[2])
print(myListOfNames2[3])

# Return the length of the list
print(f"The list length is {len(myListOfNames2)} ")

# Slice myListOfNames using indexes
" start slice : end slice"
"index:   0,      1,      2,    3,     4,       5        6"
#      ['SDLC', 'HTML', 'CSS', 'JS', 'myListOfSQL', 'NoSQL', 'Python']
print(myListOfNames2[2:5])  # ( Start and end index position of items)
print(myListOfNames2[2:6])  # ( Start and end index position of items)
print(myListOfNames2[2:7])  # ( Start and end index position of items)
print(myListOfNames2[6])  # ( Start and end index position of items)
print(myListOfNames2)
# delete an item from myListOfNames by index position
del myListOfNames2[1]
print(myListOfNames2)

# delete/remove an item from the myListOfNames by value
myListOfNames2.remove("Nur")
print(myListOfNames2)

myListOfNums = [11, 1, -4, 2.6, 0, 10, 2]
# Find the min and max value in a list by using the min/max method n
print(f"This is the min number from the list  {min(myListOfNums)}")
print(f"This is the min number from the list  {max(myListOfNums)}")

# How to sort items in a lists
myListOfNums.sort()
print(f"List is in ascending order {myListOfNums}")


myListOfNums.sort(reverse=True)
print(f"List is in descending order {myListOfNums}")

# clear all items in a myList
myListOfNums.clear()
print(f"List is cleared {myListOfNums}")
