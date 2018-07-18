n,q=input().split()
q=int(q)
a=[int(i) for i in input().split()]
u=[0]*q
v=[0]*q
xor=[0]*q
for i in range(0,q):
    u[i],v[i]=input().split()
    u[i]=int(u[i])
    v[i]=int(v[i])

for i in range(0,q):
    for j in range(u[i]-1,v[i]):
        xor[i]=xor[i]^a[j]
for i in xor:
    print(i)
