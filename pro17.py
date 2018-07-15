
x,y=input().split()
len=len(x)
x=int(x)
y=int(y)
a=[int(i) for i in input().split()]
chk=0

for i in range(0,len):

    for j in range(i+1,len):

        z=int(a[i])+int(a[j])
        if z==y:
            chk=1
if chk==1:
    print("yes")
else:
    print("no")
