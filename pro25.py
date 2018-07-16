n=int(input())
a=[int(i) for i in input().split()]
max1=[0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,n):
    max1[i]=0
    for j in range(i+1,n):
        if max1[i]==0:
            if a[i]<a[j]:
                max1[i]=max1[i]+1
            else:
                break
        elif a[j-1]<a[j]:
            max1[i]=max1[i]+1
        else:
            break
    max1[i]=max1[i]+1

print(max(max1))
