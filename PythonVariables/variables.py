# Variable naming convention
"Variable naming convention: Be mindful that variables are case sensitive"
username = "Musa21"  # use meaningful name
userName = "Abu24"  # camel case/notation
user_name = "alphaK345"  # use snake case/ uderscore between two words
username1 = "aMalik23"
firstName = "Fatima"  # single quotes can also be use for string values
userAge = 23

"""The use of capital letters in variable initialisation indicates that this variable will be  treated as 
constant(its value cannot be changed), this is  a work around as python doesn't natively support constant"""
AGE = 12

"The examples below does not follow the python naming conventionon't do this"
# £money or $money = 102 # don't use symbols at the start of your variable names
# User = "Kadija" # no caps at start of varaible names
# user name = "Sara" # no spaces between a varable name
# 1user = "Ibrahim" #  don't start variable names with a number


# Variable Initialisation
"""
num1 is a variable that is initialised with the value 101. As 101 is a numeric value, meaningful idenifier
has been used in this  variable initialisation. """
# Initialisation is when a variable is assinged an initial value
#

num1 = 101
num2 = 30

fullName = "Musa Kamara"  # fullName declared as a variable and initialised with a string value "Musa Kamara"

"""In the above Initialisation, the datatype for each variable wasn't set. This is because 
datatype in python is implicit when the variable is initialise, num1 is initialised with an integer data type
and fullName is is initialised with a string datatype"""


print(f"The answer to {num1} + {num2} = {num1 + num2}")

print(f"Welcome {fullName} to programming in python")

" formating output without f-string"
print("Hello ", fullName, "you are", num2, "years old")

# Variable Assignment
"Is when the value of a variable is changed at the memory location"
num3 = 20  # Varaible initialisation

num3 = 36  # The value held in the memory location num3 has been mdofied from 20 to 36


"To check the datatype for a variable, use the the type class object in the print statement as shown below"
print(type(num1))
print(type(num2))
print(type(fullName))


"""casting is a method used to convert one data type to another str(num2). In the print statement below the
 num2 variable is of type integer. However, it is now been casted/converted as a string value so it can be printed 
 without any errors. Also, the + operator in the print statement is used in this instance to concatenate (join together)"""

print("Hello " + fullName + " you are now " + str(num2) + " years old")
num2 = 50
total = num1 + num2
print(f"The total {total} ")
