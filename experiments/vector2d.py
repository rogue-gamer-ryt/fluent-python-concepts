import math


class Vector:
    def __init__(self, x=0, y=0, show_unambiguous_repr=True):
        self.x = x
        self.y = y
        self._show_unambiguous_repr = show_unambiguous_repr
    
    def __repr__(self):
        if self._show_unambiguous_repr:
            return f"Vector({self.x!r}, {self.y!r})"
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # def __bool__(self):
    #     return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

if __name__ == "__main__":
    v1 = Vector(2, 4)
    v2 = Vector(3, 4)

    print(f"Combined Vector: {v1 + v2}")
    print(f"Scaled Vector: {v1 * 3}")
    print(f"Absolute Value: {abs(v1)}")

    v3 = Vector('0', '0')
    v4 = Vector('0', '0', show_unambiguous_repr=False)
    print(f"This should show string values: {v3}")
    print(f"This would \'look\' like integer values: {v4}")