# TP1 - MARTÍN DAVIDENCO - COMISION 12

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Escribe tu nombre ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("Escribe tu nombre ")
apellido = input("Escribe tu apellido ")
edad = input("Escribe tu edad ")
residencia = input("Escribe tu lugar de residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = float(input("escribe el radio"))
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio
print(f"El area es {area} y el perimetro es {perimetro}")
# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("escribe una cantidad de segundos"))
horas = segundos // 3600  
print(f"esos segundos son {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
num = int(input("Escribe un numero"))
print(f"Tabla de multiplicar. x 1 = {num}, x 2 = {num * 2},  x 3 = {num * 3},  x 4 = {num * 4},  x 5 = {num * 5},  x 6 = {num * 6},  x 7 = {num * 7},  x 8 = {num * 8},  x 9 = {num * 9},   x 10 = {num * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Escribe un numero"))
num2 = int(input("Escribe otro numero"))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print (f"La suma es: {suma}, la resta es: {resta}, la multiplicación es: {multiplicacion} y la division es: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

altura = float(input("¿Altura?"))
peso = float(input("¿Peso?"))
imc = peso / (altura * altura)
print(f"Su índica de IMC es de: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Temperatura en celsius?"))
farenheit = celsius * 1.8 + 32
print(f"La temperatura en Farenheit es de {farenheit}")


# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números
num1 = float(input("Escribe un numero"))
num2 = float(input("Escribe un numero"))
num3 = float(input("Escribe un numero"))
promedio = (num1 + num2 + num3) / 3
print(f"Esto da un promedio de: {promedio}")