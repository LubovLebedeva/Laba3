from math import pi

class Sphere:
    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        else:
            raise TypeError # raise TypeError("<Последняя строчка лога об ошибке>")
        self.r, self.x, self.y, self.z = arg

    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2 < self.r**2

result = Sphere()
print ("Объем сферы:", result.get_volume())
print ("Площадь внешней поверхности сферы:", result.get_square())
print ("Радиус сферы:", result.get_radius())
print ("Центр сферы:", result.get_center())
result.set_radius(2); print ("Поменяем радиус сферы на", result.get_radius())
result.set_center(1, 1, 1); print ("Поменяем центр сферы на", result.get_center())
print ("Точка (2,0,1) внутри сферы?", result.is_point_inside(2,0,1))
