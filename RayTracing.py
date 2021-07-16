from Screen import Screen
import numpy as np
from Vector import Vector
from Ray import Ray
from ImageGenerator import ImageGenerator
from Sphere import Sphere

def testImage(imageGenerator):
    imageGenerator.saveImage('QuadroPreto')
    imageGenerator.fadeImageRGB()
    imageGenerator.saveImage('FadeRGB')


def main():
    aspRat = 16/9
    imGen = ImageGenerator(int (400/aspRat), 400)
    origin = Vector(0, 0, 0)
    posCamera = origin.copy()
    sphere = Sphere(0.5, Vector(0,0,-1))
    screen = Screen(2, imGen.aspecRatio, 1)
    screen.getLowerLeft(origin)

    imGen.castRay(origin, screen, sphere)
    imGen.saveImage('RayTracing1')


main()