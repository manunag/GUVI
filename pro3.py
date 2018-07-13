x,y=input().split()
lenx=int(len(x))
len=len(y)
count=0
if(lenx<=len):
    for i in range(0,int(len)):
        if(i<lenx):
            if x[i] in y[i]:
                continue
            else:
                x=x[:i]+y[i]+x[i+1:]
                count=count+1
        else:
            x=x[:i+1]+y[i]
            count=count+1
else:
    count=lenx-int(len)

    x=x[:int(len)]


    for i in range(0,int(len)):
        if lenx>len:
            if x[i] in y[i]:
                continue
            else:
                x=x[:i]+y[i]+x[i+1:]
                count=count+1
print(count)
