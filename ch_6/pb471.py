# Write a Python program to copy the contents of a file to another file.
with open("2.txt","w+") as f:
    with open("friends.txt","r") as x:
        y = x.readlines()
        f.writelines(y)