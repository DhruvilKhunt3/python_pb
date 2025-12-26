# Write a Python program to reverse the content of a one file and store it in second file and also convert content of second
# file into uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from
# the content of third file.
# Examples:
# If data file one contains the following data:
# Friends are crazy, Friends are naughty !
# Friends are honest, Friends are best !
# Output 1:
# ! tseb era sdneirF ,tsenoh era sdneirF
# ! ythguan era sdneirF ,yzarc era sdneirF
# 4
# Output 2:
# ! TSEB ERA SDNEIRF ,TSENOH ERA SDNEIRF
# ! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF
# Output 3:
# Vowels = 22
# Output 4:
# ! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF
vowel =0
with open("friends.txt","r") as a:
    with open("file2.txt","w") as b:
        with open("file3.txt","w") as c:
            x = a.readlines()
            for i in x[::-1]:
                b.writelines(i)
                c.writelines(i.upper())
            for i in x:
                if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                    print('h')
print(vowel)