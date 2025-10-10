def product_of_natural_numbers(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

n = int(input("Enter a positive integer: "))
product_n = product_of_natural_numbers(n)
print(f"Multiplication (product) of first {n} natural numbers: {product_n}")