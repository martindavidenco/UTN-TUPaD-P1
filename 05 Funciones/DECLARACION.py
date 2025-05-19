#1
def saludo():
    print("Hola mundo")

#2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    print(f"El área del círculo es: {area}")
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print(f"El perímetro del círculo es: {perimetro}")

#5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
#6  
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#7  
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division) 
#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc}")
#9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
#10
def calcular_prmedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio es: {promedio}")