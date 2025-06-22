# programacion 1 trabajo practico numero 8 - datos complejos
# alumno: martín davidenco

# decidi hacer un condicional para la ejecución de las actividades, ingresando el numero de la actividad a ejecutar
ejercicio = int(input("escribí el numero del ejercicio a ejecutar (del 1 al 10) "))

if ejercicio == 1:
    print(f"ejercicio 1:")
    precios_frutas = {'banana': 1200, 'ananá': 2500, 'melón': 3000, 'uva': 1450}
    precios_frutas['naranja'] = 1200
    precios_frutas['manzana'] = 1500
    precios_frutas['pera'] = 2300
    print(precios_frutas)

elif ejercicio == 2:
    print(f"ejercicio 2:")
    precios_frutas = {'banana': 1200, 'ananá': 2500, 'melón': 3000, 'uva': 1450,
                      'naranja': 1200, 'manzana': 1500, 'pera': 2300}
    precios_frutas['banana'] = 1330
    precios_frutas['manzana'] = 1700
    precios_frutas['melón'] = 2800
    print(precios_frutas)

elif ejercicio == 3:
    print(f"ejercicio 3:")
    precios_frutas = {'banana': 1330, 'ananá': 2500, 'melón': 2800, 'uva': 1450,
                      'naranja': 1200, 'manzana': 1700, 'pera': 2300}
    frutas = list(precios_frutas.keys())
    print(frutas)

elif ejercicio == 4:
    print(f"ejercicio 4:")
    contactos = {}
    for i in range(5):
        nom = input("nombre del contacto: ")
        num = input("numero de telefono: ")
        contactos[nom] = num
    buscar = input("de quien queres el numero? ")
    if buscar in contactos:
        print("numero:", contactos[buscar])
    else:
        print("no esta ese contacto")

elif ejercicio == 5:
    print(f"ejercicio 5:")
    frase = input("escribi una frase: ")
    palabras = frase.split()
    unicas = set(palabras)
    print("palabras unicas:", unicas)
    repes = {}
    for p in palabras:
        if p in repes:
            repes[p] += 1
        else:
            repes[p] = 1
    print("cantidad por palabra:", repes)

elif ejercicio == 6:
    print(f"ejercicio 6:")
    alumnos = {}
    for i in range(3):
        nom = input("nombre del alumno: ")
        notas = []
        for j in range(3):
            nota = float(input(f"nota {j+1} de {nom}: "))
            notas.append(nota)
        alumnos[nom] = tuple(notas)
    for nom in alumnos:
        prom = sum(alumnos[nom]) / 3
        print(f"promedio de {nom}: {prom:.2f}")

elif ejercicio == 7:
    print(f"ejercicio 7:")
    parc1 = {1, 2, 3, 4}
    parc2 = {3, 4, 5, 6}
    print("aprobaron los dos:", parc1 & parc2)
    print("solo uno de los dos:", parc1 ^ parc2)
    print("al menos uno:", parc1 | parc2)

elif ejercicio == 8:
    print(f"ejercicio 8:")
    stock = {}
    prod = input("producto a consultar: ")
    if prod in stock:
        print("hay:", stock[prod])
        cant = int(input("cuantas unidades agregas? "))
        stock[prod] += cant
    else:
        nuevo = int(input("cuantas unidades tiene el producto nuevo? "))
        stock[prod] = nuevo
    print(stock)

elif ejercicio == 9:
    print(f"ejercicio 9:")
    agenda = {}
    seguir = "s"
    while seguir == "s":
        dia = input("dia: ")
        hora = input("hora: ")
        cosa = input("que hay en ese momento? ")
        agenda[(dia, hora)] = cosa
        seguir = input("queres meter otra? (s/n): ")
    dia = input("consulta - dia: ")
    hora = input("consulta - hora: ")
    clave = (dia, hora)
    if clave in agenda:
        print("hay:", agenda[clave])
    else:
        print("no hay nada anotado")

elif ejercicio == 10:
    print(f"ejercicio 10")
    paises = {"argentina": "buenos aires", "brasil": "brasilia", "uruguay": "montevideo"}
    invertido = {}
    for pais, cap in paises.items():
        invertido[cap] = pais
    print(invertido)

else:
    print("escribi un numero valido de ejercicio")
