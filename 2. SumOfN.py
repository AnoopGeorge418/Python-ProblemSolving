# step 1: Ask input from the user as a number  - which user wants summ of
# do a loop with range() function from 1 to user input + 1 - to get upto user input from 1
# add each number from 1 to user input and print it as a sum 
# ex: user input = 5, output = 1 + 2 + 3 + 4 + 5 = 15

num = int(input('Enter the number: '))

total = 0
for i in range(1, num + 1):
    total += i

print(f'Sum of {num} is: {total}')