# Add items from two list using their index position: index =  0 1 2 3 4 5 6 7 8 9 "

numList1 = [2, 20, 12, 20, 3, 4]

numList2 = [3, 4, 5, 6, 7, 23]

numList1_2 = [numList1[i] + numList2[i] for i in range(len(numList1))]
print(numList1_2)


# join two lists using the + operator
numList1 = [2, 20, 12, 20, 3, 4]

numList2 = [3, 4, 5, 6, 7, 23]

joineLists = numList1 + numList2

print(joineLists)

# find common names in two different list
myListOfNames1 = ["Abu", "Uthman", "Daud", "Adam", "Bilal", "Abdul", "Nur"]
myListOfNames2 = ["Abubakarr", "Umar", "Gibril", "Adam", "Issa", "Abdul"]

commonNames = [pNames for pNames in myListOfNames1 if pNames in myListOfNames2]
print(commonNames)

# find common numbers in two different list
numList1 = [2, 20, 12, 20, 3, 4]
numList2 = [3, 4, 5, 6, 7, 23]
commonNums = [nums for nums in numList1 if nums in numList1]
print(commonNums)

# Search trhough list to find a name
myListOfNames3 = [
    "Abu",
    "Uthman",
    "Daud",
    "Bilal",
    "Abdul",
    "Nur",
    "Abubakarr",
    "Umar",
    "Gibril",
    "Adam",
    "Issa",
]

findName1 = input("Enter a name to search for")

nameInList = [
    name for name in myListOfNames3 if findName1 in myListOfNames3 and findName1 == name
]
print(f"Found {findName1}")


findName2 = input("Enter a name to search for")
for name in nameInList:
    if name == findName2:
        print(f"Found {findName2}")
        break
else:
    print(f"Not Found {findName2}")

# in multidimentional items in the list are counted from left to right
# and the the lists are counted from top to bottom
twoDList = [
    ["Abu", "Uthman", "Daud", "Adam", "Bilal", "Abdul", "Nur"],
    [2, 20, 12, 20, 3, 4, 5],
    [3, 4, 5, 60, 70, 23, 78],
    ["Abubakarr", "Umar", "Gibril", "Adam", "Issa", "Musa", "Kareem"],
]
print(twoDList[0][2])
print(twoDList[0][1])
print(twoDList[0][4])
print(twoDList[1][2])
print(twoDList[1][5])
print(twoDList[2][3])
