n,k = input().split()
n=int(n)
k=int(k)
n,k = int(n),int(k)
a = [ int(i) for i in input().split()]
b = [ int(i) for i in input().split()]
maxx = 0
for i in range(0,n) :
    b[i] = b[i]+ k
    d = []
    for j in range(0,n) :
        d.append(b[j]//a[j])
    minn = min(d)
    if minn > maxx :
        maxx = minn
print(maxx)
