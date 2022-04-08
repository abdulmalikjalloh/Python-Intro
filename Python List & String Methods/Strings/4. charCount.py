pLanguage = "Python shoul be your first programming language"  # string to search
counter = 0  # flag variable initialise to 0
searchChar = input(
    "Enter letter to search for: "
)  # promt to enter search string or char

for char in pLanguage:  # iterates through the search string
    # print(char)

    if char == searchChar:  # compare user entered string or with string in pLanguage
        #   0    =  0 + 1(1), 1 = 1 + 1(2), 2 = 2 + 1 (3)
        counter = counter + 1  # inncrease the count of a charcter if found
print(f"The {char} character appears {counter} times in the sentence {pLanguage}")
