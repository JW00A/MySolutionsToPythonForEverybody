fname = input('Please enter a file name: ')
try:
    fhand = open(fname)
except:
    print('Wrong file name!')
    exit()

dictionary = dict()
for line in fhand:
    words = line.split()
    if len(words) > 5 and line.startswith('From'):
        index = words[5].find(':')
        word = words[5][:index]

        dictionary[word] = dictionary.get(word, 0) + 1

tuples_list = list()
for key, val in dictionary.items():
    tuples_list.append((key, val))

tuples_list.sort()

for key, val in tuples_list:
    if val > 1:
        print(f'Hour {key} has appeared in the search: {val} times')
    else:
        print(f'Hour {key} has appeared in the search: {val} time')