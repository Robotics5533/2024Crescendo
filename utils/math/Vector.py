class Vector:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def pythagorean(self, point: 'Vector') -> float:
        return ((self.a - point.a) ** 2 + (self.b - point.b) ** 2) ** 0.5
