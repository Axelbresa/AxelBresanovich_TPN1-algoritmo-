def encontrar_faltante(n, numeros):
    #creamos un restriccion que si n no es mayor a 0 no continuara la secuencia
    if n <= 0:
       print("n debe ser mayor 0")
       return "n debe ser mayor 0"
    
    #suma el total de los numeros que te deberia dar
    suma_total = sum(range(1, n + 1))
    #suma de los numeros ingresados
    suma_dada = sum(numeros)
    #resta la suma total con las suma de los numeros ingresados para obtener el faltante
    numero_faltante = suma_total - suma_dada
    #imprimimos el valor del numero faltante
    print("numero faltante: ", numero_faltante)
    return numero_faltante

#caso de prueba
assert encontrar_faltante(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
assert encontrar_faltante(5, [1, 2, 3, 4]) == 5, "Error en el caso de prueba"
assert encontrar_faltante(-17, []) == "n debe ser mayor 0", "Error en el caso de prueba"
assert encontrar_faltante(0, []) == "n debe ser mayor 0", "Error en el caso de prueba"
assert encontrar_faltante(7, [1, 2, 3, 4, 5, 6]) == 7, "Error en el caso de prueba"
assert encontrar_faltante(10, [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Error en el caso de prueba"


