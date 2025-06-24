import re

finput = input('Please enter a filename: ')
try:
    fhand = open(finput)
except:
    print('Wrong filename!')
    exit()

list_of_nums = list()
for line in fhand:
    if len(line) > 0:
        search = re.findall(r'^New\s.*:\s(\d+)$', line)
        if len(search) > 0:
            list_of_nums.append(search)

list_of_ints = list()
for inner_list in list_of_nums:
    for number in inner_list:
        list_of_ints.append(int(number))

print(f'The average number of all the numbers is: {int(sum(list_of_ints)/len(list_of_ints))}')