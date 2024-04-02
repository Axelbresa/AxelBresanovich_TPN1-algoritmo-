def encontrar_valor(matriz, fila, columna):
    #buscamos el valor del numero en esa fila y columna de la matriz, si no encuentra nada retorna none
    if fila < 1 or fila > len(matriz) or columna < 1 or columna > len(matriz[0]):
        return None  
    else:
        return matriz[fila - 1][columna - 1]

def number_spiral(fila, columna):
    #diseñamos nuestra matriz
    matriz = [
        [1, 2, 9, 10, 25],
        [4, 3, 8, 11, 24],
        [5, 6, 7, 12, 23],
        [16, 15, 14, 13, 22],
        [17, 18, 19, 20, 21]
    ]
    #llamamos a la funcion encontrar valor y la pasamos matriz, fila y columna
    valor_encontrado = encontrar_valor(matriz, fila, columna)

    #Hacemos un estructura condicional, si encuentra el valor imprime y si no, fila y columna fuera de rango 
    if valor_encontrado is not None:
        print(f"El valor en la fila {fila} y columna {columna} es: {valor_encontrado}")
    else:
        print("La fila o columna especificada está fuera de rango.")

    return valor_encontrado

#caso de prueba y llamamos a la funcion pasando fila y columna
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
