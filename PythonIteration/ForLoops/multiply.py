"Create a multiplication table based on user input"
num1 = int(input("Enter number for mulplication table: "))
#       start at number1 , end at 16(16-1)
for num2 in range(1, 13):
    # num multiply by num2
    print(f"{num1} x {num2} = {num1 * num2} ")
