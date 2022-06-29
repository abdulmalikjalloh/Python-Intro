# declarae a dictionary with key value pairs 
userDetails = {"fullName": "Anna Doe", "Course":"Bootcamp", "Module":"Python"}
# declarae a dictionary with key only 
userDetails1 = {"fullName":"", "Course":"", "Module":""}

# use the input() to dynamically add values to the dictionary with their respective keys 
userDetails1["fullName"] = input("Enter your fullname: ")
userDetails1["Course"] = input("Enter Course: ")
userDetails1["Module"] = input("Enter Module: ")
print(userDetails1)
"""
Task Create a record
Use the dictionary data structure to create a record for a film
Your record should have at least three attributes. 
Movie title, Actor(s), Realease Date
Test your dictionary by printing it."""
#Solution
movie = {"Title": "", "Actor": "", "Release Date": ""}
movie["Title"] = input("Enter the title: ")
movie["Actor"] = input("Enter the main actor: ")
movie["Release Date"] = input("Enter the release date: ")

# use the input() to dynamically add key value pairs to an empty dictionary 
userDetails2 = {} # declare an initialize an empty dictionary
userDetails2Key = input("Enter key: ") #dynamically ask for a key
userDetails2[userDetails2Key] = input("Enter yur fullname: ") # we ask for value and assign it to a key
print(userDetails2)