def weird_algorithm(n):
    # Creamos un rango de n si es invalido imprimara un mensaje del error si es valido seguira la secuencia
    if n <= 0 or n > 1000000:
        raise ValueError("El valor de n debe estar en el rango de 1 a 1,000,000")
    else:
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
        return array


print(weird_algorithm(3))
# caso de prueba
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"




   
