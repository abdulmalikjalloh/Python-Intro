# Python Data Types

"""Data types are variables used to reserve memory space.
In python programming an explicit varaiable initialisation is not required to reserve memory space. This 
happens automatically when you initialised a value to a variable."""

# String datatype
fName1 = "Issa"  # implicit datatype as value is wrapped in quotation, therefore python interprete it as a string
fName2 = "Mariam"
fName3 = ""  # Implicit data type with no value
stringVal1 = """
This string of text is reference with the stringVal1 variable
This string of text is reference with the stringVal1 variable
This string of text is reference with the stringVal1 variable
This string of text is reference with the stringVal1 variable
"""
stringVal2 = ""

# Multiline comment
"""
This is a multiline comment that is not initialised with a variable.Therefore, will not be printed in the terminal 
This is a multiline comment that is not initialised with a variable.Therefore, will not be printed in the terminal
This is a multiline comment that is not initialised with a variable.Therefore, will not be printed in the terminal
This is a multiline comment that is not initialised with a variable.Therefore, will not be printed in the terminal
"""
# Single line comment
"This is a single line comment not initialised with a variable. Therefore, will not be printed in the terminal"

"To check the datatype for a variable, use the the type class object in the print statement as shown below"
print(type(fName1))
print(type(fName2))
print(type(fName3))
print(type(stringVal1))

"Boolean datatype: True/False , Yes/No"
myBoolVal1 = True
myBoolVal2 = False

print(type(myBoolVal1))
print(type(myBoolVal2))

"Numeric data types"
number1 = 102  # int datatype
number2 = 103.6  # float datatype
print(type(number1))
print(type(number2))
