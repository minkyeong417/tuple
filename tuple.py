filename = input('Enter a file name: ')
handle = open(filename, 'r')
dic = dict()
text = handle.read()
for word in list(text):
    if 'a'< word <'z' or 'A'< word <'Z':
        dic[word] = dic.get(word,0) + 1
lists = dic.items()
newl = list()
for k,v in lists:
    newl.append((v,k))
for a,b in sorted(newl,reverse = True):
    print(b)
