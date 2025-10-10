def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Input from the user
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
# Validate positive integers
if num1 <= 0 or num2 <= 0:
    print("Both numbers must be positive integers.")
else:
    result = gcd(num1, num2)
    print(f"The greatest common divisor (GCD) of {num1} and {num2} is {result}.")