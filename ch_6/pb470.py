# Write a python program that reads a text file and changes the file by capitalizing each character of file.
f = open("friends.txt","r")
x = f.readlines()
print(x)
f.close()
f = open("friends.txt",'w')
for i in x:
    f.write(i.upper())