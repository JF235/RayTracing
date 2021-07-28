from Vector import *

class Screen():
    def __init__(self, verticalSize, aspectRatio, cameraDistance):
        '''
        A tela é inicializada com os parâmetros

        verticalSize atribui valor para self.viewPortHeight (tamanho vertical)

        aspectRatio é responsável por controlar a proporcionalidade
        e salvar o atributo self.viewPortWidth (tamanho horizontal)

        cameraDistance é a distância entre a camera e a tela descrita por
        self.focalLength
        '''
        self.viewPortHeight = verticalSize # Tamanho Vertical da tela (diferente dos pixels)
        self.viewPortWidth = aspectRatio * verticalSize # Tamanho Horizontal da tela
        self.focalLength = cameraDistance # Distancia da Camera até a tela
    
    def calculateLowerLeft(self, origin):
        '''
        Calcula o vetor que corresponde ao canto inferior esquerdo
        da tela e associa ao atributo self.lowerLeft
        '''
        horizontalStep = Vector(self.viewPortWidth, 0, 0) * 0.5
        verticalStep = Vector(0, self.viewPortHeight, 0) * 0.5
        stepToScreen = Vector(0, 0, self.focalLength) 
        self.lowerLeft =  (origin - horizontalStep - verticalStep - stepToScreen)