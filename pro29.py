
x=int(input())

sum=0
for i in range(0,x):
    sum=0
    t=i
    while(t!=0):
        z=t%10
        sum=sum+z
        t=int(t/10)

    sum=sum+i
    if sum==x:
        print(1)
        print(i)
