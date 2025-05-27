# PROGRAMACION 1 TRABAJO PRACTICO NUMERO 7 - RECURSIVIDAD
# Alumno: Martín Davidenco

# DECIDI HACER UN CONDICIONAL PARA LA EJECUCIÓN DE LAS ACTIVIDADES, INGRESANDO EL NUMERO DE LA ACTIVIDAD A EJECUTAR
ejercicio = int(input("Escribe el número del ejercicio a ejecutar (Del 1 al 8) ")) # Ajustado al TP

if ejercicio == 1:
    print(f"Ejercicio 1: Factorial")
    def factorial_recursivo(n):
        if n == 0:  # Caso base [cite: 6, 18]
            return 1
        else:  # Paso recursivo [cite: 6, 18]
            return n * factorial_recursivo(n - 1) # [cite: 6, 18]

    # Pedimos al usuario que ingrese un número
    try:
        numero_usuario = int(input("Ingresa un número entero para calcular los factoriales: "))
        if numero_usuario < 0:
            print("El factorial no está definido para números negativos.")
        else:
            print(f"\nCalculando factoriales desde 1 hasta {numero_usuario}:")
            for i in range(1, numero_usuario + 1): # El TP pide factorial de todos los números hasta el ingresado [cite: 50]
                print(f"El factorial de {i} es: {factorial_recursivo(i)}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

elif ejercicio == 2:
    print(f"Ejercicio 2: Fibonacci")
    def fibonacci_recursivo(posicion):
        if posicion == 0:  # Caso base [cite: 34]
            return 0
        elif posicion == 1:  # Caso base [cite: 34]
            return 1
        else:  # Paso recursivo
            return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2) # [cite: 34]

    try:
        posicion_usuario = int(input("Ingresa la posición hasta la cual deseas ver la serie de Fibonacci: "))
        if posicion_usuario < 0:
            print("La posición debe ser un número no negativo.")
        else:
            print(f"\nSerie de Fibonacci hasta la posición {posicion_usuario}:") # [cite: 51]
            for i in range(posicion_usuario + 1):
                print(f"F({i}) = {fibonacci_recursivo(i)}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

elif ejercicio == 3:
    print(f"Ejercicio 3: Potencia")
    def potencia_recursiva(base, exponente):
        if exponente == 0:  # Caso base
            return 1
        # La fórmula n^m = n * n^(m-1) es para m > 0 [cite: 52]
        elif exponente < 0: 
            # El TP no lo pide, pero por si las moscas
            return 1 / potencia_recursiva(base, -exponente)
        else:  # Paso recursivo
            return base * potencia_recursiva(base, exponente - 1) # [cite: 52]

    try:
        base_usuario = float(input("Ingresa el número base: "))
        exponente_usuario = int(input("Ingresa el exponente (entero): "))

        resultado = potencia_recursiva(base_usuario, exponente_usuario)
        print(f"{base_usuario} elevado a {exponente_usuario} es: {resultado}")

    except ValueError:
        print("Por favor, ingresa números válidos.")

elif ejercicio == 4:
    print(f"Ejercicio 4: Decimal a Binario")
    def decimal_a_binario_recursivo(numero): # [cite: 54]
        if numero < 0:
            return "Debe ser un número positivo"
        # El proceso se repite hasta que el cociente llegue a 0 [cite: 55]
        # Cuando el cociente es 0, el número original era 0 o 1.
        if numero // 2 == 0:  # Caso base
            return str(numero % 2)
        else:  # Paso recursivo
            # Los restos leídos de abajo hacia arriba forman el binario [cite: 55]
            # Así que el resto actual va al final
            return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)

    try:
        num_decimal = int(input("Ingresa un número entero positivo para convertir a binario: "))
        if num_decimal < 0:
            print("El número debe ser positivo.")
        elif num_decimal == 0: # Caso especial para el 0
            print(f"El binario de {num_decimal} es: 0")
        else:
            binario_resultado = decimal_a_binario_recursivo(num_decimal)
            print(f"El binario de {num_decimal} es: {binario_resultado}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

elif ejercicio == 5:
    print(f"Ejercicio 5: Palíndromo")
    def es_palindromo_recursivo(palabra): # [cite: 58]
        # palabra = palabra.lower().replace(" ", "") # El TP dice sin espacios ni tildes [cite: 58]
        longitud = len(palabra)

        if longitud <= 1:  # Caso base: palabra vacía o de una letra
            return True
        else:
            if palabra[0] == palabra[longitud - 1]:  # Compara el primer y último carácter
                # Paso recursivo: con la subcadena interior
                return es_palindromo_recursivo(palabra[1:longitud - 1])
            else:
                return False # No es palíndromo

    palabra_ingresada = input("Ingresa una palabra para ver si es palíndromo (sin espacios ni tildes): ")
    if es_palindromo_recursivo(palabra_ingresada):
        print(f"'{palabra_ingresada}' SÍ es un palíndromo.")
    else:
        print(f"'{palabra_ingresada}' NO es un palíndromo.")


elif ejercicio == 6:
    print(f"Ejercicio 6: Suma de dígitos")
    def suma_digitos_recursivo(n): # [cite: 60]
        if n < 0:
            return "El número debe ser positivo" # El TP dice entero positivo [cite: 60]
        if n < 10:  # Caso base: el número tiene un solo dígito
            return n
        else:  # Paso recursivo
            ultimo_digito = n % 10 # Usar % y // [cite: 61]
            resto_del_numero = n // 10
            return ultimo_digito + suma_digitos_recursivo(resto_del_numero)

    try:
        num_ingresado = int(input("Ingresa un número entero positivo para sumar sus dígitos: "))
        if num_ingresado < 0:
            print("Tiene que ser positivo che.")
        else:
            print(f"La suma de los dígitos de {num_ingresado} es: {suma_digitos_recursivo(num_ingresado)}")
    except ValueError:
        print("Dije NÚMERO entero.")


elif ejercicio == 7:
    print(f"Ejercicio 7: Pirámide de bloques")
    def contar_bloques_recursivo(n_base): # [cite: 64]
        if n_base <= 0: # Si n es 0 o negativo, no hay bloques.
            return 0
        if n_base == 1:  # Caso base: último nivel con un solo bloque [cite: 63]
            return 1
        else:  # Paso recursivo
            # n bloques en el nivel actual + bloques del nivel anterior (n-1) [cite: 63]
            return n_base + contar_bloques_recursivo(n_base - 1)

    try:
        bloques_base = int(input("Ingresa el número de bloques en el nivel más bajo de la pirámide: "))
        if bloques_base < 0:
            print("No se puede con bloques negativos...")
        else:
            print(f"Se necesitan {contar_bloques_recursivo(bloques_base)} bloques en total.")
    except ValueError:
        print("Un número de bloques, porfa.")


elif ejercicio == 8:
    print(f"Ejercicio 8: Contar dígito en un número")
    def contar_digito_recursivo(numero, digito_buscado): # [cite: 66]
        if numero < 0:
            return "El número debe ser positivo" # El TP dice entero positivo [cite: 66]
        if digito_buscado < 0 or digito_buscado > 9:
            return "El dígito a buscar debe estar entre 0 y 9"

        if numero < 10:  # Caso base: número de un solo dígito
            return 1 if numero == digito_buscado else 0
        else:  # Paso recursivo
            ultimo_digito_del_numero = numero % 10
            coincide = 0
            if ultimo_digito_del_numero == digito_buscado:
                coincide = 1
            
            return coincide + contar_digito_recursivo(numero // 10, digito_buscado)
    
    try:
        num_principal = int(input("Ingresa el número entero positivo: "))
        dig_a_buscar = int(input("Ingresa el dígito (0-9) a contar: "))

        if num_principal < 0:
            print("El número grande tiene que ser positivo.")
        elif not (0 <= dig_a_buscar <= 9):
            print("El dígito a buscar tiene que ser entre 0 y 9.")
        else:
            veces = contar_digito_recursivo(num_principal, dig_a_buscar)
            print(f"El dígito {dig_a_buscar} aparece {veces} veces en el número {num_principal}.")
    except ValueError:
        print("Ingresaste algo que no era un número, probá de nuevo.")


   

else:
    print("Escribe un numero valido de ejercicio (1 al 8).")