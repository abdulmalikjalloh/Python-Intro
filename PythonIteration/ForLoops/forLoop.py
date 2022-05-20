# To put simply iteration means repetition, python uses the for and while loops for repetition.
# For Loop is used when the number of iteration is known.

"""
The for loop takes number as a variable which will hold the initial value of 0.
The variable number will then be re-assigned the values 1,2,3,4,5,6,7..14
15 is excluded as the value initialisation started at zero(0) technically 0 -14
that is 15 iterations 

"""
for number in range(15):  # in the range we specify the number of iterations(15)
    print(number)

"""Specifying the start ensure the iteration/count can start at the specified start value and stop at the 
specified stop value"""
print("start and stop")
#                (start,end)
for number in range(5, 15):  # in the range we specify the start and stop
    print(number)

"using the step specifies the increment (or decrement) value"
print("start, stop, step")
#                (start,end,step)
for number in range(
    5, 150, 10
):  # in the range we specify the start, stop and step values
    print(number)

"To count down use the - operator on the step value as shown below"
print("solution")
print("Start, end and decrement value ")
#                   start/end values
for number in range(100, 2, -10):
    print(number)
