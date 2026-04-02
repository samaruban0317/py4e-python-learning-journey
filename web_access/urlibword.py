import urllib.request,urllib.parse,urllib.error
word = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
count = 0
words = dict()
for i in word:
    wrd = i.decode().split()
    count = count+1
    for j in wrd:
        words[j] = words.get('j',0)+1
print(count,'\n',words)