n,a,b=input().split()
a=int(a)
b=int(b)
n=int(n)
x=a+b
while x<=n:
	if x==n:
		c=1
		break
	else:
		c=0
		x=x+a+b
if c==1:
	print("YES")
else:
	print("NO")
