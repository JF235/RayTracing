from Vector import *
import numpy as np
from Sphere import *

class Ray:
    '''
    Documentacao de Raio
    '''

    def __init__(self, source, direction):
        '''
        Inicializa um raio a partir de dois vetores:

        source é o vetor que indica a fonte dos raios.

        direction é o vetor que indica a direção pelo qual o raio viaja.
        '''

        self.source = source
        self.direction = direction.normalize()

    def __repr__(self):
        return f'{self.source} + t {self.direction}'

    def getPoint(self, t = 0) -> Vector:
        return self.source + t * self.direction
    
    # Retorna a cor com relação a posição atingida
    def getColor(self, hittableList):
        '''
        É responsável por indicar a cor com relação a posição atingida.
        '''

        acertou = hittableList.hit(ray = self)
        
        if(acertou):
            # Aqui tem interseccao entao vou colorir a regiao
            # em que esta a esfera
            N = hittableList.hitRecord.normal
            return 0.5 * np.array([N.x + 1, N.y + 1, N.z + 1])
        else:
            direction = self.direction
            t = 0.5 * (direction.y + 1) # Quanto maior o valor de y maior é t...
            
            azul = np.array([0.5, 0.7, 1.0])
            branco = np.array([1,1,1])

            return (1 - t) * branco + t * azul # ... e quanto maior t mais azul ele fica.

