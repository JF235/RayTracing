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

class HittableList():
    pass

