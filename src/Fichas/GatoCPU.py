from random import randrange 
from .Gato import Gato

class GatoCPU(Gato):
    def __init__(self, pos):
        super().__init__(pos)
        
    def moverGato(self, arr):
        if(len(arr) == 0):
            pass
            
        elif(len(arr) == 1):
            self.asignarPosicion([arr[0][0], arr[0][1]])
            
        else:
            rand = randrange(2)
            if(rand == 0):
                self.asignarPosicion([arr[0][0], arr[0][1]])
            else:
                self.asignarPosicion([arr[1][0], arr[1][1]])





