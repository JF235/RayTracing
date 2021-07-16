import matplotlib.pyplot as plt
import numpy as np
from Ray import Ray
from Vector import Vector
from Screen import Screen

class ImageGenerator():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.image = np.zeros((height, width, 3))
        self.aspecRatio = width/height
    
    def saveImage(self, imageName):
        plt.imsave(f'Imagens/{imageName}.png', self.image)
    
    def fadeImageRGB(self):
        for i in range(self.height):
            for j in range(self.width):
                newPixel = np.array([j/(self.width), 1 - i/self.height , 0.25])
                self.writePixel(newPixel, i, j)
    
    def writePixel(self, pixel, i, j):
        self.image[i, j] = pixel


    def castRay(self, origin, screen:Screen, sphere):
        for i in range(self.height):
            print(f"{i}/{self.height}")
            for j in range(self.width):
                # u, v são coordenadas parametrizadas do plano de projeção.
                u = j / self.width
                v =  1 - i / self.height
                
                horizontalStep = Vector( screen.viewPortWidth, 0, 0) * u
                verticalStep = Vector(0, screen.viewPortHeight, 0) * v
                
                ray = Ray(origin, screen.lowerLeft + horizontalStep + verticalStep - origin)
                newPixel = ray.getColor(sphere)
                self.writePixel(newPixel, i, j)
