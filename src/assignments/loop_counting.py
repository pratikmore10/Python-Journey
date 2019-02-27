largest = None
smallest = None
num_list = list()
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        num_list.append(num)
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
    except:
        print('Invalid input')
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
