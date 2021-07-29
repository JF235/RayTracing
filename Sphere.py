from numpy import absolute, sqrt
from Vector import *
from Hittable import *
from Ray import *

class Sphere(Hittable):
    def __init__(self, radius, center):
        super().__init__()
        self.radius = radius
        self.center = center
    

    def hit(self, ray, hitRecord, tmin = -1000000, tmax = 100000):
        sourceToCenter = ray.source - self.center
        a = dot(ray.direction, ray.direction)
        b = 2* dot(sourceToCenter, ray.direction)
        c = dot(sourceToCenter, sourceToCenter) - self.radius ** 2
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return False
        
        t = (-b - sqrt(discriminant) ) /(2*a) # menor raiz
        if(t < tmin or t > tmax):
            t = (-b + sqrt(discriminant) ) /(2*a) # maior raiz
            if (t < tmin or t > tmax):
                return False
        
        hitRecord.t = t
        hitRecord.intersecPoint = ray.getPoint(t)
        hitRecord.normal = (ray.getPoint(t) - self.center).normalize()

        return True
