fname = input("Enter file name: ")
fh = open(fname)
lst = list()
out = []
for line in fh:
    word = line.rstrip()
    word1 = word.split()
    for words in word1:
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)
