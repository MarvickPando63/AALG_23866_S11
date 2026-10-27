def imprime(sud):
    for x in sud:
        print(x)
    print()

def validar(sud, num, f, c):
    #si numero ya esta en fila
    if num in sud[f]: return False
    #sinumero ya esta en columna
    if any(sud[i][c] == num for i in range(9)): return False
    #any devuelve True si encuentra aunque sea una coincidencia
    #revisar inicio del 3x3
    f0,c0 = (f//3)*3, (c//3)*3   
    #si num ya esta en la matriz 3x3
    for i in range(f0,f0 + 3):
        for j in range(c0,c0 +3):
            if sud[i][j] == num: return False
    #si no estan en las anteriores
    return True
def fi_co_disponible(sud):
    #devuelve la siguiente f y c disp, 
    for f in range(9):
        for c in range(9):
            if sud[f][c] == 0:
                return f, c
    #sino -1
    return -1, -1

def sudoku(sud):
    #El fin del sudoku es que no haya f,c disponible
    #busca disponibles
    f,c = fi_co_disponible(sud)
    if f == -1: return True
    #probar num del 1-9
    for num in range(1,10):
        if validar(sud,num,f,c):
            #colocar temporalmente
            sud[f][c]=num
            #si el resto del sudoku se puede resolver
            if sudoku(sud): return True
            #si no funciona, backtracking
            sud[f][c]=0
    #si ningun numero funciona en la casilla, no hay solucion por este camino
    return False
    
sudo=[
    [0,6,0,1,0,4,0,5,0],
    [0,0,8,3,0,5,6,0,0],
    [2,0,0,0,0,0,0,0,1],
    [8,0,0,4,0,7,0,0,6],
    [0,0,6,0,0,0,3,0,0],
    [7,0,0,9,0,1,0,0,4],
    [5,0,0,0,0,0,0,0,2],
    [0,0,7,2,0,6,9,0,0],
    [0,4,0,5,0,8,0,7,0]
]
if sudoku(sudo):
    print("Sudoku resuelto:")
    imprime(sudo)
else:
    print("No hubo solución")