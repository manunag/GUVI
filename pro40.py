
s=input()
count=0
a=['d','h','o','n','i']
if len(s)==5:
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if a[i]==s[j]:
                a[i]=0
                break
    for i in range(len(a)):
        if a[i]!=0:
            count=1
    if count==0:
        print("yes")
    else:
        print("no")
else:
    print("no")
