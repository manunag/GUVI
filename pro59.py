import sys
a = input()
b = a.split('|')
c = input()

n = abs(len(b[0])-len(b[1]))

if n==0 :
    print('Impossible')
    sys.exit()
if n != len(c) :
    print('Impossible')
    sys.exit()
if len(c) >= n :
    if len(b[0]) < len(b[1]) :
        s = b[0] + c + '|' + b[1]
    else :
        s = b[0] + '|' + b[1] + c
    print(s)
else :
    print('Impossible')
