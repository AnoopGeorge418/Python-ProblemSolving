num = int(input('Number: '))

flag = 0
for i in range(1, num):
    if num % i == 0:
        flag = 1
        break

if flag == 1:
    print(f'{num} is not a prime number')
else:
    print(f'{num} is a prime number')
