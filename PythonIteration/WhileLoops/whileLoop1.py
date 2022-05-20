# Iteration means repetitions
# While loop: keeps looping until a condition is met

"Ask for user input and convert  the input to lower case characters"
userGuess = input("Enter your guess word: ").lower()

while userGuess != "python":
    # "ask for user input again while the condition is not met"
    userGuess = input("Try Again: ").lower()

print(f"You have correcTly guessed {userGuess}")
