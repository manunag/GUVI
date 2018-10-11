a=input()
b=len(a)
x=[]
for i in range(0,b):
    j=i+1
    if j==b:
        break
    else:

        while(a[j] not in x ):

            x.append(a[i:j+1])
            x.append(a[i])
            x.append(a[j])
            j=j+1
            if j==b:
                break


print(len(max(x,key=len)))
