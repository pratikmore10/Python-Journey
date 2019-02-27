name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')
dct = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From') or not line.startswith('From:'):
        continue
    words = line.split()
    email = words[1:]
    for mail in email:
        dct[mail] = dct.get(mail, 0) + 1


big_count = None
big_user = None
for user, count in dct.items():
    if big_count is None or count > big_count:
        big_user = user
        big_count = count

print(big_user, big_count)
