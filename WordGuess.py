from itertools import permutations

def getWords(Av, WordList, le):
    combs = []
    for x in permutations(Av, le):
        t = ""
        combs.append(t.join(x))
    found = []
    for i in combs:
        if i in WordList:
            found.append(i)
    return found

def loadList(fileloc):
    WordList = []
    with open(fileloc, 'r') as file:
        for line in file:
            for word in line.split():
                WordList.append(word.lower())
    return WordList

#Loading and getting input
WList = loadList("WordList")
Av = input("Input available letters: ")

#Da smartie bits appends uniques
comb = []
for i in range(4,7):
    for j in getWords(Av, WList, i):
        if j not in comb:
            comb.append(j)
            print(j)
