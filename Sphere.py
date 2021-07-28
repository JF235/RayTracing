from numpy import sqrt
from Vector import *

class Sphere:
    def __init__(self, radius: int, center: Vector):
        self.radius = radius
        self.center = center

    def checkIntersection(self, ray):
        sourceToCenter:Vector = ray.source - self.center
        a = dot(ray.direction, ray.direction)
        b = 2* dot(sourceToCenter, ray.direction)
        c = dot(sourceToCenter, sourceToCenter) - self.radius ** 2
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return -1;
        else:
            return (-b - sqrt(discriminant) ) /(2*a) # menor raiz

