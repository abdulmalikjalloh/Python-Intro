s1 = "Python is a programming language"  # string
s2 = "Python is my first programming language"  # string
s3 = """Writing program in python is great, 
and it is my first programming language 
"""
s4 = " How are you doing in python programming "

# Characters access and printed by index
print(s1[10], s2[16], s3[14])

# Return the length of the string
print(len(s3))

# Slice string using indexes
print(s1[5:12])  # Use start and end index
print(s1[5:])  # Use start index and no end index
print(s1[5:-1])  # Use start index and negative end index
print(s1[-2:-1])  # Use negative start and end index
print(s1[5:-2])  # Use start index and negative end index
print(s1[:])  # Use no start index or end index specified

# print by index using steps
s5 = "Beautiful"
print(s5)
print(
    s5[1:9:2]
)  # Use start and end index and step value( to print every second character)
print(s3)
print(
    s3[1::2]
)  # Use start and end index and step value(to print every second character)

# Strip string of whitespace from string of characters
print(s4)
print(s4.lstrip())  # lstrip strips white spaces on the left(start of string)
print(s4.rstrip())  # rstrip strips white spaces on the right(end of string)
print(s4.strip())  # strip  strips white spaces on the left and(start and end of string)


# Use the count method to count a specific character
print(s3.count("a"))

# Use of  upper, lower and title methods to convert to upper, lower and title cases
print("Upper case", s4.upper())
print("Lower case", s4.lower())
print("Title case", s4.title())

# Use the replace method to replace the one substring with a another substring
print(s4.replace("How", "What"))
