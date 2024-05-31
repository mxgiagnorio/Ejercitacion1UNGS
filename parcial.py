# El cine del barrio decide sistematizar la venta de entradas, cuentan con 6 salas que emiten una función
# diaria y cada sala tiene una capacidad distinta. Los compradores eligen una película y avisan cuantas
# entradas desean. Se debe hacer un programa que avise a que sala deben ingresar o si ya no hay
# disponibilidad. En caso de haber disponibilidad se deberán descontar los asientos ocupados.
# Salas= [ 1 , 2 , 3 , 4 , 5 , 6 ]
# Peliculas = [“Xmen”, “Titanic”, “Saw”, “Rio”, “Taxi Driver”, “Avatar”]
# CapacidadDisponiblePorSala= [ 80 , 70 , 60 , 75 , 40 , 90 ]


entradas = int(input("Cantidad de entradas : "))
Peliculas = ["Xmen", "Titanic", "Saw", "Rio", "Taxi Driver", "Avatar"]


def disponibilidadCine(salas, peliculas, capacidadSala, entradas):

    for i in range(len(peliculas)):
        if entradas > capacidadSala[i]:
            return "No hay disponibilidad"

        if entradas < capacidadSala[i]:

            asientosDisponibles = capacidadSala[i] - entradas

            print("Quedan", asientosDisponibles, "asientos disponibles",
                  "la funcion sera en la sala", salas[i])


# programa

entradas = int(input("cantidad de entradas vendidas para la pelicula: "))
pelicula = input("Elija que pelicula quiere ver: ")


# Ejercicio 2: (3 puntos)
# La biblioteca de la universidad asigna un código a cada libro que posee, el mismo se conforma con las
# consonantes del título que no estén repetidas y exactamente 4 dígitos con la cantidad de páginas, en
# caso de tener más de 9999 páginas se mostrarán los últimos dígitos.
# Ejemplo: Título: “eternamente” Cantidad de hojas: 918 Salida: “RM0918”
# Hacer una función que reciba el título y la cantidad de páginas de un libro y devuelva el código


def consonantes(palabra):

    vocales = "aeiou"
    nuevo = ""

    for letra in palabra:
        if letra != vocales and letra not in nuevo:
            nuevo = nuevo + letra
    return nuevo


def digitos(numero):

    numero_str = str(numero)
    longitud = len(numero_str)

    # Si la longitud es menor que 4, rellenamos con ceros
    if longitud < 4:
        ceros_necesarios = 4 - longitud
        ultimos_4_digitos = '0' * ceros_necesarios + numero_str
    else:
        # Construir manualmente los últimos 4 dígitos sin rebanado
        ultimos_4_digitos = ''
        for i in range(longitud - 4, longitud):
            ultimos_4_digitos += numero_str[i]

    return ultimos_4_digitos


def codigo(titulo, paginas):

    print("titulo: ", titulo, "cantidad de hojas: ",  paginas,
          "codigo :", consonantes(titulo), digitos(paginas))
