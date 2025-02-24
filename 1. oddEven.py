# 1, 3, 5, 7, 9, 11 are considered to be odd numbers
# 2, 4, 6, 8, 10 are considered to be even numbers

# step 1: get the user input as a number
# step 2: if given number gives a reminder of 0
# step 3: print It is a Even number.
# step 4: if given number does not gives a reminder of 0
# step 5: print It is a Odd number.

num = int(input('Enter a number to check: '))

if num % 2 == 0:
    print("It's Even Number")
else:
    print("It's Odd number")