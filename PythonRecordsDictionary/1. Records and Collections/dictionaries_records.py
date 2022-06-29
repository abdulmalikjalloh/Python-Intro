# A record is a static data structure. You must determine the attributes and the data
# types for each entity # during declaration. These will then be fixed for each record
# used in the database. Python does not have # a native data structure for a record.
# data structure called a dictionary to represent a record.  A # dictionary has some of
# the features of a record. # A dictionary has key value pairs and is mutable in nature.
# We use curly brackets to declare a dictionary

# dictionary in python is a collection of records
# create a record
dict1 = {1: "Jenny"}  # is a record (in a dictionary)

dict2 = {
    1: "Anna",
    2: "Paul",
    3: "Lucy",
    4: "James",
}  # create a dictionary with four records

print(dict2)  # print records from the dictionary

print(dict2[2])  # print a specifi record from the dictorary based on the key

print(dict2.items())  # print all recors using the items method

courses = {"course1": "Python", "course2": "CSS", "course3": "HTML", "course4": "JS"}

print(courses["course2"])  # print using a key that is of string datatype

# print using the keys method
dkeys = dict2.keys()  # access the keys and pass it to a variable dkeys
print("My nnnn", dkeys)
for aKey in dkeys:
    print(aKey)


# print using the values method
dValues = dict2.values()  # access the values and pass it to a variable dValues
for aValue in dValues:
    print(aValue)
