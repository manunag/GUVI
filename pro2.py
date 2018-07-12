x,y=input().split()
a=[]
z=int(len(x))
t=z-int(y)
g=-1

for j in range(0,int(y)+1):
    d=0
    g=g+1
    for i in range(g,t):
        d=d*10+int(x[i])
    if t<=int(z):
        t=t+1
    a.append(d)
min=int(a[0])
for i in a:
    if i<min:
        min=i
print(min)
