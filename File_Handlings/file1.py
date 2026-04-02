fh = open("words.txt")
for lines in fh:
    words = lines.upper()
    print (words.rstrip())