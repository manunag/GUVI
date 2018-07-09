
n=input()
if n.isalpha():
    print("invalid")
else:
    n=int(n)
    a = [int(i) for i in input().split()]
    chk=0
    for i in range(0,n):
        if a[i]==i:
            if(i==n-1):
                print(i)
                chk=1
            else:
                print(i,end=' ')
                chk=1
    if chk==0:
        print(-1)
