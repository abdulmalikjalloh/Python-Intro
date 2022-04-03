"1. Sequence : in python is the execution of code in the order in which it was written"
# Comments are written in single quotes '', double quotes "" or hash tag #. in fact these # lines are commented out with #.

"""Therefore, the python interpreter would not print any commented code in the terminal. However, print statements below on from line 7 with their respective strings wrapped
in quotes will be printed in the order they were written...that print from line 7 followeed by the next line...and so on"""

print(
    "Welcome to the Python Diaries series"
)  # The character wrapped in "quotes" inside this print function are interpreted as string(text)
print("Session 1: Intro to python epsiode 1")

"The code below output the answer to 12 + 22 "
print(
    12 + 22
)  # The + operator in this instance is used to perform addition between two numbers


# Below I have format the output using f-strings.
# See the real python documention on the link below on f-string for further reading
# https://realpython.com/python-f-strings/
print(f"The answer to {12} + {22} = {12+22}")
print(
    f"The answer to {12} + {22}\n = {12+22}"
)  # The backslash and n (\n) is used to print the output on a new line
