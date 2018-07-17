a=input()
c=0
z=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a.lower()
for i in range(0,len(a)):
    for j in range(0,len(z)):
        if a[i]==z[j]:
            z[j]=0
for i in range(0,len(z)):
    if z[i]!=0:
        c=c+1
if c==0:
    print("yes")
else:
    print("no")
