"""This is when an if/else block(selection) is place inside another if/else block(selection).
  Nested if only"""
learnerAge = int(input("Enter learner's age: "))
compAge = 16
compCode = "Python"
if learnerAge > compAge:  # compare the learnerAge with compAge
    passCode = input("Enter learner code")
    # The if below is nested in the first if block above and will only execute if the first if condition is true
    if passCode == compCode:  # check if passCode equal to compCodeme
        print(f"{passCode} valid. Access granted")
print("closing")
