def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) for num in fila))


def encontrar_vacio(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                return fila, col
    return None


def es_valido(tablero, num, pos):
    fila, col = pos

    # Verificar fila
    for j in range(9):
        if tablero[fila][j] == num and j != col:
            return False

    # Verificar columna
    for i in range(9):
        if tablero[i][col] == num and i != fila:
            return False

    # Verificar subcuadrícula 3x3
    caja_fila = fila // 3
    caja_col = col // 3

    for i in range(caja_fila * 3, caja_fila * 3 + 3):
        for j in range(caja_col * 3, caja_col * 3 + 3):
            if tablero[i][j] == num and (i, j) != pos:
                return False

    return True


def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)

    # Caso base: no quedan casillas vacías
    if not vacio:
        return True

    fila, col = vacio

    # Probar números del 1 al 9
    for num in range(1, 10):
        if es_valido(tablero, num, (fila, col)):
            tablero[fila][col] = num

            # Llamada recursiva
            if resolver_sudoku(tablero):
                return True

            # Backtracking
            tablero[fila][col] = 0

    return False


# Ejemplo de Sudoku (0 representa casillas vacías)
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku original:")
mostrar_tablero(tablero)

if resolver_sudoku(tablero):
    print("\nSudoku resuelto:")
    mostrar_tablero(tablero)
else:
    print("No existe solución.")