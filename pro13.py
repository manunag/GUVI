n,q=input().split()
n=int(n)
q=int(q)
ar=[int(i) for i in input().split()]

x=[]
y=[]
for i in range(0,q):
    a,b=input().split()
    x.append(a)
    y.append(b)


for i in range(0,q):
    min=ar[i]
    s=int(x[i])-1

    t=int(y[i])-1
    for j in range(s,t+1):
        if min>ar[j]:
            min=ar[j]
    print(min)
