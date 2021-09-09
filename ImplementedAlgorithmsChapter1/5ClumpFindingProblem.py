'''
KWESIGA KATO STEVEN 2018/BCS/034/PS
    AKANKUNDA DARIUS   2018/BCS/013/PS
CLUMPFINDING(Genome, k, t, L)
FrequentPatterns an empty set
for i 0 to 4k  1
CLUMP(i) 0
for i 0 to |Genome|  L
Text the string of length L starting at position i in Genome
FREQUENCYARRAY COMPUTINGFREQUENCIES(Text, k)
for index 0 to 4k  1
if FREQUENCYARRAY(index)  t
CLUMP(index) 1
for i 0 to 4k  1
if CLUMP(i) = 1
Pattern NUMBERTOPATTERN(i, k)
add Pattern to the set FrequentPatterns
return FrequentPatterns
'''


import itertools
from collections import Counter

def find_frequent(string, k,t):
    words = []
    frequent = []

    for i in range(len(string)):
        word = "".join(string[i: i + k])

        if len(word) == k:
            words.append(word)

    return Counter(words).most_common()

def clump_finding_problem(string, k, L, t):
    words = []
    for i in range(len(string)):
        strings1 = string[i:i + L]
        if len(strings1) == L:
            words.append(find_frequent(strings1, k, t))

    pattern = list(itertools.chain(*words))
    print(*set([x[0] for x in pattern if x[1] >= t]))


data = "".join(open('rosalind_ba1e.txt')).split()
clump_finding_problem(data[0], int(data[1]), int(data[2]), int(data[3]))
