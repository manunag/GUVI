s=input()
for i in range(len(s)-1):
    if s[0]<s[i+1]:
        print(s[i+1:])
        break
