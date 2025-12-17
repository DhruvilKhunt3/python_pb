# Write python program to count the number of lines in a file.
with open("friends.txt","r") as f:
    x = f.readlines()
    print(len(x))