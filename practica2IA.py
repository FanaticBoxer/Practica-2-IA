import copy
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




def colocarCaballo(tablero, fila, columna, caminos):
    if (0 <= fila < len(tablero) and 0 <= columna < len(tablero[0])):
        tablero[fila][columna]='k'
        
    atacadas = casillasAtacadas(tablero, fila, columna)
    for casilla in atacadas:
        tablero[casilla[0]][casilla[1]] += 1 #+1 a casillas que se ataquen
    
    caminos.append(copy.deepcopy(tablero)) #añade camino



#def poda:
    
    
#COSTE= 1 + 0s QUE ATACA EL CABALLO - 0,1* casillas ya atacadas que ataca el caballo.
def coste(caminos):#recibe como parametro una lista de los estados recorridos
    
    ultimo_estado = caminos [-1]
    penultimo_estado = caminos[-2]

    if len(caminos) == 1:
        return 0
    
    c = 1
    for i in range(N):
        for j in range(M):
            # Contar las casillas atacadas en el cambio de estado
            if ultimo_estado[i][j] == 1 and penultimo_estado[i][j] == 0:
                c = c+1
                
            # Contar las casillas atacadas por el ultimo caballo que ya lo estuvieran
            if ultimo_estado[i][j] != 'k' and ultimo_estado[i][j] > 1 and ultimo_estado[i][j] > penultimo_estado[i][j]:
                c= c-0.1
    return c


def main():

    # CREA EL TABLERO CON TODO 0s
    tablero = [[0 for _ in range(M)] for _ in range(N)]
    
    caminos = [] 
    caminos.append(copy.deepcopy(tablero))

    #COLOCA CABALLO, PONE A +1 SUS ATAQUES Y AÑADE ESTADO A CAMINOS
    colocarCaballo(tablero, 0, 5, caminos)
    colocarCaballo(tablero, 2, 2, caminos)
    colocarCaballo(tablero, 0, 0, caminos)
    colocarCaballo(tablero, 0, 2, caminos)
    
    print ("el coste de colocar el ultimo caballo ha sido", coste(caminos))
    
    for fila in tablero:
        print(" ".join(f"{elem:>2}" for elem in fila))#(imprimir con formato)
        
        
    #HISTORIAL DE ESTADOS
    print("\nHistorial de estados:")
    for idx, estado in enumerate(caminos):
        print(f"\nEstado {idx + 0}:")
        for fila in estado:
            print(" ".join(f"{elem:>2}" for elem in fila))

main()


