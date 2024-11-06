#
#DIMENSIONES DEL TABLERO
N=8
M=8

    #DEVUELVE LISTA DE TOUPLES CON CASILLAS ATACADAS
def casillasAtacadas(tablero, fila, columna):
    atacadas=[]
    ataques = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
    
    for atq in ataques:
        ataqueFila = fila + atq[0]
        ataqueColumna = columna + atq[1]
    
        if 0 <= ataqueFila < N and 0 <= ataqueColumna < M:
            atacadas.append((ataqueFila, ataqueColumna))
    
    return atacadas




    #COLOCAR CABALLOS
def colocarCaballo(tablero, fila, columna):
    if (0 <= fila < len(tablero) and 0 <= columna < len(tablero[0])):
        tablero[fila][columna]='k'
        
    atacadas = casillasAtacadas(tablero, fila, columna)
    for casilla in atacadas:
        tablero[casilla[0]][casilla[1]] = 1

        
        
    
        


    
#COSTE DE UN CAMINO:
#

#def coste():


def main():


    # CREA EL TABLERO CON TODO 0s
    tablero = [[0 for _ in range(M)] for _ in range(N)]

    # Imprimir la matriz para verificar que está inicializada correctamente
    #for fila in tablero:
    #    print(fila)

    colocarCaballo(tablero, 3, 3) 
    print ("ESTADO NUMERO 1\n\n")
    for fila in tablero:
        print(" ".join(f"{elem:>2}" for elem in fila))#(imprimir con formato)
        
        
main()