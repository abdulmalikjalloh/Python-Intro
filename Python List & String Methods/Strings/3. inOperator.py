months = "There are 12 months in year"

if "in" in months:
    print("Found")
else:
    print("Not Found")


user1 = "Bilal"
if "a" in user1 or "e" in user1 or "i" in user1 or "o" in user1 or "u" in user1:
    print("found")
else:
    print("not found")


user2 = "Ahmed"
letters = ["a", "o", "i", "e", "u"]

for aLetter in letters:
    # print(aLetter)
    if aLetter in user2:
        print(f"{aLetter} found")
    else:
        print(f"Not found {aLetter}")
