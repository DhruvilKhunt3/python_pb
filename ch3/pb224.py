def newton_sqrt(x, iterations):
    guess = x / 2  # Initial
    for _ in range(iterations):
        guess = (guess + x / guess) / 2  
    return guess

x = float(input("Enter the number to find the square root of: "))
iterations = int(input("Enter the number of iterations: "))

sqrt_value = newton_sqrt(x, iterations)

print(f"The approximate square root of {x} after {iterations} iterations is: {sqrt_value}")