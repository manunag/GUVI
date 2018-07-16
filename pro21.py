n=int(input())
a=[int(i) for i in input().split() ]
x=int(n/2)
y=x+1
sum1=0
sum2=0

for i in range(0,x):
    sum1=sum1+a[i]
avg1=sum1/x

for i in range(y-1,n):
    sum2=sum2+a[i]
avg2=sum2/(n-x)
if avg1==avg2:
    print("yes")
else:
    sum1=0
    sum2=0
    for i in range(0,y):
        sum1=sum1+a[i]
    
    avg1=sum1/y

    for i in range(y+1,n):
        sum2=sum2+a[i]
    if y==n:
        avg2=sum2/1
    else:
        avg2=sum2/(n-y)

    if avg1==avg2:

        print("yes")
    else:
        print("no")
