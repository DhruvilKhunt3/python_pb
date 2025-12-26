def sum_of_natural_numbers(n):
    return n * (n + 1) // 2  # Using formula 1+2+...+n = n*(n+1)/2

def average_of_natural_numbers(n):
    total = sum_of_natural_numbers(n)
    return total / n

n = int(input("Enter a positive integer: "))

sum_n = sum_of_natural_numbers(n)
avg_n = average_of_natural_numbers(n)

print(f"Sum of first {n} natural numbers: {sum_n}")
print(f"Average of first {n} natural numbers: {avg_n}")