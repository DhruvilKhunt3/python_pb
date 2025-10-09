def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print("Temperature Conversion")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = input("Enter your choice (1/2): ")
if choice == '1':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print("°F is equal to°C",c)
elif choice == '2':
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print("°C is equal to °F",f)
else:
    print("Invalid choice! Please enter 1 or 2.")