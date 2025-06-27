import abc
from Tablero.Ajedrez import Ajedrez

class Gato(Ajedrez, metaclass = abc.ABCMeta):
    def __init__(self, pos):
        super().__init__(pos, "negro")
    
    def posiblesMovimientos(self):
        cad = [" " for i in range(self.movimientos)]
        aux = int(self.posicion[1]) - 1
        if( (self.posicion[0].upper()  == 'H') or (self.posicion[0].upper()  == 'A') ):
            #print("entre a este if")
            cad = [" "]
            cad[0] = ("G" + str(aux)) if (self.posicion[0].upper()  == 'H') else ("B" + str(aux))
            
            return cad

        #print("ya voy a darle sus movimientos")
        aux1 = ord(self.posicion[0].upper()) + 1
        aux2 = chr(aux1)
        cad[0] = aux2 + str(aux)
        
        aux3 = ord(self.posicion[0].upper()) - 1
        aux4 = chr(aux3)
        cad[1] = aux4 + str(aux)
        
        return cad;

    def casillasGatos(self, posibles2, gatos, num):
        elimino = 0
        auxilio = [" " for i in range(len(posibles2))]
        for i in range( len(posibles2) ):
			## vamos a ver la posicion de los otros gatos
            for j in range(len(gatos)):
				## guarda la casilla donde anda uno de los 4 gatos
                aiuda = gatos[j].obtenerPosicion()[0] + gatos[j].obtenerPosicion()[1]
                aiuda = aiuda.lower()
                
				## si la casilla donde esta el gato es justo uno de los movimientos posibles del otro gato
				## entonces me mentiste, no se puede mover ahí, quitalo con el metodo auxiliar.
				## ademas por supuesto, que no sea él mismo, sino ahi si de plano no se podría mover
                if(posibles2[i].lower() == aiuda and j != num):
                    auxilio = [" " for i in range(len(posibles2) - 1)]
                    auxilio = self.copiarArreglo(auxilio, self.eliminarElemento(posibles2, aiuda.upper()))
                    elimino += 1
        
        if(elimino != 0):
            posibles2 = [" " for i in range(len(auxilio))]
            posibles2 = self.copiarArreglo(posibles2, auxilio)
        
        return posibles2

    def eliminarElemento(self, arr, elem):
        aux = [" " for i in range(len(arr))]
        for i in range(len(arr)):
            aux[i] = arr[i]
        arr = [" " for i in range(len(arr) - 1)]
        for i in range(len(arr)):
            if(aux[i].upper() == elem):
                arr[i] = aux[i + 1]
            
            else:
                arr[i] = aux[i];
            
        return arr;

    def copiarArreglo(self, arr1, arr2):
        for i in range(len(arr1)):
            arr1[i] = arr2[i]

        return arr1

    @abc.abstractmethod
    def moverGato(self, arr, chat):
        pass
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Gato:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented






