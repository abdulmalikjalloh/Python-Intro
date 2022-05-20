# Iteration means repetitions
# While loop: keeps looping until a condition is met

"Ask for user input and convert  the input to lower case characters"
userGuess = input("Enter your guess word: ").lower()
guessAttempts = 1  # flag variable

"using the 'and' operator ensure that both condition has to be met"
while userGuess != "python" and guessAttempts < 3:
    # "ask for user input again while the condition is not met, with the number of attempted guess(es)"
    userGuess = input(f"Try Again: You have used {guessAttempts} / 3 attempts ").lower()
    guessAttempts += 1  # increment guessAttempts by  1

# This condition will be executed if the user guessed correctly before the exhausting all three attempts
if userGuess == "python":
    print(f"You have correctly guessed {userGuess}")
else:
    # This block of code will be  executed if all guesses have been exhausted
    print(f"You now used {guessAttempts} / 3 attempts | No more guess left ")
