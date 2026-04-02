import re

fname = input("Enter file name: ")
fh = open(fname)

total = 0

for line in fh:
    numbers = re.findall('[0-9]+', line)
    for n in numbers:
        total += int(n)

print(total)
