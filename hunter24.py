a,n=input().split()
aj= [int(x) for x in input().split()]

c=0
for i in range(0,int(a)):
	for j in range(i+1,int(a)):
		if(aj[i]+aj[j]==int(n)):
			c=1
			break
if c==1:
	print("YES")
else:
	print("NO")
