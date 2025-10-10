# for single star in midle
for i in range(1,6):
    if(i==5):
        print('*'*(i-1),' '*((2*(5-i))-1),'*','*'*(i-1),sep='')
    else:
        print('*'*i,' '*((2*(5-i))-1),'*'*i,sep='')
for i in range(4,0,-1):
    print('*'*i,' '*((2*(5-i))-1),'*'*i,sep='')