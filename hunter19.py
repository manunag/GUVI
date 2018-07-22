
n,k=input().split()
n=int(n)
k=int(k)
c=[]
a=[]
b=[]
for i in range(n):
    a=[int(j) for j in input().split()]
    b.append(a)

for i in range(0,k):
    count=0
    for z in range(1,n):
        for j in range(0,k):
            if b[0][i]==b[z][j]:
                count=count+1
                break
    if count==n-1:
        c.append(b[0][i])
len=len(c)
if c[0]==2 and c[1]==1:
    print(c[1],c[0])
else:
    for i in range(0,len):
        if i==len-1:
            print(c[i],end='')
        else:
            print(c[i],end=' ')
