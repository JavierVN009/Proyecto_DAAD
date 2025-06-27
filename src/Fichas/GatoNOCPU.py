from .Gato import Gato

class GatoNOCPU(Gato):
    def __init__(self, pos):
        super().__init__(pos)

    def moverGato(self, arr):
        if(len(arr) == 0):
            print("Tu gato no se puede mover")
            pass
        
        elif(len(arr) == 1):
            print("tu gato solo tiene un movimiento a la casilla: ")
            print("    " + arr[0] + "\n")
            print("¿Quieres moverlo o mejor pasas de turno?: \n [1] Quiero moverlo \n [2] Mejor paso\n")
            #// $$ Vamos a leer las entradas del carnal, a ver si hace todo bien
            ayu5 = input("opcion: ")
            op5 = ayu5[0]
            ## // $$ Si la opcion es incorrecta
            if(op5 != '1' or op5 != '2'):
            ## // $$ metelo a un ciclo hasta que ponga lo correcto por favor!!! (o hasta que mate el programa, tambien jala)
                while(op5 != '1' or op5 != '2'):
                    if(op5 == '1'): 
                        break
                    if(op5 == '2'): 
                        break
                    print("ESCRIBE \'1\' O \'2\', ¿Que es eso de poner: " + ayu5 + " ?")
                    print("\n[1] SI ME MUEVO\n[2] NO ME MUEVO\n")
                    ayu5 = input("opcion: ")
                    op5 = ayu5[0]
            
            if(op5 == '1'):     ## //$$ pos lo movemos
                self.asignarPosicion([arr[0][0], arr[0][1]])
            
            
        else:
            print("tu gato solo se puede mover a las siguientes casillas: ")
            for i in range(len(arr)):
                if(i == len(arr) - 1):
                    print("  " + arr[i])
                    
                else:
                    print("  " + arr[i] + ",", end = "")
                    
            print("¿Vas a querer moverlo a la casilla " + arr[0] + ", a la casilla " + arr[1] + " o prefieres saltar tu turno?: \n[1] mover a la casilla " + arr[0] + "\n[2] mover a la casilla " + arr[1] + "\n[3] saltar turno\n")
			## // $$ Vamos a leer las entradas del carnal, a ver si hace todo bien
            ayu5 = input("opcion: ")
            op5 = ayu5[0]
			
            ## // $$ Si la opcion es incorrecta
            if(op5 != '1' or op5 != '2' or op5 != '3'):
				## // $$ metelo a un ciclo hasta que ponga lo correcto por favor!!! (o hasta que mate el programa, tambien jala)
            	while(op5 != '1' or op5 != '2'):
                    if(op5 == '1'):
                        break
                    if(op5 == '2'):
                        break
                    if(op5 == '3'):
                        break
                    print("ESCRIBE \'1\', \'2\' O \'3\', ?Que es eso de poner: " + ayu5 + " ?")
                    print("\n[1] MOVER A: " + arr[0] + "\n[2] MOVER A: " + arr[1] + "\n[3] NO ME MUEVO\n")
                    ayu5 = input("opcion: ")
                    op5 = ayu5[0]
            
            if(op5 == '1'):     ## //$$ pos lo movemos a la casilla esa
                self.asignarPosicion([arr[0][0], arr[0][1]])
        
            elif(op5 == '2'):    ## //$$ Lo movemos a la otra casilla entonces
                self.asignarPosicion([arr[1][0], arr[1][1]])
            


