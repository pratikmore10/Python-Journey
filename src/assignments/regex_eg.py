import re
word = open('regex eg.txt')
lst = list()
totalSum = 0
for lines in word:
    lines = lines.rstrip()
    numbers = re.findall('[0-9]+', lines)
    if len(numbers) > 0:
        # print(numbers)
        numbersSum = 0
        for num in numbers:
            numbersSum += int(num)
        # print(numbersSum)
        totalSum += numbersSum
print(totalSum)
