# PROGRAMACION 1 TRABAJO PRACTICO NUMERO 5 - LISTAS
# Alumno: Martín Davidenco

# DECIDI HACER UN CONDICIONAL PARA LA EJECUCIÓN DE LAS ACTIVIDADES, INGRESANDO EL NUMERO DE LA ACTIVIDAD A EJECUTAR

while True:
    ejercicio = int(input("Escribe el número del ejercicio a ejecutar (Del 1 al 10, o 0 para salir): "))

    if ejercicio == 0:
        print("Saliendo del programa.")
        break

    elif ejercicio == 1:
        print("Ejercicio 1:")
        lista = list(range(0,100,4))
        print(lista)

    elif ejercicio == 2:
        print("Ejercicio 2:")
        # código del ejercicio 2
        penultimo = [1,2,3,4,5]
        print(penultimo[-2])


    elif ejercicio == 3:
        print("Ejercicio 3:")
        # código del ejercicio 3
        lista_vacia = []
        lista_vacia.append(1)
        lista_vacia.append(2)
        lista_vacia.append(3)
        print(lista_vacia)
    elif ejercicio == 4:
        print("Ejercicio 4:")
        # código del ejercicio 4
        animales = ["perro", "gato", "conejo", "pez"]
        animales[1] = "loro"
        animales[-1] = "oso"
        print(animales)
      
    elif ejercicio == 5:
        print("Ejercicio 5:")
        # código del ejercicio 5
        print("Define una lista llamada numeros con los valores [8, 15, 3, 22, 7]. Elimina el número máximo de la lista usando max(numeros) dentro de remove(). En este caso, elimina el 22. Imprime la lista resultante.")
    elif ejercicio == 6:
        # código del ejercicio 6
        lista = list(range(10,31,5))
        print(lista[-1] , lista[-2])
    elif ejercicio == 7:
        print("Ejercicio 7:")
        # código del ejercicio 7
        autos = ["sedan", "polo", "suran", "gol"]
        autos[1:3] = ["corsa", "clio"]
        print(autos)
    elif ejercicio == 8:
        print("Ejercicio 8:")
        # código del ejercicio 8
        dobles = []
        dobles.append(5 * 2)
        dobles.append(10 * 2)
        dobles.append(15 * 2)
        print(dobles)


    elif ejercicio == 9:
        print("Ejercicio 9:")
        # código del ejercicio 9
        compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
        compras[2].append("jugo")
        compras[1][1] = "tallarines"
        compras[0].remove("pan")
        print(compras)


    elif ejercicio == 10:
        print("Ejercicio 10:")
        # código del ejercicio 10
        lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
        print(lista_anidada)    

    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 10 o 0 para salir.")
