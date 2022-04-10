"Select is used to control the flow of program using if and else to ensure a block of code is executed if the condition is true else not true."

# Comparison operator compare values
# == equal

print(" What is your favourite sport? ")
favSport = input()
compFav = "Football"
if favSport == compFav:  #  if this condition is true(met) do something.
    print(f"Good choice, {favSport} is a great sport")
else:  # else do something different.
    print(
        "Would have been nice if {favSport} is your favourite sport instead of {compFav}"
    )
