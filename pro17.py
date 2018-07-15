x,y=input().split()
x=int(x)
y=int(y)
a=[int(i) for i in input().split()]
chk=0
for i in range(0,x):

    for j in range(i+1,x):

        z=int(a[i])+int(a[j])
        if z==y:
            chk=1
if chk==1:
    print("yes")
else:
    print("no")
