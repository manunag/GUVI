x,y=input().split()
x=int(x)
y=int(y)
a=[int(i) for i in input().split()]
b=int(input())
sum=0
for i in range(0,x):
    sum=sum+a[i]
sum=int(sum/2)
z=int(a[y]/2)
if sum-z==b:
    print("Bon Appetit")
else:
    print(z)
