from __future__ import print_function
a=raw_input()
b=raw_input()
c=[]
d=[]
e=[]
for i in range(len(a)):
    c.append(int(a[i]))
for i in range(len(b)):
    d.append(int(b[i]))
c.reverse()
d.reverse()
if(len(a)>=len(b)):
    for i in range(len(a)-len(b)):
        d.append(0)
if(len(b)>=len(a)):
    for i in range(len(b)-len(a)):
        c.append(0)
for i in range(max(len(a),len(b))):
    if c[i]+d[i]>=10 and i<max(len(a),len(b))-1:
        c[i+1]=c[i+1]+1
        e.append(c[i] + d[i]-10)
    else:
        e.append(c[i] + d[i])
e.reverse()
for i in range(len(e)):
    print(e[i],end='')



