"""This is when an if/else block(selection) is place inside another if/else block(selection).
  Nested if only"""

learner = input("Enter learner name: ")
pythonScore = float(input("Enter your python score: "))
htmlScore = float(input("Enter your HTML score: "))
mySqlScore = float(input("Enter your SQL score: "))

if pythonScore < 45:
    print(f"{learner}, try again in python {pythonScore}")
elif htmlScore < 45:
    print(f"{learner}, try again in HTML {htmlScore}")
elif mySqlScore < 45:
    print(f"{learner}, try again in SQL {mySqlScore}")

else:  # The if blocks are nested in the else below and will be executed based on the average score
    averageGrade = (pythonScore + htmlScore + mySqlScore) / 3
    if averageGrade <= 55:
        print(f"{learner}, your score is {averageGrade} and is Grade C ")
    if averageGrade <= 79:
        print(f"{learner}, your score is {averageGrade} and is Grade B")
    if averageGrade <= 89:
        print(f"{learner}, yourour score is {averageGrade} and is Grade B ")
