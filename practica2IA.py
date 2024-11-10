import numpy as np

def initial_state (M, N):
    board = np.zeros((M, N), dtype=object)
    return board



#DEVUELVE LISTA DE CASILLAS ATACADAS
def attackedSquares(board, row, col):
    attacked=[]
    attacks = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
    
    for atq in attacks:
        attackRow = row + atq[0]
        attackCol = col + atq[1]
        if 0 <= attackRow < board.shape[0] and 0 <= attackCol < board.shape[1]:
            attacked.append((attackRow, attackCol))
    return attacked



#DEVUELVE NUEVO TABLERO CON CABALLO COLOCADO
def placeKnight(board, row, col):
    new_board = np.copy(board)
    
    # Coloca el caballo
    new_board[row][col] = 'k'
    
    # Actualiza las casillas atacadas
    attacked = attackedSquares(new_board, row, col)
    for r, c in attacked:
        new_board[r][c] += 1  # +1 en las casillas que ataca el caballo
    
    return new_board



#DEVUELVE LA CANTIDAD DE UN ELEMENTO QUE HAY EN EL TABLERO
def elementCounter(board, element):
    c = 0
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if board[row][col] == element:
                c = c + 1
    return c



#DEVUELVE LISTA DE EXPANSIONES
def expand(board):
    boards = []
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if board[row][col] == 0: #evita el ataque entre caballos
                new = placeKnight(board, row, col)
                boards.append(new)
    return boards



#BOOL QUE DEVUELVE SI EL TABLERO ES SOLUCION
def is_solution(board):
    sol = False
    knights = elementCounter(board, 'k')
    row = board.shape[0]
    col = board.shape[1]
    
    if row*col <= 4: #Para tableros 2x2 o más pequeños
        if knights == row*col:
            sol = True
            
    elif (row*col) == 6: #Para tableros 2x3 (excepcion de los tableros pares)
    	if knights == 4:
            sol = True
            
    elif (row*col) % 2 == 1: #Para tableros de casillas impares
    	if knights == row*col // 2 + 1:
            sol = True
	
    else:
    	if knights == row * col // 2: #Para tableros de casillas pares
            sol = True
    
    return sol
    


#COSTE DE PASAR DE UN ESTADO A OTRO =
# = 1 + 0s QUE ATACA EL CABALLO - 0,1* CASILLAS YA ATACADAS QUE ATACA EL ULTIMO CABALLO.
def cost(path):
    if len(path) == 0:
        return 0
    
    c = 1.0
    
    for estado_0, estado_1 in zip(path[: -1], path[1: ]): #se emparejan los estados de dos en dos.
        
        for i in range(estado_0.shape[0]):
            for j in range(estado_0.shape[1]):

                if estado_1[i][j] == 1 and estado_0[i][j] == 0:
                    c = c+1 # sumar las casillas atacadas en el cambio de estado
                    
                elif estado_1[i][j] != 'k' and estado_1[i][j] > 1 and estado_1[i][j] > estado_0[i][j]:
                    c = c-0.1 # Contar las casillas atacadas por el ultimo caballo que ya lo estuvieran
    return c



#heurística = casillas libres (sin caballos ni ataques)
def heuristic(board):
    return elementCounter(board, 0)



#
def eq(a, b):
  return np.array_equal(a,b)



 # Si detecta que dos caminos llevan al mismo estado,
 # solo nos interesa aquel camino de menor coste
 # Más adelante usamos la poda despues de ordenar
def prune(): #suponemos que están ordenados por coste
    resto = []


    return resto
    


def main():
    board = initial_state(8, 8)
    
    path = [] 
    path.append(np.copy(board))
    

    #COLOCA CABALLO, PONE A +1 SUS ATAQUES Y AÑADE ESTADO A path
    board = placeKnight(board, 0, 5)
    exp = expand(board)
    placeKnight(board, 2, 2)
    placeKnight(board, 0, 0)
    placeKnight(board, 0, 2)
    
    
        
            
    print("\nEXPANSIONES:")
    for idx, estado in enumerate(exp):
        print(f"\nEstado {idx}:")
        for row in estado:
            print(" ".join(f"{elem:>2}" for elem in row))


main()


def poda(caminos): # suponemos que están ordenados por coste
  res = []
  nodos = [np.zeros(shape=(3,3))] # Dummy para que no de errores
  for c in caminos:
    if not np.any(np.all(c[0] == nodos, axis=(1, 2))): # si no ha sido alcanzado
      nodos.append(c[0])
      res.append(c)
  return res



