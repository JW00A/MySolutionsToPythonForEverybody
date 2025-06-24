fout = input('Enter a file name: ')
fhandle = open(fout)

count = 0
total = 0
for line in fhandle:
    if 'X-DSPAM-Confidence' in line:
        count += 1
        colon_index = line.find(":")
        total += float(line[colon_index+1:].strip())
        
print(f'Average spam confidence: {total / count}')