from __future__ import print_function
a=raw_input()
b={}
for i in a:
    b[i]=a.count(i)
for i in b:
    print (i,end='')
    print(b[i],end='')


