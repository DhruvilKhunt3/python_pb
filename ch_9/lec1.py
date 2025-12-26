class point:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x
    def __sub__(self, other):
        return self.x - other.x
    def __mul__(self, other):
        return self.x * other.x
    def __floordiv__(self, other):
        return self.x // other.x
    def __lt__(self, other):
        return self.x < other.x
    def __le__(self, other):
        return self.x <= other.x
    def __eq__(self, other):
        return self.x == other.x
    def __ne__(self, other):
        return self.x != other.x
    def __gt__(self, other):
        return self.x > other.x
    def __ge__(self, other):
        return self.x >= other.x
o1 = point(10)
o2 = point(3)
print(f"Addition (o1 + o2): {o1 + o2}")
print(f"Subtraction (o1 - o2): {o1 - o2}")
print(f"Multiplication (o1 * o2): {o1 * o2}")
print(f"Floor Division (o1 // o2): {o1 // o2}")
print()

print("=== Testing Comparison Operations ===")
print(f"Less Than (o1 < o2): {o1 < o2}")
print(f"Less Than or Equal (o1 <= o2): {o1 <= o2}")
print(f"Equal (o1 == o2): {o1 == o2}")
print(f"Not Equal (o1 != o2): {o1 != o2}")
print(f"Greater Than (o1 > o2): {o1 > o2}")
print(f"Greater Than or Equal (o1 >= o2): {o1 >= o2}")
print()