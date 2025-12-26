# Write a python program to read line by line from a given files file1 & file2 and write into file3.
with open("file3.txt","w+") as a:
    with open("friends.txt","r") as b:
        with open("2.txt","r") as c:
            for i in c:
                a.writelines(i)
            for j in b:
                a.writelines(j)
