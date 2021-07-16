from Vector import Vector, dot

class Sphere:
    def __init__(self, radius: int, center: Vector):
        self.radius = radius
        self.center = center

    def checkIntersection(self, ray) -> bool:
        wasIntersected = False
        sourceToCenter:Vector = ray.source - self.center
        a = dot(ray.direction, ray.direction)
        b = 2* dot(sourceToCenter, ray.direction)
        c = dot(sourceToCenter, sourceToCenter) - self.radius ** 2
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            wasIntersected = True
        return wasIntersected


