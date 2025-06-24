list = []
while True:
    user_input = input('Enter a number: ')

    if user_input == 'done':
        break
    else:
        try:
            int_val = int(user_input)
            list.append(int_val)
        except:
            print('Invalid input')

total = sum(list)
length = len(list)
minimum = min(list)
maximum = max(list)
print(total, length, minimum, maximum)