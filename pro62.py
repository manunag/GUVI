a=input()
b=len(a)
x=[]


for i in range(0,int(b)):
    j=b-1
    while(j>i):
        t=i
        s=j

        if(t+1==s):

            if(a[t]==a[s]):
                c=1
        else:
            while(t!=(s+1)):
                
                if(a[t] == a[s]):
                    c=1
                else:
                    c=0
                    break
                t=t+1
                s=s-1
        if(c==1):
            x.append(a[i:j+1])
        j=j-1

ll=len(max(x,key=len))
print(b-ll)
