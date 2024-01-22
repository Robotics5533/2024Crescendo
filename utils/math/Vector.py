from typing import Callable, Union

class Vector:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def pythagorean(self, point: 'Vector') -> float:
        return ((self.a - point.a) ** 2 + (self.b - point.b) ** 2 + (self.c - point.c) ** 2) ** 0.5
    
    def map(self, func: Callable[[float, int], Union[float, int]]):
        return Vector(func(self.a), func(self.b), func(self.c))

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.a - other.a, self.b - other.b, self.c - other.c)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.a * scalar, self.b * scalar, self.c * scalar)

    def dot_product(self, other: 'Vector') -> float:
        return self.a * other.a + self.b * other.b + self.c * other.c

    def cross_product(self, other: 'Vector') -> 'Vector':
        return Vector(
            self.b * other.c - self.c * other.b,
            self.c * other.a - self.a * other.c,
            self.a * other.b - self.b * other.a
        )

    def magnitude(self) -> float:
        return (self.a ** 2 + self.b ** 2 + self.c ** 2) ** 0.5

    def normalize(self) -> 'Vector':
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return Vector(self.a / mag, self.b / mag, self.c / mag)
