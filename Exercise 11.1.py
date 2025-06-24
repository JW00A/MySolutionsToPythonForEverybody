import re

finput = input('Please enter a name of the file: ')
try:
    fhand = open(finput)
except:
    print('Wrong filename!')
    exit()

count = 0

rinput = str(input('Please enter a regular expression: '))
for line in fhand:
    if len(line) > 0:
        try:
            search_regex = re.search(rf'{rinput}', line)
        except:
            print('Wrong regex!')
            exit()
        
        if search_regex:
            count += 1

print(f'{finput} had {count} lines that matched {rinput}')