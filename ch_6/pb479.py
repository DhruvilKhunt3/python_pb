space = 0
with open("friends.txt",'r') as f:
    x = f.read()
    print(len(x.split()))