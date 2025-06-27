import abc

class Ajedrez(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def posiblesMovimientos(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Ajedrez:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented

    def __init__(self, posicion, color):
        self.posicion = posicion     # La posición donde se encuentra la ficha
        self.color = color          #El color de la ficha (blanca o negra)
        self.movimientos = 2        #cantidad de movimientos que podemos dar depende la posición donde nos encontremos.
        
    def obtenerPosicion(self):
        return self.posicion

    def obtenerColor(self):
        return self.color

    def obtenerMovimientos(self):
        return self.movimientos

    def asignarPosicion(self, pos):
        self.posicion = pos[0] + pos[1]
        #self.posicion[0] = pos[0]
        #self.posicion[1] = pos[1]

    def asignarMovimientos(self, mov):
        self.movimientos = mov

    def asignarColor(self, col):
        self.color = col

#MAIN
'''
raton = Raton("G6")
print("RATON")
print(raton.obtenerPosicion())
print(raton.obtenerMovimientos())
print(raton.obtenerColor())
gato1 = GatoNOCPU("E3")
gato2 = GatoCPU("H4")
gato3 = GatoNOCPU("H6")
gato4 = GatoCPU("C8")
gatos = [gato1, gato2, gato3, gato4]
print("\nGatoNoCPU")
print(gato1.obtenerPosicion())
print(gato1.obtenerMovimientos())
print(gato1.obtenerColor())
print("\nGatoCPU")
print(gato2.obtenerPosicion())
print(gato2.obtenerMovimientos())
print(gato2.obtenerColor())
print("\nGatoNoCPU")
print(gato3.obtenerPosicion())
print(gato3.obtenerMovimientos())
print(gato3.obtenerColor())
print("\nGatoCPU")
print(gato4.obtenerPosicion())
print(gato4.obtenerMovimientos())
print(gato4.obtenerColor())
print("\n"*2)
print("POSIBLES MOVIMIENTOS (en principio)")
print(raton.posiblesMovimientos())
print(gato1.posiblesMovimientos())
print(gato2.posiblesMovimientos())
print(gato3.posiblesMovimientos())
print(gato4.posiblesMovimientos())
print("\n"*2)
print("POSIBLES MOVIMIENTOS RATON")
print(raton.casillasRaton(raton.posiblesMovimientos(), gatos))
print("\n"*2)
print("POSIBLES MOVIMIENTOS GATOS")
print(gato1.casillasGatos(gato1.posiblesMovimientos(), gatos, 0))
print(gato2.casillasGatos(gato2.posiblesMovimientos(), gatos, 1))
print(gato3.casillasGatos(gato3.posiblesMovimientos(), gatos, 2))
print(gato4.casillasGatos(gato4.posiblesMovimientos(), gatos, 3))
print("\nMovemos los gatos CPU\n")
print("posicion actual")
print(gato2.obtenerPosicion())
print(gato4.obtenerPosicion())
print("posicion movido")
gato2.moverGato(gato2.casillasGatos(gato2.posiblesMovimientos(), gatos, 1))
gato4.moverGato(gato4.casillasGatos(gato4.posiblesMovimientos(), gatos, 1))
print(gato2.obtenerPosicion())
print(gato4.obtenerPosicion())
print("Vemos sus nuevos posibles movimientos")
print(gato2.casillasGatos(gato2.posiblesMovimientos(), gatos, 1))
print(gato4.casillasGatos(gato4.posiblesMovimientos(), gatos, 3))
print("Los volvemos a mover")
gato2.moverGato(gato2.casillasGatos(gato2.posiblesMovimientos(), gatos, 1))
gato4.moverGato(gato4.casillasGatos(gato4.posiblesMovimientos(), gatos, 1))
print(gato2.obtenerPosicion())
print(gato4.obtenerPosicion())
print("Y vemos por ultima vez sus nuevos posibles movimientos")
print(gato2.casillasGatos(gato2.posiblesMovimientos(), gatos, 1))
print(gato4.casillasGatos(gato4.posiblesMovimientos(), gatos, 3))
print("Finalmente, movemos a los gatos que son No CPU")
print("\nMovemos los gatos NO CPU\n")
print("posicion actual")
print(gato1.obtenerPosicion())
print(gato3.obtenerPosicion())
print("posicion movido")
gato1.moverGato(gato1.casillasGatos(gato1.posiblesMovimientos(), gatos, 1))
gato3.moverGato(gato3.casillasGatos(gato3.posiblesMovimientos(), gatos, 1))
print(gato1.obtenerPosicion())
print(gato3.obtenerPosicion())
print("Vemos sus nuevos posibles movimientos")
print(gato1.casillasGatos(gato2.posiblesMovimientos(), gatos, 1))
print(gato3.casillasGatos(gato4.posiblesMovimientos(), gatos, 3))
print("\n\n Y YA ACABAMOS!!!")'''





