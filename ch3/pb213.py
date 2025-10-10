def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

num = 5
print(f"The factorial of {num} is {factorial_recursive(num)}")