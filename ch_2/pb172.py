for i in range(1,101,1):
    sum1,sum2 = 0,0
    x = str(i)
    mul = 1
    for j in x:
        sum1+=(int(j)**mul)
        mul+=1
    for j in x:
        sum2+=int(j)
    if (sum1==i)and(i%sum2==0):
        print(i)