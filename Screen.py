from Vector import Vector

class Screen():
    def __init__(self, verticalSize, aspectRatio, cameraDistance):
        self.viewPortHeight = verticalSize # Tamanho Vertical da tela
        self.viewPortWidth = aspectRatio * verticalSize # Tamanho Horizontal da tela
        self.focalLength = cameraDistance # Distancia da Camera até a tela
    
    def getLowerLeft(self, origin):
        horizontalStep = Vector(self.viewPortWidth, 0, 0) * 0.5
        verticalStep = Vector(0, self.viewPortHeight, 0) * 0.5
        stepToScreen = Vector(0, 0, self.focalLength) 
        self.lowerLeft =  (origin - horizontalStep - verticalStep - stepToScreen)