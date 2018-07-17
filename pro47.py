n,k=input().split()
x=1
k=int(k)
n=int(n)

while(k>0):
    k=k-1
    x*=10;
for i in range(1,x+1):
    if((n*i)%x==0):
        print(n*i)
        break
