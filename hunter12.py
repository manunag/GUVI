n,x=input().split()
n=int(n)
x=int(x)
a=[int(i) for i in input().split()]

for i in range(0,n):
    for j in range(i+1,n):
        if(a[j]>a[i]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print(a[x-1])
