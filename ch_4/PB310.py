# 310 Write a Python program using function to shift the decimal
# digits n places to the left, wrapping the extra digits around. If
# shift > the number of digits of n, then reverse the string.
num = (input('Enter number -> '))
shift = int(input('Enter shift -> '))
result = '' 
if shift > len(num):
    result = num[::-1]
else:
    result = num[shift:] + num[:shift]
print(result)