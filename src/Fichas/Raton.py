from Tablero.Ajedrez import Ajedrez

class Raton(Ajedrez):

    def __init__(self, pos):
        super().__init__(pos, "blanco")
    
    def posiblesMovimientos(self):
        cad = [" ", " "]
        aux = int(self.posicion[1]) + 1
        aux8 = int(self.posicion[1]) - 1
        if( (self.posicion[0].upper()  == 'H') or (self.posicion[0].upper()  == 'A') ):
            if(self.posicion[0].upper()  == 'H'):
                cad = [" "]
                cad[0] = "G" + str(aux)
            else:
                cad[0] = ("B" + str(aux))
                cad[1] = ("B" + str(aux8))
                if(cad[1][1] == "0"):
                    cad.pop()
                
        	
            return cad
			
        elif(int(self.posicion[1]) == 1):
            for i in range(len(cad)):
                if(i%2 == 0):
                    aux2 = ord(self.posicion[0]) + 1
                    aux3 = chr(aux2)
                    cad[i] = aux3 + str(aux)
                    
                else:
                    aux2 = ord(self.posicion[0]) - 1
                    aux3 = chr(aux2)
                    cad[i] = aux3 + str(aux)
			
            return cad
		
        cad = [" " for i in range(4)]
        aux1 = ord(self.posicion[0].upper()) + 1
        aux2 = chr(aux1)
        cad[0] = aux2 + str(aux)
		
        aux3 = ord(self.posicion[0].upper()) - 1
        aux4 = chr(aux3)
        cad[2] = aux4 + str(aux)
		
        aux = aux - 2;
        cad[1] = aux2 + str(aux)
        cad[3] = aux4 + str(aux)
        
        return cad

    def casillasRaton(self, posibles, gatos):
        eliminao = 0
        posiciones = []
        permitidos = []		

		## primero vamos a guardar los indices de los movimientos que no se valen
        for i in range(len(posibles)):
			## vamos a ver la posicion de los gatos
            for j in range(len(gatos)):
				## guarda la casilla donde anda uno de los 4 gatos
                aiuda = gatos[j].obtenerPosicion()[0] + gatos[j].obtenerPosicion()[1]
                aiuda = aiuda.lower()
				## si la casilla donde esta el gato es justo uno de los movimientos posibles del ratoncito
				## entonces me mentiste, no se puede mover ahi, guarda el indice con la posicion que no podemos mover.
                if(posibles[i].lower() == aiuda):
                    if(eliminao == 0):
                        eliminao += 1
                        posiciones = [" " for i in range(eliminao)]
                        posiciones[0] = i
    				
                    else:
                        auxiliar = [" " for i in range(eliminao)]
                        for r in range(len(auxiliar)):
                            auxiliar[r] = posiciones[r]
						
                        eliminao += 1
                        posiciones = [" " for i in range(eliminao)]
                        for m in range(len(posiciones)):
                            if(m == len(posiciones) - 1):
                                posiciones[m] = i
							
                            else:
                                posiciones[m] = auxiliar[m]

        
		## Si no hay posiciones a las que no pueda acceder (el arreglo de posicione es vacio), devuelve el arreglo de posibles movimientos completo
		## No hay nada que cambiar.
        if(len(posiciones) == 0):
            return posibles
		
		## Si hay posiciones a las que el ratoncito no se puede mover
        else:
			## calculamos el tamanio del nuevo arreglo que contendra los posibles movimientos del ratoncito con las casillas reales
            tamanio = len(posibles) - len(posiciones)
			
			## creamos el arreglo de los movimientos validos (permitidos vaya), con el tamaño calculado
            permitidos = [" " for i in range(tamanio)]
			
			## creamos un entero auxiliar que sirva como iterador sobre el que tengo un poquito más de control.
            k = 0
			
			
			## Ahora vamos a llenar el arreglo de los verdaderos movimientos permitidos (con dos for de los cuales uno está anidado)
            for i in range(len(posibles)):          ## recorremos los indices de los posibles movimientos totales
			
                for j in range(len(posiciones)):  ## recorremos el arreglo que tiene los indices de los movimientos que no son validos 
				
					## si el indice del posible movimiento coincide justo con el indice al que el ratoncito no se puede mover
                    if(i == posiciones[j]): 
					
                        if(k == len(permitidos)):     ## Esta condicional de aquí es porque sino se genera una excepción 
									      ## "ArrayIndexOutOfBounds"
							
                            if((k - 1) >= 0):     ## este es por un error muy particular muy raro que podría suceder, el indice se hace 
							                   ## negativo
                                if(i + 1 == len(posibles)):
                                    permitidos[k - 1] = posibles[i]
								
                                else:
                                    permitidos[k - 1] = posibles[i + 1]
                                    
                                break
							
						
						
						## Si todo sale bien, entonces no pasa nada	
                        if(len(permitidos) == 0):
                            return permitidos    ## Si mientras está jugando, se queda sin movimientos
									            ## permitidos, ya devuelvele su arreglo, ya perdio 
                        permitidos[k] = posibles[i + 1]
                        k += 1
						##break;                                         ## Los breaks son importantes, porque queremos que solo meta un 													      // elemento por vuelta del arreglo, y si no matamos el for
											     ## va a estar metiendo los elementos erroneamente.
											    ## para esto queria el entero auxiliar al que controlo un poquito mejor.
						
					
					
					## Si no coincide el indice, mete el elemento "normalmente" (orita vas a ver por que)
                    else:
                        if(k == 0):  ## Si es el primer elemento que metes, metelo normalmente.
                            permitidos[k] = posibles[i]
                            k += 1
                            break
							
						
                        else:  ## si ya tenias un elemento antes
                            if(not (permitidos[k - 1] == posibles[i])): ## por algun motivo que no entendía, siempre habia elementos  
							                                         ## repetidos, así que me vi obligado a comprobar que el proximo 
                    												 ## elemento que se agregara no fuera el mismo que el anterior.
                                if(k == len(permitidos)):    ## igual que la condicional anterior, esta permite evitar      
								                           ## la excepcion "ArrayIndexOutOfBounds"
                                    permitidos[k - 1] = posibles[i]
                                    break
								
								
								## Sino, puedes agregar el elemento normalmente,
                                permitidos[k] = posibles[i]
                                k += 1
								##break;             // Y de nuevo, este break es para que el elemento que se agregue sea unico en 
								 		  ## cada vuelta. 
							
						
					
			
				
			
			
			## Por fin le devolvemos el arreglo 
            return permitidos
		
	
 


# In[ ]:




