a,b=input().split()
a=int(a)
b=int(b)
z=[]
for i in range(a+1,b):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if c==0:
        z.append(i)
x=len(z)
for i in range(0,x):
    if(i==x-1):
        print(z[i])
    else:
        print(z[i],end=' ')
