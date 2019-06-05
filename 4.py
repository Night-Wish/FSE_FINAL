from __future__ import print_function
a1=list(input())
b=[]
for i in range(len(a1)):
    c=0
    for j in range(len(a1[i])-1):
        c=c+a1[i][j]
        b.append(c)
a2 = {}
for i in b:
    if b.count(i) > 1:
        a2[i] = b.count(i)
print(max(a2.values()))


