fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = list()
for line in fh:
    line = line.strip()
    line = line.split()
    for word in line:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
