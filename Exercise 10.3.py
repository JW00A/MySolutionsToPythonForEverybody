import string
finput = input('Plese enter the name of the file: ')
try:
    fhand = open(finput)
except:
    print('Wrong file name!')
    exit()

dictionary = dict()
for line in fhand:
    chars = string.punctuation + string.digits + string.whitespace # + string.ascii_uppercase if only a-z letters are needed
    line = line.translate(str.maketrans('', '', chars)).lower()
    for letter in line:
        dictionary[letter] = dictionary.get(letter, 0) + 1

tuples_list = list()
for key, val in dictionary.items():
    tuples_list.append((key, val))

tuples_list.sort(reverse=False)

for key, val in tuples_list:
    print(f'The letter {key} has appeared {val} times')