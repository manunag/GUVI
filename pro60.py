a=input()
x=3
j=x
z=[]
for i in range (1,int(a)+1):
    if j==0:
        x=x*2
        j=x
    z.append(j)
    j=j-1
print(z[int(a)-1])
