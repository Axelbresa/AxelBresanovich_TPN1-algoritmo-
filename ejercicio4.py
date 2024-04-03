def reorganizar_palindromo(cadena):
    # Creamos un rango de n si es invalido imprimara un mensaje del error si es valido seguira la secuencia
    if not 1 <= len(cadena) <= 1000000:
        print("RANGO INVÁLIDO")
        return "RANGO INVÁLIDO"

# Verificar que la cadena solo contenga letras minúsculas del alfabeto inglés
    for caracter in cadena:
        if not 'a' <= caracter <= 'z':
            print("CARACTERES INVÁLIDOS")
            return "CARACTERES INVÁLIDOS"

    # Contador de caracteres
    contador_caracteres = {}
    for caracter in cadena:
        contador_caracteres[caracter] = contador_caracteres.get(caracter, 0) + 1
    
    # Contador de caracteres con conteo impar
    conteo_impar = 0
    caracter_impar = ''
    for caracter, conteo in contador_caracteres.items():
        if conteo % 2 != 0:
            conteo_impar += 1
            caracter_impar = caracter
    
    # Si hay más de un carácter con conteo impar, no es posible formar un palíndromo
    if conteo_impar > 1:
        print("NO SOLUTION")
        return "NO SOLUTION"
    
    # Construir la mitad del palíndromo
    mitad_palindromo = ''
    for caracter, conteo in contador_caracteres.items():
        mitad_palindromo += caracter * (conteo // 2)
    
    # Armar el palíndromo completo
    palindromo = mitad_palindromo + caracter_impar + mitad_palindromo[::-1]
    print("palindromo:", palindromo)
    return palindromo

# Verificar con assert
assert reorganizar_palindromo("") == "RANGO INVÁLIDO", "Error en el caso de prueba"
assert reorganizar_palindromo("aabbc") == "abcba", "Error en el caso de prueba"
assert reorganizar_palindromo("baa") == "aba", "Error en el caso de prueba"
assert reorganizar_palindromo("baae") == "NO SOLUTION", "Error en el caso de prueba"
assert reorganizar_palindromo("OSO") == "CARACTERES INVÁLIDOS", "Error en el caso de prueba"
assert reorganizar_palindromo("ñoñ") == "CARACTERES INVÁLIDOS", "Error en el caso de prueba"


