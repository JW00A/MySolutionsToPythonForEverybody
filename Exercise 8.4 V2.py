import string

unique_words = ['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks', 'It', 'is', 'the', 'east', 'and', 
                'Juliet', 'sun', 'Arise', 'fair', 'kill', 'envious', 'moon', 'Who', 'already', 'sick', 'pale', 'with', 'grief']

count = 0
for word in unique_words:
    word = word.lower()
    unique_words[count] = word
    count += 1

fhand = open('romeo-full.txt')

for line in fhand:
    for word in line.split():
        word = word.translate(word.maketrans('', '', string.punctuation)).lower()
        #word = word.strip(string.punctuation).lower()

        if not word in unique_words:
            unique_words.append(word)

unique_words.sort()
print(unique_words)

count = 0
for _ in unique_words:
    count += 1
print(count)