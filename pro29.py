
x=int(input())
y=0
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
        y=1
        print(1)
        print(i)
if y==0:
    print(0)
