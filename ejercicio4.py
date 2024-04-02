# Dada una cadena de caracteres, tu tarea es reorganizar los caracteres de la cadena de manera
# que puedas formar un palíndromo. Si no es posible formar un palíndromo, debes indicarlo.
# Input:
# El único parámetro contiene una cadena de caracteres de longitud n ( 1 ≤ n ≤ 10^6 ). La
# cadena solo contiene letras minúsculas del alfabeto inglés.
# Output:
# Retorna una cadena que represente un palíndromo formado reorganizando los caracteres de la
# cadena de entrada. Si no es posible formar un palíndromo, retorna "NO SOLUTION".

def invertir_palabra(palabra):
    palabra_inversa = ""    
    for i in palabra[::-1]:
        palabra_inversa += i
        polindromo(palabra_inversa, palabra)

def polindromo(palabra_inversa, palabra):
    print("palabra a la inversa", palabra_inversa)
    if palabra_inversa==palabra:
        print("Es un polindromo: ", palabra_inversa)
    else:
        print("No es un polindromo")

assert invertir_palabra("aabbc") == "abcba", "Error en el caso de prueba"




