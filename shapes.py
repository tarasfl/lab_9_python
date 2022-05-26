import math


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_square(self) -> float:
        return math.pi * self._radius * self._radius


class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    def get_square(self) -> float:
        return self._width * self._height


class Triangle:
    def __init__(self, hypotenuse, leg1, leg2, height):
        self._hypotenuse = hypotenuse
        self._leg1 = leg1
        self._leg2 = leg2
        self._height = height


class Cylinder(Rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)

    def get_surface_square(self):
        return math.pi * (self._width * self._width) / 4 + 2 * math.pi * (self._width / 2) * self._height


class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def get_volume(self) -> float:
        return math.pi * (self._radius * self._radius * self._radius) * 4 / 3


class Cone(Triangle):
    def __init__(self, hypotenuse, leg1, leg2, height):
        super().__init__(hypotenuse, leg1, leg2, height)

    def get_square_of_bottom(self) -> float:
        return math.pi * (self._hypotenuse * self._hypotenuse) / 4


if __name__ == '__main__':
    s = Sphere(9)

    print(s.get_volume())
