def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The maximum of {num1} and {num2} is {max_of_two(num1, num2)}")