x=str(input())
if x.isalpha():
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        print("Ovel")
    else:
        print("Consonant")
else:
    print("Invalid")
