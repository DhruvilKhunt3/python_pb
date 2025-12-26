num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(f"{num1} is {check_odd_even(num1)}")
print(f"{num2} is {check_odd_even(num2)}")