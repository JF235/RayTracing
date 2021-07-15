from Vector import Vector
import numpy as np

class Ray():
    def __init__(self, source, direction) -> None:
        self.source = source
        self.direction = direction.normalize()

    def __repr__(self):
        return f'{self.source} + t {self.direction}'

    def getPoint(self, t = 0):
        return self.source + t * self.direction
    
    def getColor(self):
        direction = self.direction
        t = 0.5 * (direction.y + 1) # Quanto maior o valor de y maior é t
        
        azul = np.array([0.5, 0.7, 1.0])
        branco = np.array([1,1,1])

        return (1 - t) * branco + t * azul # Quanto maior t mais azul ele fica.

