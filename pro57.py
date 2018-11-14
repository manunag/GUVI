import sys
a,b=input().split()

for i in range(0,len(a)-1) :
    x, y = i,i+1
    c = a[x:y + 1]
    
    if c in b :
        print('yes')
        sys.exit()
print('no')
