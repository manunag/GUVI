n=int(input())
a=[int(i) for i in input().split()]
j=0
for i in range(0,n):
    if i%2==0 and a[i]%2!=0:
        if j==0:
            print(a[i],end='')
            j=j+1
        else:
            print('',end=' ')
            print(a[i],end='')
    elif i%2!=0 and a[i]%2==0:
        if j==0:
            print(a[i])
            j=j+1
        else:
            print('',end=' ')
            print(a[i],end='')
