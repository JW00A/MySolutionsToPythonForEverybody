finput = input('Enter a file name: ')
try:
    fhand = open(finput)
except:
    print('Wrong file name!')
    exit()

dictionary = dict()
for line in fhand:
    words = line.split()

    if len(words) > 3 and words[0] == 'From':
        dictionary[words[2]] = dictionary.get(words[2], 0) + 1

print(dictionary)