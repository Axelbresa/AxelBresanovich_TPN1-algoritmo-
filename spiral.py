def encontrar_valor(matriz, fila, columna):
    if fila < 1 or fila > len(matriz) or columna < 1 or columna > len(matriz[0]):
        return None  
    else:
        return matriz[fila - 1][columna - 1]

def longitud_array():
    n = 25  
    lado = int(n ** 0.5) + 1 if (n ** 0.5) % 1 != 0 else int(n ** 0.5)
    print("lado:", lado)

    arrays = []
    for i in range(1, n + 1):
        if i%2==0:
            arrays.append(i)
        else:
            arrays.append(i)

    matriz = [arrays[i * lado : (i + 1) * lado] for i in range(lado)]
    reordenar_matriz_espiral(matriz)


def reordenar_matriz_espiral(matriz):
    for i, fila in enumerate(matriz, start=1):
        print("Fila:", i)
        for j, elemento in enumerate(fila, start=1):
            if elemento == 3:
                i += 1  
                print(f"P ({i}, {j}): {elemento}", end=" ")
                break  
            print(f"P ({i}, {j}): {elemento}", end=" ")
        print()
    valor_buscado(matriz)


def valor_buscado(matriz):
    fila_buscar = 2
    columna_buscar = 1

    valor_encontrado = encontrar_valor(matriz, fila_buscar, columna_buscar)

    if valor_encontrado is not None:
        print(f"El valor en la fila {fila_buscar} y columna {columna_buscar} es: {valor_encontrado}")
        diseño_array(matriz)
    else:
        print("La fila o columna especificada está fuera de rango.")

def diseño_array(matriz):
     print("Diseño de la matriz: ")
     for fila in matriz:
        for elemento in fila:
                print(elemento, end=" ")
        print()  

longitud_array()
