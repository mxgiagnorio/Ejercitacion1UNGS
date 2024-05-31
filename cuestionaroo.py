def legajoEstudiantes(apellidos, numDirecciones):
    legajos = []

    for i in range(len(apellidos)):
        apellido = apellidos[i]
        direccion = numDirecciones[i]

        primeraLetra = apellido[0].upper()
        cantidadDigitos = len(str(direccion))

        legajo = primeraLetra + str(cantidadDigitos)
        legajos.append(legajo)

    return legajos


# Programa principal
apellidos = ["perez", "lopez", "pinto", "antunez", "espindola"]
numDirecciones = [32, 236, 3125, 3861, 25]

resultado = legajoEstudiantes(apellidos, numDirecciones)
print(resultado)
