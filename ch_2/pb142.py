x = int(input('Enter x -> '))
y = int(input('Enter y -> '))
z = int(input('Enter z -> '))
if x>y and x>z:
    print('max is',x)
else:
    if y>z:
        print('max is ',y)
    else: 
        print('max is ',z)