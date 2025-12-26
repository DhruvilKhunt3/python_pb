def is_armstrong(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3 
        temp //= 10
    return sum == number

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")