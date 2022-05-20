from random import randint

num = 1  # int(input("Enter a number: "))
" num(5) is the start value <= 20(is the end value)"
while num <= 20:  # set a condition which uses a value to count to
    print(num)  # print the value num

    randNum2 = randint(1, 100)
    # print(randNum2)

    if num == randNum2:  # set a condition
        break  # break out of the loop as per the condition set
    num += 1  # increment num value by 1
