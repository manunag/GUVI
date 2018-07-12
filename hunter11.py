a=[str(i) for i in input().split()]
x=len(a)
for i in range(0,x):
    print(a[i][::-1],end=' ')
