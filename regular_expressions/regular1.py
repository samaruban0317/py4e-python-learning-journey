import re
name = input("Enter file name:")
fh = open(name)
nums = list()
counts = 0
for i in fh:
    words = i.rstrip()
    numbers = re.findall('([0-9.]+)',words)
    for num in numbers:
        try:
            integer = int(num)
            nums.append(integer)
        except:
            continue
for count in nums:
    counts = counts + count
print(counts)