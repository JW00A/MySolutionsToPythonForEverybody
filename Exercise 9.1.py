fhand = open('words.txt')

dictionary = dict()
for line in fhand:
    words = line.split()
    if len(words) > 0:
        for word in words:
            dictionary[word.lower()] = dictionary.get(word.lower(), 0) + 1

keys = list(dictionary.keys())
keys.sort()

string = ''
for key in keys:
    string += f'{key}: {dictionary[key]}, '

print(string)