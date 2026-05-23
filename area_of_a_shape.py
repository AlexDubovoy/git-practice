from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Абстрактный метод для расчёта площади фигуры."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Расчёт площади прямоугольника: ширина * высота."""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Расчёт площади круга: п * радиус * радиус."""
        return math.pi * self.radius ** 2

rectangle = Rectangle(5, 10)
circle = Circle(7)

print(f"Площадь прямоугольника: {rectangle.area()}")  # 50
print(f"Площадь круга: {circle.area():.2f}")          # ~153.94