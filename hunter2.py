n=int(input())
a=list(input()for i in range(n))

for i in range(0,n):
    
    for j in range (i+1,n):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in a:
    print(int(i) ,end='')
