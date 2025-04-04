#PROGRAMACION 1 TRABAJO PRCTICO NUMERO 3 - ESTRUCTURAS CONDICIONALES
# Alumno: Martín Davidenco
#DECIDI HACER UN CONDICIONAL PARA LA EJECUCIÓN DE LAS ACTIVIDADES, INGRESANDO EL NUMERO DE LA ACTIVIDAD A EJECUTAR

ejercicio = int(input("Escribe el número del ejercicio a ejecutar (Del 1 al 9) "))

if ejercicio == 1:
    print(f"Ejercicio 1:")
    edad = int(input("Ingrese su edad "))
    if edad >= 18:
        print("Es mayor de edad")

elif ejercicio == 2:
    print(f"Ejercicio 2:")
    nota = int(input("Ingrese su nota "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Reprobado")

elif ejercicio == 3:
    print(f"Ejercicio 3:")
    numero = int(input("Ingrese un número "))
    if numero % 2 == 0:
        print("Es un número par")
    else: print("Por favor, ingrese un número par")

elif ejercicio == 4:
    print(f"Ejercicio 4:")
    edad = int(input("Ingrese su edad "))
    if edad < 12 and edad > 0:
        print("Usted es un niño")
    elif edad >= 12 and edad < 18:
        print("Usted es un adolescente")
    elif edad >= 18 and edad < 30:
        print("Usted es un joven adulto")
    elif edad >= 30:
        print("Usted es un adulto")
    else: 
        print("ingresa un numero valido")    

elif ejercicio == 5:
    print(f"Ejercicio 5:")
    password = input("Ingrese una contraseña ")
    if len(password) >= 8 and len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        
elif ejercicio == 6:
    print(f"Ejercicio 6:")
    from statistics import mode, median, mean
    import random
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    print(f"Media = {media}, mediana = {mediana}, moda = {moda}")
    if media > mediana and mediana > moda:
        print("Hay sesgo positivo")
    elif media < mediana and mediana < moda:
        print("Hay sesgo negativo")
    elif media == moda and media == mediana:
        print("No hay sesgo")
    else:
        print("ERROR")

elif ejercicio == 7:
    print(f"Ejercicio 7:")
    escribe = input("Escribe una frase o palabra ")
    if escribe[-1] == "a" or escribe[-1] == "e" or escribe[-1] == "i" or escribe[-1] == "o" or escribe[-1] == "u" :
        print(f"{escribe}!")
    else:
        print(escribe)

elif ejercicio == 8:
    print(f"Ejercicio 8:")
    nombre = input("Ingrese su nombre ")
    opcion = int(input("Ingrese: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. "))
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.capitalize())
    else:
        print("ingresa un numero valido")

elif ejercicio == 9:
    print(f"Ejercicio 9:")
    magnitud = int(input("Ingrese la magnitud del terremoto "))
    if magnitud < 3:
        print("Muy leve (imperceptible).")
    elif magnitud >= 3:
        print("Leve (ligeramente perceptible).")
    elif magnitud >= 4 and magnitud < 5 :
        print("Moderado (sentido por personas, pero generalmente no causa daños).")
    elif magnitud >=5 and magnitud < 6 :
        print("Fuerte (puede causar daños en estructuras débiles).")
    elif magnitud >=6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos).")
    elif magnitud >= 7:
        print ("Extremo (puede causar graves daños a gran escala).")

elif ejercicio == 10:
    print(f"Ejercicio 10")
    hemisferio = input("Ingrese el hemisferio (N/S): ").strip().upper()
    mes = int(input("Ingrese el número del mes (1-12): "))
    dia = int(input("Ingrese el día del mes: "))
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    elif hemisferio == "S":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
            estacion = "Invierno"
        else:
            estacion = "Primavera"
    else:
        estacion = "Hemisferio no válido"
    print(f"La estación correspondiente es: {estacion}")

else:
    print("escribe un numero valido de ejercicio")
