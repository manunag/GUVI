n=int(input())
a=[int(i) for i in input().split()]
b=a[:]
sum=0

cand=[1]*n
for i in range(0,n):
    c=1
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
            c=0
        else:
            c=1
    if c==1:
        a[i]=0
for i in range(0,n):
    for j in range(0,n):
        if b[i]<=a[j]:
            cand[i]=cand[i]+1

for i in range(len(cand)):
    sum=sum+cand[i]
print(sum)
