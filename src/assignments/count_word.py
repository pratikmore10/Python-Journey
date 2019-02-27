fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    total = total + float(line.split()[1])
average = total/count
print("Average spam confidence: " + str(average))
