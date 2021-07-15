import numpy as np

class Vector:
    def __init__(self, x, y, z = 0):
        self.x = x 
        self.y = y
        self.z = z
        self.coordinates = np.array([x,y,z])

    def __add__(self, other):
        newX = self.x + other.x
        newY = self.y + other.y
        newZ = self.z + other.z

        return Vector(newX, newY, newZ)

    def __sub__(self, other):
        newX = self.x - other.x
        newY = self.y - other.y
        newZ = self.z - other.z

        return Vector(newX, newY, newZ)


    def __mul__(self, scalar):
        newX = self.x * scalar
        newY = self.y * scalar
        newZ = self.z * scalar

        return Vector(newX, newY, newZ)

    __rmul__ = __mul__
    '''
    def __truediv__(self, num):
        return Vector(self.x/num, self.y/num, self.z/num)    
    '''

    def __repr__(self):
        return f'[{self.x}  {self.y}  {self.z}]'
    
    def dot(self, vec):
        return (self.x * vec.x) + (self.y * vec.y) + (self.z * vec.z)


    def norm(self):
        return np.sqrt(self.dot(self))
    

    def normalize(self):
        unitVec = self.coordinates.copy()
        unitVec = unitVec/self.norm()
        return Vector(unitVec[0], unitVec[1], unitVec[2])

    '''
        def printVec(self):
            print(f'[{self.x}  {self.y}  {self.z}]')
    '''
    
    def copy(self):
        copiedVec = Vector(self.x, self.y, self.z)
        return copiedVec