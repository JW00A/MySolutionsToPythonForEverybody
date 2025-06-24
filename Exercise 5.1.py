list_of_vals = []

while True:
    user_input = input('Enter a number: ')
    
    if user_input == 'done':
        break
    else:
        try:
            int_val = int(user_input)
            list_of_vals.append(int_val)
        except:
            print('Invalid input')

sum_of_vals = sum(list_of_vals)
len_of_vals = len(list_of_vals)
print(sum_of_vals, len_of_vals, sum_of_vals/len_of_vals)