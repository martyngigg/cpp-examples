f = open('Holmes.txt','r')

g = {}

punctuation = (".", ",", "?", "'", "\"", "!", "(", ")", ":")

for line in f:
    line = line.rstrip().lower()
    words = line.split()
    for word in words:
        word = word.rstrip()
        for p in punctuation:
            index = word.find(p)
            if index == -1: continue
            # Match found
            if index == 0:
                word = word.lstrip(p)
            elif index == len(word) - 1:
                word = word.rstrip(p)
            else:
                word = word[:index] + word[index+1:]
        if len(word) < 5: continue
        if word in g.keys():
            g[word] += 1
        else:
            g[word] = 1

occ = {}
for key,value in g.iteritems():
    if value in occ.keys():
        occ[value].append(key)
    else:
        occ[value] = [key]

for key in sorted(occ.keys(),reverse=True):
    value = occ[key]
    for word in value:
        print '%s %d' % (word.ljust(15), key)

