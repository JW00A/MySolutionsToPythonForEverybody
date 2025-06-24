finput = input('Please enter a file name: ')
try:
    fhand = open(finput)
except:
    print('Wrong file name!')
    exit()

dictionary = dict()
for line in fhand:
    words = line.split()

    if len(words) > 2 and words[0] == 'From':
        required_word = words[1]
        dictionary[required_word] = dictionary.get(required_word, 0) + 1

list_tuples = list()
for key, value in dictionary.items():
    list_tuples.append((value, key))

list_tuples.sort(reverse=True)

for key, value in list_tuples[:1]:
    print(f'{value} sent the most: {key}')