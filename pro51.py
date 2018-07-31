t=int(input())
b=[int(i) for i in input().split()]
y=[]
for i in range(len(b)):
    if int(b[i])<0:
        b[i]=int((b[i]/b[i]))*-1
    else:
        b[i]=int(b[i]/b[i])
z=int(-1)
for i in range(len(b)):
    count=0
    z=int(-1)
    if b[i]==z:
        count=count+1
        for j in range(i+1,len(b)):
            z=z*-1
            if b[j]==z:
                count=count+1

                if j==len(b)-1:
                    y.append(count)

            else:
                y.append(count)
                break
    else:
        z=1
        count=count+1
        for j in range(i+1,len(b)):
            z=z*-1
            if b[j]==z:
                count=count+1

                if j==len(b)-1:
                    y.append(count)

            else:
                y.append(count)
                break
    if i==len(b)-1:
        y.append(count)

for i in range(len(y)):
    if i==len(y)-1:
         print(y[i],end='')
    else:
        print(y[i],end=' ')
