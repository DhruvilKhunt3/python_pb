num = input('Enter number -> ')
new_num = ''
for i in num:
    x = int(i)
    if(x==9):
        x=0
    else:
        x+=1
    new_num+=str(x)
print(int(new_num))