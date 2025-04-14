# PROGRAMACION 1 TRABAJO PRACTICO NUMERO 4 - ESTRUCTURAS REPETITIVAS
# Alumno: Martín Davidenco

# DECIDI HACER UN CONDICIONAL PARA LA EJECUCIÓN DE LAS ACTIVIDADES, INGRESANDO EL NUMERO DE LA ACTIVIDAD A EJECUTAR

while True:
    ejercicio = int(input("Escribe el número del ejercicio a ejecutar (Del 1 al 10, o 0 para salir): "))

    if ejercicio == 0:
        print("Saliendo del programa.")
        break

    elif ejercicio == 1:
        print("Ejercicio 1:")
        contador = 0
        for num in range(1,101):
            contador += 1
            print(f"{contador}. {num}")

    elif ejercicio == 2:
        print("Ejercicio 2:")
        # código del ejercicio 2
        num = int(input("Escribe un número entero: "))
        num_manipulado = abs(num) 
        cant_digitos = 0

        while num_manipulado > 0:
            num_manipulado = num_manipulado // 10
            cant_digitos += 1

        print(f"El número {num} tiene {cant_digitos} dígito/s.")


    elif ejercicio == 3:
        print("Ejercicio 3:")
        # código del ejercicio 3
        num1 = int(input("Escribí un número entero: "))
        num2 = int(input("Escribí otro número entero: "))

        if num1 == num2:
            print("Los números deben ser distintos.")
        else:
            menor = min(num1, num2)
            mayor = max(num1, num2)
            suma = 0

            for i in range(menor + 1, mayor):  
                suma += i

            print(f"La suma de los números entre {num1} y {num2} es: {suma}")

    
    elif ejercicio == 4:
        print("Ejercicio 4:")
        # código del ejercicio 4
        numero = int(input("escribe un numero entero"))
        suma = 0
        while numero != 0:
            suma = suma + numero
            numero = int(input("escribe un numero entero , presion 0 para salir"))
        print(f"La suma total de enteros es {suma}")
    elif ejercicio == 5:
        print("Ejercicio 5:")
        # código del ejercicio 5
        import random
        aleatorio = random.randint(0,9)
        numero = -1
        intentos = 0
        while aleatorio != numero:
            numero = int(input("Adivina un numero del 0 al 9 "))
            intentos += 1
        print(f" Adivinaste en {intentos} intentos")
    elif ejercicio == 6:
        print("Ejercicio 6:")
        # código del ejercicio 6
        for num in range(100, -1, -1):
            print(num)

    elif ejercicio == 7:
        print("Ejercicio 7:")
        # código del ejercicio 7
        num = int(input("ingresa un numero entero positivo "))
        suma = 0
        for n in range(num + 1):
            suma = suma + n
        print(suma)
    elif ejercicio == 8:
        print("Ejercicio 8:")
        # código del ejercicio 8
        intentos = 10
        par = 0
        impar = 0
        for n in range (10):
            num = int(input("ingrese un entero "))
            if num % 2 == 0:
                par += 1
            else:
                impar += 1
        print(f"Se ingresaron {par} pares y {impar} impares")


    elif ejercicio == 9:
        print("Ejercicio 9:")
        # código del ejercicio 9
        intentos = 10
        suma = 0
        for n in range(intentos):
            num = int(input("ingresa un numero "))
            suma = num + suma
        print(f"El promedio de los unmero enteros ingresados es: {suma / intentos}")

    elif ejercicio == 10:
        print("Ejercicio 10:")
        # código del ejercicio 10
        num = int(input("ingresa un numero "))
        num_manipulado = num
        num_inversa = ""
        digito = 1
        while num_manipulado > 0:
            digito =  num_manipulado % 10
            num_inversa += str(digito)
            num_manipulado = num_manipulado // 10
        print(num_inversa)

    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 10 o 0 para salir.")
