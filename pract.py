def encontrar_faltante(cantidad_elementos, numeros):
    suma_total = sum(range(1, cantidad_elementos + 1))
    suma_dada = sum(numeros)
    numero_faltante = suma_total - suma_dada
    return numero_faltante

def valores_numericos():
    cantidad_elementos=int(input("ingresa la cantidad de numeros: "))
    numeros=[]
    for i in range(cantidad_elementos):
        numero = int(input(f"Ingrese el valor del número {i + 1}: "))
        numeros.append(numero) 
        print("numeros: ", numeros)
    # cantidad_elementos = 5
    # numeros = [1, 2, 4, 5]  

    faltante = encontrar_faltante(cantidad_elementos, numeros)
    print("El número faltante es:", faltante)

valores_numericos()
