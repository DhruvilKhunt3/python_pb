# Write a Python program to read a text file and do following: 1. Print no. of words 2. Print no. statements
f = open("city.txt",'r')
count = 0
for i in f:
    x = i.split()
    for j in x:
        count+=1
print(count)