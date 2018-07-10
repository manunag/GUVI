
n=input()
if n.isalpha():
    print("invalid")
else:
    n=int(n)
    a=[int(i) for i in input().split()]
    count=int(0)

    for i in range(0,n):
        count=int(0)
        for j in range(i+1,n):
            if a[i]==a[j]:
                a[j]='\0'
                count = count+1
        if count==0:
            print(a[i])
