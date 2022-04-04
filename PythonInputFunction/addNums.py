# input function: is used to capture user input
# The default datatype for the input function is string. Therefore, not string inut must be
# casted to their respective data type
myNum1 = int(input("Enter your first number: "))
myNum2 = int(input("Enter your second number: "))

sum = myNum1 + myNum2
print(f"The total of {myNum1} + {myNum2} = {sum}")
print(type(myNum1))
