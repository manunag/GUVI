n = int(input())
a = [ int(i) for i in input().split()]
count=0
for i in range(0,n-2) :
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if a[i] > a[j] > a[k] :
                count=count+1
print(count)
