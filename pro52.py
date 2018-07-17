a=[0,0,0,0]
b=[0,0,0,0]
c=0
a[0],b[0]=input().split()
a[1],b[1]=input().split()
a[2],b[2]=input().split()
a[3],b[3]=input().split()
for i in range(0,4):
    for j in range(1,4):
        if int(a[i])-int(a[j])==0:
            a[i]=0
            a[j]=0
        if int(b[i])-int(b[j])==0:
            b[i]=0
            b[j]=0
for i in range(0,4):
    if int(a[i]!=0) or int(b[i]!=0):
        c=c+1
if c==0:
    print("yes")
else:
    print("no")
