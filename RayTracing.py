from Screen import *
from Vector import *
from Ray import *
from ImageGenerator import *
from Sphere import *

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
    screen.calculateLowerLeft(origin)

    imGen.castRay(origin, screen, sphere)
    imGen.saveImage('RayTracing3')


main()