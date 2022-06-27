class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Cube(Square):
    def surface_area(self):
        area = super().area()
        return 6 * area


print(Cube(6).surface_area())