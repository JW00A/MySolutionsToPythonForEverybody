nums = []

while True:
    user_input = input("Please enter a number(write done if you're done): ")
    if user_input == 'done':
        break

    try:
        int_input = float(user_input)
        nums.append(int_input)
    except:
        print('Please enter a number!')

if len(nums) > 0:
    print(f'Maximum: {max(nums)}')
    print(f'Minimum: {min(nums)}')