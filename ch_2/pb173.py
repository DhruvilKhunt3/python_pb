def get_score(n):
    while True:
        s = int(input("Enter Test Score: "))
        if s > 100:
            print("Entered score is more than hundred, so enter again")
        else:
            return s

s1 = get_score(1)
s2 = get_score(2)
s3 = get_score(3)
s4 = get_score(4)
s5 = get_score(5)
s6 = get_score(6)
s7 = get_score(7)
s8 = get_score(8)
s9 = get_score(9)
s10 = get_score(10)

total = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10
average = total / 10
highest = s1
lowest = s1
for s in [s2, s3, s4, s5, s6, s7, s8, s9, s10]:
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s


first = highest
second = -1 #highest find karva mate variable ni valu minmun levani
for s in [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]:
    if s != first and s > second:
        second = s

low1 = lowest
low2 = 101 #lowest find karva mate variable ni value maimun levani
for s in [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]:
    if s != low1 and s < low2:
        low2 = s
print(low1,low2)
new_avg = (total - low1 - low2) / 8

print("Highest Score is:", highest)
print("Lowest Score is:", lowest)
print("Average Test Score is:", average)
print("Second Largest Score is:", second)
print("Average after dropping the two lowest scores:", new_avg)