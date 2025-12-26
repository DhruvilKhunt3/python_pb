# Write a python program to search for a string in text files.
search = input("enter string for search -> ")
with open("2.txt","r") as f:
    x = f.readlines()
    for i in x:
        y = i.split()
        for z in y:
            if z==search:
                print("found")
