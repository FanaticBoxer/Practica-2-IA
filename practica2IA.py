#import numpy as np

    #COLOCAR CABALLOS
def colocarCaballo(tablero, fila, columna):
    if (0 <= fila < len(tablero) and 0 <= columna < len(tablero[0])):
        tablero[fila][columna]='k'
        list [(1,2),(2,1),(2,-1),(1,-2)(-1,-2),(-2,-1)(-2,1)(-1,2)]
    else: print ("Fuera de los limites")

    
    #COSTE DE UN CAMINO = CASILLAS LIBRES QUE ATACA EL NUEVO CABALLO
    
def main():
    
    # DIMENSIONES DEL TABLERO
    N = 8
    M = 8

    # CREA EL TABLERO CON TODO 0s
    tablero = [[0 for _ in range(M)] for _ in range(N)]

    # Imprimir la matriz para verificar que está inicializada correctamente
    for fila in tablero:
        print(fila)

    colocarCaballo(tablero, 3, 3) 
    print ("ESTADO NUMERO 1")
    for fila in tablero:
        print(" ".join(f"{elem:>2}" for elem in fila))#(imprimir con formato)
        
        
main()