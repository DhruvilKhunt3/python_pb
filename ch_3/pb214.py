def is_in_range(number, start, end):
    return start <= number <= end

num = 7
range_start = 5
range_end = 10

if is_in_range(num, range_start, range_end):
    print(f"{num} is in the range {range_start} to {range_end}")
else:
    print(f"{num} is NOT in the range {range_start} to {range_end}")