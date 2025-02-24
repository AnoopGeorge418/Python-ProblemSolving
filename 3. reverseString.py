# step 1: get the input from the user as string
# step 2: reverse the string
# print the revered output

userInput = input('Input here: ')
reversedInput = userInput[::-1]

print(reversedInput)


# 2nd way 
# 1. convert the user input to a list
# 2. apply reversed method to it
# 3. take out of the list 
# 4. print the output

userInput = input('Input here: ')

# converting user input to a list
convertingToList = list(userInput)
# reversing the list
convertingToList.reverse()

# converting the list into normal input in reversed format
reversedInput = ' '.join(convertingToList)

print(reversedInput)