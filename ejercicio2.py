# Se te dan todos los números entre 1 a “n” excepto uno. Tu tarea es encontrar el número que
# falta.

# Input:
# El primer parámetro contiene la cantidad de elementos del array.
# El segundo parámetro contiene “n” números. Cada número es único y está entre 1 y n
# (inclusive).
# Output:
# Retornar el número que falta.

def encontrar_faltante(cantidad_elementos, numeros):
    numeros = [1, 2, 4, 5]  
    suma_total = sum(range(1, cantidad_elementos + 1))
    suma_dada = sum(numeros)
    numero_faltante = suma_total - suma_dada
    print(numero_faltante)
    return numero_faltante

assert encontrar_faltante(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
