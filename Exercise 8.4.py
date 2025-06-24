unique_words = ['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks', 'It', 'is', 'the', 'east', 'and', 
                'Juliet', 'sun', 'Arise', 'fair', 'kill', 'envious', 'moon', 'Who', 'already', 'sick', 'pale', 'with', 'grief']

fhand = open('romeo-full.txt')

for line in fhand:
    for word in line.split():
        if not word.strip(',.?!:;[]-') in unique_words:
            unique_words.append(word.strip(',.?!:;[]-'))

unique_words.sort()
print(unique_words)