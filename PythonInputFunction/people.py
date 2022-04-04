# method1  Ask user to enter their name using the print function
print("Enter your first name? ")
pFname = input()  # the input function is initialised with the pFname variable
print(f"{pFname} is your firstname")

# method2  asking user for input using the input function
pLname = input("Now, enter your last name? ")
print(f"{pFname} {pLname}, you have completed registration")
# using the + operator to concatenate: join together
print("Your fullname is " + pFname + " " + pLname)
print("Your fullname is ", pFname, pLname)
