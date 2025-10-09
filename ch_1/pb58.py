a = int(input('enter base -> '))
n = int(input('enter result -> '))
x,pow = 0,1
while pow<n:
    pow = pow*a
    x = x+1
if(pow==n):
    print(x)
else:
    print('no int found')