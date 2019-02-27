fname = input("Enter file name: ")
fh = open(fname, 'r')
print(fh.read().rstrip())
