fout = input('Enter a file name: ')
fhandle = open(fout)

for line in fhandle:
    print(line.upper())