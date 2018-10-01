a=int(input())
aj= [int(x) for x in input().split()]
aj=aj[::-1]
for i in range(0,a):
	print(aj[i],end='')
	if(i!=a-1):
		print("->",end='')
