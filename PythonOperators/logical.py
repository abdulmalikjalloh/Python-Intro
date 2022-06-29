# Logical expression evaluate to tru or false
"Logical operators: and, or, not "


"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to """


num1 = 10
num2 = 5

print(num1 == num2)
print(num1 == 10)
print(num2 == 5)

#  and, or, not "
print("The and operator")
print(num1 == 10 and num2 == 5)
print(num1 == 10 and num2 == 50)


print("The or operator")
print(num1 == 10 or num2 == 5)
print(num1 == 10 or num2 == 50)
print(num1 == 15 or num2 == 50)

print("The not with and operator")
print(not (num1 == 10))
print(not (num1 == 10 and num2 == 5))
print(not (num1 == 10 and num2 == 50))

print("The not with or operator")

print(
    not (num1 == 10 or num2 == 5)
)  # num1 is not equal to 10 and num2 isnot equal to 5
print(not (num1 == 10 or num2 == 50))
