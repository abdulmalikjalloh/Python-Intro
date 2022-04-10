# Arithmetic Expression.

"Arithmetic expressions evaluates to a number, therefore uou must thing about BIDMAS(evaluated in order of precedence) when using it in python"

myNum1 = 100
myNum2 = 50
myNum3 = 111
myNum4 = 22
myNum5 = 2

"""-Arithmetic operators.
(+) plus operator.
(-) subtraction operator.
(\*) muliplication operator.
(/) division operator (anwer with remainder).
(//) floor division/ integer quotient operator (round the answer with no remainder).
(%) operator : mod/modulus (outputs the remainder ).
(\*\*) powers."""


print(f"use of the  plus operator: {myNum1} + {myNum2} = {myNum1 + myNum2}")


print(f"use of the  subtraction operator: {myNum1} - {myNum2} = {myNum1 -  myNum2}")

print(f"use of the  mulitiplication  operator: {myNum1} X {myNum2} = {myNum1 * myNum2}")

print(f"use of the Division operator: {myNum1} / {myNum2} = {myNum1 / myNum2}")

print(
    f"\nUse of the Floor Division operator: {myNum3} // {myNum4} rounded to = {myNum3 // myNum4}"
)

print(
    f"use of the Modulus/Mod operator: {myNum3} % {myNum4} remainder = {myNum3 % myNum4}"
)

print(f"use of the  power operator: {myNum5} power {myNum5} = {myNum5 ** myNum5}")

"""Logical expression evaluates to either True or False and used to control program flow(i.e the execution of the code based).
The three logical Operators are; and, or, not ".
Comparison Operators.
Use comparison operators to compare values.
(==) equal to.
(<)less than.
(>)greater than.
(<) less than or equal to.
(>=) greater than or equal to.
(!=) Not equal to."""

# Using the comparison operators
myNum1 = 12
myNum2 = 6

print(f"The value {myNum1} == {myNum2} evaluated to: {myNum1 == myNum2}")
print(f"The value {myNum1} > {myNum2} evaluated to: {myNum1 > myNum2}")

# Logical operators: and, or , not

print("Using the or operator")
print(
    f"The value {myNum1} equal to {8} or {myNum2} equal to {20} evaluated to: {myNum1 == 8 or myNum2 == 20}"
)
print(
    f"The value {myNum1} equal to {11} or {myNum2} equal to {5} evaluated to: {myNum1 == 11 or myNum2 == 5}"
)

print("Using the and operator")
print(
    f"The value {myNum1} equal to {8} and {myNum2} equal to {20} {myNum1 == 8 and myNum2 == 20}"
)
print(
    f"The value {myNum1} equal to {8} and {myNum2} equal to {15} {myNum1 == 8 and myNum2 == 15}"
)


print("Using the not operator")
print(f"The value {myNum1} not equal to {8}: {not (myNum1 == 8)}")
print(
    f"The value {myNum1} not equal to {8} and {myNum2} not equal to {20}: {not (myNum1 == 8 and myNum2 == 20)}"
)
print(
    f"The value {myNum1} not equal to {8} and {myNum2} not equal to {15}: {not (myNum1 == 8 and myNum2 == 15)}"
)
