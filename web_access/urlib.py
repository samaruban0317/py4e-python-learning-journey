import urllib.request,urllib.parse,urllib.error
fhand = urllib.request.urlopen('https://data.pr4e.org/intro-short.txt')
for i in fhand:
    print(i.decode().strip())