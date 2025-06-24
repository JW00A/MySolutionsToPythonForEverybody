fout = input('Enter a file name: ')

if fout.lower() == 'na na boo boo':
    print(f"{fout.upper()} TO YOU - You have been punk'd!")
    exit()

try:
    fhandle = open(fout)
except:
    print(f'File cannot be opened: {fout}')
    exit()

count = 0
for line in fhandle:
    if 'Subject: ' in line:
        count += 1

print(f"There were {count} subject lines in {fout}")