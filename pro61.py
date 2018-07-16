x=input()
y=input()
t=[]
s=[]
z=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,len(x)):
    for j in range(0,len(z)):
        if x[i] in z[j]:
            t.append(j+1)
        if y[i] in z[j]:
            s.append(j+1)
for i in range(0,len(x)):
    t[i]=t[i]+s[i]
    if t[i]>26:
        t[i]=t[i]-26
    a=t[i]
    t[i]=z[a-1]
for i in t:
    print(i,end='')
