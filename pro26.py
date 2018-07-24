n=input()
a=[int(i) for i in input().split()]
z=[]
for i in range(len(a)):
    count =1
    x=a[i]
    for j in range(i+1,len(a)):
        if a[j]>x:
            count=count+1
            x=a[j]
    z.append(count)
print(max(z))
