n=input()
if n.isalpha():
    print("invalid")
else:
    n=int(n)
    a=[int(i) for i in input().split()]
    count=int(0)

    for i in range(0,n):
        count=int(0)
        for j in range(0,n):
            if a[i]==a[j]:
                count = count+1
        if count==1:
            print(a[i])
