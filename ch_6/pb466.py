# Write a python program to create and read the city.txt file in one go and print the contents on the output screen.
with open("city.txt","w+") as f:
    f.write("Hello hii hey")
    x = f.readlines()
    print(x)

f = open("city.txt","r")
for x in f:
    print(x)