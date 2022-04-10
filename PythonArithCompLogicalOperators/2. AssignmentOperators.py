"The same value can be assigned to to multiple variables"
myNum1 = myNum2 = myNum3 = 12
print(
    f"The three variables myNum1, myNum2 and myNum3 assigned the same value {myNum1, myNum2, myNum3} "
)
# Python uses several compound operators, the compound assignment operator, add the value stored in the variable on the right
# to the value stored in the variable on the left, then assign the total value to the variable on the left.
"""The use of compound assignment a+=b """
myNum4, myNum5 = 11, 6
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")

myNum4 += myNum5  # compound assignment
print(
    f"This compound assignment add the the value in myNum4 and myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)

myNum4, myNum5 = 10, 5
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")
myNum4 -= myNum5  # compound assignment
print(
    f"This compound assignment subtracts the the value in myNum4 from myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)

myNum4, myNum5 = 13, 7
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")
myNum4 *= myNum5  # compound assignment
print(
    f"This compound assignment mulitiplies the the value in myNum4 and myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)


myNum4, myNum5 = 14, 2
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")
myNum4 /= myNum5  # compound assignment
print(
    f"This compound assignment divides the the value in myNum4 from myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)


myNum4, myNum5 = 9, 2
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")
myNum4 %= myNum5  # compound assignment
print(
    f"This compound assignment use the modulus to divide the the value in myNum4 from myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)

myNum4, myNum5 = 2, 3
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")
myNum4 **= myNum5  # compound assignment
print(
    f"This compound assignment find the power of the the value in myNum4 and myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)

myNum4, myNum5 = 15, 4
print(f"The value held in myNum4 and myNum5 are {myNum4} and {myNum5} respectively")
myNum4 //= myNum5  # compound assignment
print(
    f"This compound assignment use the floor division to dive the the value in myNum4 from myNum5 and stored it in myNum4 variable using the compund assignment {myNum4}"
)
