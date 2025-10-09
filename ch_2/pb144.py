x = int(input("Enter number -> "))
while x != 1 and x != 4:
    s = 0
    while x > 0:
        digit = x % 10
        s += digit * digit
        x //= 10
    x = s

if x == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")