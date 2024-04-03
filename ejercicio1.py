def weird_algorithm(n):
    # Creamos un rango de n si es invalido imprimara un mensaje del error si es valido seguira la secuencia
    if n <= 0 or n > 1000000:
        print("rango invalido")
        return "rango invalido"
    #creamos un array donde se guardara todos los valores durante el proceso, incluido el numero que le pasamos
    array=[n]
    #Mientras n diferente de 1 se seguira ejecutando
    while n!=1:
    #Si el resto da 0 se dividira por 2 el numero
        if n % 2 == 0:
            n //= 2
    #Si el resto da diferente de 0 se multiplicara por 3 y se sumara 1
        else: 
            n = n * 3 + 1
    #Se agrega al array los valores
        array.append(n)
    print(array)
    return array


# caso de prueba
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
assert weird_algorithm(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
assert weird_algorithm(2) == [2, 1], "Error en el caso de prueba"
assert weird_algorithm(32) == [32, 16, 8, 4, 2, 1], "Error en el caso de prueba"
assert weird_algorithm(0) == "rango invalido", "Error en el caso de prueba"
assert weird_algorithm(1000000000) == "rango invalido", "Error en el caso de prueba"






   
