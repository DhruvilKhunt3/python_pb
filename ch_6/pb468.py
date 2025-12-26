f = open("friends.txt","r")
count = 1
for i in f:
    if(count%2!=0):
        print(i)
        count+=1
    else:
        count+=1
