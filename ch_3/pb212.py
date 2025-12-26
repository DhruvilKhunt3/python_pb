def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

f = 98.6
c = 37.0

print(f"{f}°F is {fahrenheit_to_celsius(f)}°C")
print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")