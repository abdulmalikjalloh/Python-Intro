# sets are used to store multiple items in a single variable..
# Set Items: Set items are unordered and declared in curly brackets,
#  unchangeable, and do not allow duplicate values.
set1 = {410,132,4,2,40,12,34,20} #declare a set with curly braces and assign values to it 

print(set1)

set1.update([9,10,12,15]) # update a set : we mean add more items to the set

print(f" Print after update {set1}")

# freeze a set by using the frozenset 
fset1 = frozenset(set1)
print(f" This set is frozen {fset1}")


# fset1.update([1,23,34,4455,55])  you can't update a frozen
set2 = {1,23,34,4455,55, "Anna", "Lucy", 12.8}
print(set2)