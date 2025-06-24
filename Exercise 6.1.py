fruit = 'banana'
user_input = input('Do you want to enter custom fruit(default: banana) or anything else? (Yes or No) ')

if user_input == 'Yes' or user_input == 'yesy':
    fruit = input('Please enter something: ')
else:
    fruit = 'banana'

index = len(fruit) - 1
string = ''
while index >= 0:
    string += fruit[index]
    index -= 1

string += '\n'
index = 0
while index < len(fruit):
    string += fruit[index]
    index += 1

print(string)