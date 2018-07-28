
n=int(input())
a=[int(i) for i in input().split()]
y=[]
for i in range(len(a)):
    if int(a[i])<0:
        a[i]=int((a[i]/a[i]))*-1
    else:
        a[i]=int(a[i]/a[i])

z=int(-1)
for i in range(len(a)):
    count=0
    z=int(-1)
    if a[i]==z:
        count=count+1
        for j in range(i+1,len(a)):
            z=z*-1
            if a[j]==z:
                count=count+1

                if j==len(a)-1:
                    y.append(count)

            else:
                y.append(count)
                break

    else:
        z=1
        count=count+1
        for j in range(i+1,len(a)):
            z=z*-1
            if a[j]==z:
                count=count+1

                if j==len(a)-1:
                    y.append(count)

            else:
                y.append(count)
                break
    if i==len(a)-1:
        y.append(count)

for i in range(len(y)):
    if i==len(y)-1:
         print(y[i],end='')
    else:
        print(y[i],end=' ')
