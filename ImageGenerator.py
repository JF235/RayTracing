import matplotlib.pyplot as plt
import numpy as np
from Ray import *
from Vector import *
from Screen import *


class ImageGenerator:

    def __init__(self, height, width):
        '''
        A classe ImageGenerator é inicializada com as proporções passadas
        e é preenchida com um array tridimensional.
       
        Altura = height

        Largura = width

        Profundidade = 3 (R G B)
        '''
        self.width = width
        self.height = height
        self.image = np.zeros((height, width, 3))
        self.aspecRatio = width/height
    

    def saveImage(self, imageName):
        '''
        Salva a imagem no diretório "Imagens/" com o nome
        passado como argumento e extensão .png
        '''
        plt.imsave(f'Imagens/{imageName}.png', self.image)
    
    def fadeImageRGB(self):
        '''
        Cria uma imagem que consiste em um degradê de cores.
        '''
        for i in range(self.height):
            for j in range(self.width):
                newPixel = np.array([j/(self.width), 1 - i/self.height , 0.25])
                self.writePixel(newPixel, i, j)
    
    def writePixel(self, pixel, i, j):
        '''
        Sobre a posição i, j é escrito o pixel passado como argumento.
        '''
        self.image[i, j] = pixel


    def castRay(self, origin, screen, hittableList):
        '''
        Para cada pixel na tela,
        '''
        for i in range(self.height):
            print(f"{i}/{self.height}") # Apenas para contar a progressão
            
            for j in range(self.width):
                # u, v são coordenadas parametrizadas do plano de projeção.
                u = j / self.width
                v =  1 - i / self.height
                
                horizontalStep = Vector( screen.viewPortWidth, 0, 0) * u
                verticalStep = Vector(0, screen.viewPortHeight, 0) * v
                
                ray = Ray(source = origin, direction = screen.lowerLeft + horizontalStep + verticalStep - origin)
                newPixel = ray.getColor(hittableList)
                self.writePixel(newPixel, i, j)
