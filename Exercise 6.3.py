def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

userInputString = input('Enter a string: ')
userInputLetter = input('Enter a letter: ')
print(f"The number of ({userInputLetter})'s in the string is: " + str(count(userInputString, userInputLetter)))