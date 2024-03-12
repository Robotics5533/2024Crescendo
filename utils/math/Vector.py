from typing import Callable, Union, Tuple
import math

from utils.math.algebra import deadzone

class Vector:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    


    @staticmethod
    def index_to_name(index: int) -> str:
        return "xyz"[index]
    
    def deadzone(self, error = 0.1): 
        values = [self.a, self.b, self.c]
        return deadzone(values, error)

    def pythagorean(self, point: 'Vector') -> float:
        return ((self.a - point.a) ** 2 + (self.b - point.b) ** 2 + (self.c - point.c) ** 2) ** 0.5
    
    def map(self, func):
        return Vector(func(self.a, 0), func(self.b, 1), func(self.c, 2))

    def dot_product(self, vec: 'Vector') -> float:
        return self.a * vec.a + self.b * vec.b + self.c * vec.c

    def cross_product(self, vec: 'Vector') -> 'Vector':
        return Vector(
            self.b * vec.c - self.c * vec.b,
            self.c * vec.a - self.a * vec.c,
            self.a * vec.b - self.b * vec.a
        )

    def magnitude(self) -> float:
        return (self.a ** 2 + self.b ** 2 + self.c ** 2) ** 0.5

    def normalize(self) -> 'Vector':
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return Vector(self.a / mag, self.b / mag, self.c / mag)

    def rotate(self, angle: float) -> 'Vector':
        rad_angle = math.radians(angle)
        
        new_a = self.a * math.cos(rad_angle) - self.b * math.sin(rad_angle)
        new_b = self.a * math.sin(rad_angle) + self.b * math.cos(rad_angle)
        
        return Vector(new_a, new_b, self.c)

    def scalar_project(self, vec: 'Vector') -> float:
        dot_product = self.dot_product(vec)
        magnitude_vec = vec.magnitude()
        
        if magnitude_vec == 0:
            raise ValueError("Magnitude of the vector onto which to project is zero.")
        
        return dot_product / magnitude_vec
    def __rmul__(self,other)->'Vector':
        return self*other
    def __mul__(self,other)->'Vector':
        if type(other) == float or type(other) == int:
            return Vector(self.a*other,self.b*other,self.c*other)
    def __str__(self):
        return f"Vector({self.a},{self.b},{self.c})"