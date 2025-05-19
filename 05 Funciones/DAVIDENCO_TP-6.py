# PROGRAMACION 1 TRABAJO PRACTICO NUMERO 6 - FUNCIONES
# Alumno: Martín Davidenco
# DECIDI HACER UN CONDICIONAL PARA LA EJECUCIÓN DE LAS ACTIVIDADES, INGRESANDO EL NUMERO DE LA ACTIVIDAD A EJECUTAR

#LA DECLARACIÓN DE FUNCIONES SE ENCUENTRA EN EL ARCHIVO DECLARACION.py
import DECLARACION
ejercicio = int(input("Escribe el número del ejercicio a ejecutar (Del 1 al 9) "))

if ejercicio == 1:
    print(f"Ejercicio 1:")
    DECLARACION.saludo()

elif ejercicio == 2:
    print(f"Ejercicio 2:")
    nombre = input("Escribe tu nombre: ")
    DECLARACION.saludar_usuario(nombre)

elif ejercicio == 3:
    print(f"Ejercicio 3:")
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    edad = int(input("Escribe tu edad: "))
    residencia = input("Escribe tu residencia: ")
    DECLARACION.informacion_personal(nombre, apellido, edad, residencia)

elif ejercicio == 4:
    print(f"Ejercicio 4:")
    radio = float(input("Escribe el radio del círculo: "))
    DECLARACION.calcular_area_circulo(radio)
    DECLARACION.calcular_perimetro_circulo(radio)

elif ejercicio == 5:
    print(f"Ejercicio 5:")
    segundos = int(input("Escribe la cantidad de segundos: "))
    DECLARACION.segundos_a_horas(segundos)
elif ejercicio == 6:
    print(f"Ejercicio 6:")
    numero = int(input("Escribe un número entero: "))
    DECLARACION.tabla_multiplicar(numero)
    

elif ejercicio == 7:
    print(f"Ejercicio 7:")
    num1 = int(input("Escribe el primer número: "))
    num2 = int(input("Escribe el segundo número: "))
    suma, resta, multiplicacion, division = DECLARACION.operaciones_basicas(num1, num2)
    print(f"Suma: {suma}")  
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"Division: {division}")
elif ejercicio == 8:
    print(f"Ejercicio 8:")
    peso = float(input("Escribe tu peso en kg: "))
    altura = float(input("Escribe tu altura en metros: "))
    DECLARACION.calcular_imc(peso, altura)

elif ejercicio == 9:
    print(f"Ejercicio 9:")
    celsius = float(input("Escribe la temperatura en grados Celsius: "))
    DECLARACION.celsius_a_fahrenheit(celsius)

elif ejercicio == 10:
    print(f"Ejercicio 10")
    uno= int(input("Escribe el primer número: "))
    dos = int(input("Escribe el segundo número: "))
    tres = int(input("Escribe el tercer número: "))
    DECLARACION.calcular_prmedio(uno, dos, tres)

else:
    print("escribe un numero valido de ejercicio")

    
