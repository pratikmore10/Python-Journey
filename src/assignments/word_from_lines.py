fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    new = line.rstrip()
    if not line.startswith('?'):
        continue
    words = line.split()
    print(words[1])
    count = count + 1
print("There were", count, "lines in the file with '?' as the first word")