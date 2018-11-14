import sys
n = int(input())
a = [ int(i) for i in input().split()]

count=0
if n==1 :
    print(1)
    sys.exit()

for i in range(1,n-1) :
    if ((a[i] > a[i-1]) and (a[i] > a[i+1])) or ((a[i] < a[i-1]) and (a[i] < a[i+1])):
        count=count+1
print(count)
