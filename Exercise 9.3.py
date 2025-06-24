finput = input('Please enter a file name: ')
try:
    fhand = open(finput)
except:
    print('Wrong file name!')
    exit()

dictionary = dict()
domains = dict()
for line in fhand:
    words = line.split()

    if len(words) > 2 and words[0] == 'From':
        required_word = words[1]
        dictionary[required_word] = dictionary.get(required_word, 0) + 1

    if len(words) > 2 and words[0] == 'From':
        required_word_index = words[1].find('@')
        required_word = words[1][required_word_index+1:]

        domains[required_word] = domains.get(required_word, 0) + 1 

largest_count = None
largest_sender = None
for word in dictionary:
    if largest_count == None or dictionary.get(word, 0) > largest_count:
        largest_count = dictionary.get(word, 0)
        largest_sender = word

print(f'Histogram for emails send by different addresses: {dictionary}', '\n')

print(f'Largest sender, ({largest_sender}) sent: ', largest_count)

print(f'Domains of senders: {domains}')