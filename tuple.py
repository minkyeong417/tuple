filename = input('Enter a file name: ')
handle = open(filename, 'r')
dic = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5] #time == '09:14:16'
        dic[time[:2]] = dic.get(time[:2],0) + 1

for hr,ct in sorted(dic.items()):
    print(hr, ct)
