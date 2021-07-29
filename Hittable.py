import numpy as np
from Ray import *
from Vector import *

class HitRecord():
    def __init__(self, 
                intersecPoint = Vector(0,0,0), 
                normal = Vector(0,0,0), 
                t = 0):
        self.intersecPoint = intersecPoint
        self.normal = normal
        self.t = t # Valor de t que ocorre a interseccao


class Hittable():
    # Um objeto que pode ser atingido por um raio
    # vai possuir o raio e um intervalo de t onde
    # a interseccao pode acontecer [tmin, tmax]
    
    def __init__(self):
        self.hitRecord = HitRecord()

    # método abstrato de hit
    def hit(self, ray, hitRecord, tmin = 0, tmax = np.inf):
        pass

class HittableList(Hittable):
    def __init__(self):
        super().__init__()
        self.objects = list()

    def append(self, newObject):
        self.objects.append(newObject)
    
    def clear(self):
        self.objects.clear()

    def hit(self, ray, hitRecord = None, tmin = 0, tmax = np.inf):
        hitAnything = False
        closestDist = tmax

        for object in self.objects:
            if(object.hit(ray, object.hitRecord, tmin, closestDist)):
                hitAnything = True
                closestDist = object.hitRecord.t
                self.hitRecord = object.hitRecord
        
        return hitAnything


