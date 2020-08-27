from operator import itemgetter
from itertools import groupby
n = int(input())
prisoners = {}
iteration = 0
for iteration in range(n):
    iteration += 1
    inputan = str(input())
    split = inputan.split()
    s = split[0]
    h = int(split[1])
    prisoners[s] = h
    sort_prisoner = {}
    for i in prisoners.values():
        sort_prisoner = sorted(prisoners.items(), key=lambda x: (x[1],x[0]))
sortkeyfn = itemgetter(1)
result = {}
for key,valuesiter in groupby(sort_prisoner, key=sortkeyfn):
    result[key] = list(v[0] for v in valuesiter)
b = 1
for g in result.values():
    a = len(g)+b
    print(*g,b, a-1)
    b=a