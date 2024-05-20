# Ejercicio 1 ⋆
# Hacer un programa que guarde la siguiente lista en una variable: ["elefante", "jirafa","mono"],
# luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
# cuarto animal de la lista


animales = ["elefante", "jirafa", "mono"]

animales.append("tigre")

print(animales)


# Ejercicio 2 ⋆
# Definir una función llamada mostrarEnUnaLinea que tome una lista de enteros y muestre
# todos sus elementos en una linea separados por espacios


def mostrarEnLinea(enteros):

    for i in enteros:
        print(i, end="")


# mostrarEnLinea([1,2,3,4,5,6])


# Ejercicio 3 ⋆
# Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de
# ese entero.


def divisores(entero):

    lista = []

    for i in range(1, entero+1):
        if entero % i == 0:

            lista.append(i)

    return lista


# print(divisores(27))


# Ejercicio 4 ⋆
# Definir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos
# elementos. Si tienen igual cantidad, deberá devolver la primera.


def laMasCorta(a, b):

    if len(a) > len(b):
        return b
    else:
        return a


print(laMasCorta([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8]))


# Ejercicio 5 ⋆
# Definir una función llamada sonFactores que tome un entero n y una lista de enteros, y
# devuelva True si los números de la lista son factores de n (es decir, si n es divisible por todos
# ellos).


def sonFactores(n, enteros):

    for divisor in enteros:
        if n % divisor != 0:
            return False
    return True


# Ejercicio 6 ⋆
# Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
# y False en caso contrario.


# Hecha por mi

def elementoRepetido(lista):

    nuevaLista = []
    contador = 0

    for elemento in lista:
        if elemento not in nuevaLista:
            nuevaLista.append(elemento)
            contador = contador + 0
        else:
            contador = contador + 1

    if contador >= 1:
        return True
    else:
        return False


# Resolucion del profe

# funcion aux

def cantidadApariciones(elem, listado):
    contador = 0

    for valor in listado:
        if valor == elem:
            contador = contador + 1


def elementoRepetido(lista):

    for elem in lista:
        if cantidadApariciones(elem, lista) > 1:
            return True
    return False


# Programa

lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4, 4]

if elementoRepetido(lista2):
    print("El listado tiene elementos repetidos")
else:
    print("El listado NO tiene elementos repetidos")


# Ejercicio 7 ⋆
# Definir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
# blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
# hace, y -1 en caso contrario.


def dondeAparece(lista, blanco):

    for i in range(len(lista)):
        if lista[i] == blanco:
            return [i]

    return -1


# blanco=25
# lista = [2,8,6,7,14,15,25,64]
# print(dondeAparece(lista,blanco))


# Ejercicio 8 ⋆
# Hacer una función que tome una lista de números decimales y devuelva el promedio de los
# elementos.

def promedioDecimal(lista):
    contador = 0
    cantidad = len(lista)

    for elementos in lista:
        contador = contador + elementos

    return contador/cantidad


# Ejercicio 9 ⋆
# Escribir una función llamada maximo que tome una lista de números y devuelva el valor del
# máximo elemento.


def maximo(lista):

    actual = lista[0]

    for i in range(1, len(lista)):
        if i > actual:  # lo que estaba haciendo estaba mal porque aca estoy comparando el indice, no el valor que tiene el indice!!
            actual = i

    return actual


def maximo(lista):

    actual = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > actual:
            actual = lista[i]

    return actual


# funcion para ultimo elemento de una lista

# def maximo(lista):

#     max=[]

#     for i in range(len(lista)-1, -1,-1):

#         max.append(lista[i])

#     return max[0]


# # lista=[10,20,30,4,6,8,11,13,158]
# # print(maximo(lista))



