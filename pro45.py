x=input()
a=[]
z=int(len(x))
d=0
g=int(x)
y=0
for i in range(0,z):
          d=int(g%10)
          a.append(d)
          g=int(g/10)


for i in range(0,z):
    y=y*10+a[i]

if int(x)==y:
    print("yes")
else:
    m=a[::-1]
    count=0
    for i in range(z-1,0,-1):
        if m[i]==0:
            count=count+1
        else:
            break
    m=m[::-1]
    for i in range(0,count):
        a.append(0)
        m.append(0)
        y=y*10
    m=m[::-1]
    if a==m:
        print("yes")
    else:
        print("no")
