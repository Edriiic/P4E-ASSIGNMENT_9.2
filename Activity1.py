fname = input('Enter file name: ')
if len(fname) < 3:
    fname = 'mbox-short.txt'
fhand = open(fname)
elist = list()
dt = dict()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        #print(email)
        elist.append(email)
        #print(elist)

for word in elist:
    dt[word] = dt.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in dt.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)
