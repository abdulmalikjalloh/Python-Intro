"""
- Is used to control the flow of program using if, elif and else 
to ensure a block of code is executed if the condition is true, 
elif another condition is true, else if none of the condition in 
the if and elif block is not true. Then else do something .

"""
# Comparison operator compare values
# = assignment operator
# >= greater than or equal to
learner = "Saeed"
learnerMark = int(input(f"Enter a mark for {learner}: "))

if learnerMark >= 85:  #  if this condition is true(met) do something (Assign grade B).
    learnerGrade = "A"
elif (
    learnerMark >= 70
):  # elif this condition is true(met) do something (Assign learnerGrade B)
    learnerGrade = "B"
elif (
    learnerMark >= 50
):  # elif this condition is true(met) do something (Assign learnerGrade C)
    learnerGrade = "C"
else:  # else this condition is true(met) do something (Assign learnerGrade F)
    learnerGrade = "F"
print(f"{learner}, your learnerGrade is {learnerGrade}")
