from Screen import Screen
import numpy as np
from Vector import Vector
from Ray import Ray
from ImageGenerator import ImageGenerator

def testImage(imageGenerator):
    imageGenerator.saveImage('QuadroPreto')
    imageGenerator.fadeImageRGB()
    imageGenerator.saveImage('FadeRGB')


def main():
    aspRat = 16/9
    imGen = ImageGenerator(400, int (400/aspRat))
    origin = Vector(0, 0, 0)
    posCamera = origin.copy()

    screen = Screen(2, imGen.aspecRatio, 1)
    screen.getLowerLeft(origin)

    imGen.castRay(origin, screen)
    imGen.saveImage('RayTracing1')


main()