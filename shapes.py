import math


class Circle:
    def __int__(self, r):
        self._radius = r

    def get_square(self) -> float:
        return math.pi * self._radius * self._radius


class Rectangle:
    def __int__(self, rectangle_height, rectangle_width):
        self._height = rectangle_height
        self._width = rectangle_width

    def get_square(self) -> float:
        return self._width * self._height


class Triangle:
    def __int__(self, hypotenuse, leg1, leg2, height):
        self._hypotenuse = hypotenuse
        self._leg1 = leg1
        self._leg2 = leg2
        self._height = height


class Cylinder(Rectangle, Circle):
    def __int__(self, height, width):
        super().__int__(height, width)
        super().__int__(width / 2)

    def get_surface_square(self):
        return 2 * super(Circle).get_square() + 2 * math.pi * (super()._width / 2) * super()._height


class Sphere(Circle):
    def __int__(self, radius):
        super().__int__(radius)

    def get_volume(self) -> float:
        return math.pi * super()._radius * super()._radius * super()._radius * 4 / 3


class Cone(Triangle):
    def __int__(self, hypotenuse, leg1, leg2, height):
        super().__int__(hypotenuse, leg1, leg2, height)

    def get_square_of_bottom(self) -> float:
        return math.pi * (super()._hypotenuse * super()._hypotenuse) / 4


if __name__ == '__main__':
    pass
