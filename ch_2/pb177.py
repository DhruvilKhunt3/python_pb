year = int(input("Enter year -> "))
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e
if year in [1954, 1981, 2049, 2076]:
    dateofeaster -= 7
if dateofeaster > 31:
    month = 4  # April
    day = dateofeaster - 31
else:
    month = 3  # March
    day = dateofeaster
print(f"Easter Sunday in {year} is on {year}-{month:02d}-{day:02d}")