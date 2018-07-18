n=int(input())
a=[int(i) for i in input().split()]
sum=[0]*n
x=1
tot=0
for i in range(n):
    x=1
    for j in range(0,i):
        if a[i]!=a[j]:
            sum[i]=sum[i]+a[j]

for i in range(0,len(sum)):
    tot=tot+sum[i]
print(tot)
