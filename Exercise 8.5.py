finput = input('Please enter a filename: ')
try:
    fhand = open(finput)
except:
    print('Wrong filename!')
    exit()

word = 'From'
count = 0

string = ''
for line in fhand:
    words = line.split()
    if len(words) > 0:
        search = words[0] == word
        if search:
            string += words[1] + '\n'
            count += 1

print(string)
print(f'There were {count} lines in the file with {word} as the first word')