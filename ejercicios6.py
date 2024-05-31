# funcion para ultimo elemento de una lista

# def maximo(lista):

#     max=[]

#     for i in range(len(lista)-1, -1,-1):

#         max.append(lista[i])

#     return max[0]

# # lista=[10,20,30,4,6,8,11,13,158]
# # print(maximo(lista))
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


# Ejercicio 10 ⋆
# Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
# índice del máximo elemento.


def maximoIndice(lista):

    indice = maximo(lista)

    for i in range(len(lista)):
        if lista[i] == indice:
            return i

    return indice


# Sin usar la funcion maximo:


def maximoIndice(lista):

    valorMaxIndice = 0
    indice = lista[0]

    for i in range(1, len(lista)):

        if lista[i] > indice:
            indice = lista[i]
            valorMaxIndice = i

    return valorMaxIndice


# Ejercicio 11 ⋆
# Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
# menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
# los que están entre el índice a y el índice b


# aux

def listaAcotada(lista, a, b):

    nuevaLista = []

    for i in range(len(lista)):
        if i > a and i < b:
            nuevaLista.append(lista[i])
        elif i < a and i > b:
            nuevaLista.append(lista[i])

    return nuevaLista


def maximoEntre(lista, a, b):
    lista = listaAcotada(lista, a, b)
    indice = maximo(lista)
    valorMaxIndice = maximoIndice(lista)

    for i in range(len(lista)):
        if lista[i] > indice:
            indice = lista[i]
            valorMaxIndice = i

    return valorMaxIndice


# Ejercicio 12 ⋆
# Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
# positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
# elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modificar la que
# toma como parámetro.


def intercambiar(s, a, b):

    aux = s[a]
    s[a] = s[b]
    s[b] = aux


# Ejercicio 13 ⋆
# Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como
# parametros y devuelva la cantidad de veces que aparece n en s.


def frecuencia(s, n):

    contador = 0

    for enteros in s:
        if enteros == n:
            contador = contador + 1

    return contador


# Ejercicio 14 ⋆
# Definir una función llamada interseccion que tome dos listas sin repetidos y devuelva una
# nueva lista que contenga sólamente aquellos elementos que estén ambas listas.


def insterseccion(lista1, lista2):

    unificada = lista1 + lista2
    nuevaLista = []

    for apariciones in unificada:
        if apariciones not in nuevaLista and apariciones in lista1 and apariciones in lista2:
            nuevaLista.append(apariciones)

    return nuevaLista


# Ejercicio 15 ⋆
# Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista
# que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos


def union(lista1, lista2):

    unificada = lista1 + lista2
    nuevaLista = []

    for apariciones in unificada:
        if apariciones not in nuevaLista:
            nuevaLista.append(apariciones)

    return nuevaLista


# Ejercicio 16 ⋆
# Definir una función llamada diferencia que tome dos listas sin repetidos y devuelva una
# nueva lista que contenga los elementos la primera que no estén en la segunda.


def diferencia(lista1, lista2):

    nuevaLista = []
    unificada = lista1 + lista2

    for apariciones in unificada:
        if apariciones not in nuevaLista and apariciones in lista1 and apariciones not in lista2:
            nuevaLista.append(apariciones)
    return nuevaLista


# Ejercicio 17 ⋆
# Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común
# divisor usando funciones de los ejercicios anteriores


def esta(entero, lista):
    for i in lista:
        if (i == entero):
            return (True)
    return (False)


def interseccion(lista1, lista2):
    lista3 = []
    for i in lista1:
        if (esta(i, lista2)):
            lista3.append(i)
    return (lista3)


def divisores(a):
    lista = []
    for i in range(1, a+1):
        if (a % i == 0):
            lista.append(i)
    return lista


def maximo(lista):
    max = lista[0]
    for elem in lista:
        if max < elem:
            max = elem
    return max


def MCD(a, b):
    divA = divisores(a)
    divB = divisores(b)
    divComunes = interseccion(divA, divB)
    MCD = maximo(divComunes)
    return (MCD)


a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

print("El MCD entre ", a, " y ", b, " es: ", MCD(a, b))


# Ejercicio 18 ⋆
# Definir una función que tome un entero n y devuelva los primeros n primos.


def verificacionPrimo(n):

    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def primos(n):

    numeroPrimo = 2
    listaPrimos = []

    while len(listaPrimos) < n:
        if verificacionPrimo(numeroPrimo):
            listaPrimos.append(numeroPrimo)
        numeroPrimo = numeroPrimo + 1
    return listaPrimos


# Ejercicio 19 ⋆
# Definir una función que tome un entero n y devuelva la lista de los primos que aparecen al
# factorear n. Ejemplo, para 24, la lista debe ser: [2, 2, 2, 3]


def factoreoPrimos(n):

    lista = []
    num = 2

    while num <= n:
        if n % num == 0:
            n = n/num
            lista.append(num)
        else:
            num = num + 1
    return lista


# Ejercicio 20 ⋆
# a) Definir una función que tome una lista de números s y un número decimal x y
# devuelva la cantidad de elementos de s que sean menores que x.
# b) Si se pone como condición que s siempre esté ordenada de mayor a menor, cómo
# podría modificarse el programa para que haga menos iteraciones?

# a)


def decimalX(lista, x):
    contador = 0

    for numeros in lista:
        if numeros < x:
            contador = contador + 1

    return contador

# b)


def decimalX(lista, x):
    contador = 0

    for numero in lista:
        if numero < x:
            contador += 1
        else:
            break  # Salir del bucle ya que el resto de los elementos serán mayores o iguales

    return contador


# Ejercicio 21 ⋆
# Definir una función que tome una lista de números s y un número decimal x y cambie todos
# los elementos menores que x por 0.
# Ej:
# Para
# s = [1, 4.1, 6.3, 2, 3.2, 8]
# x = 3
# el la lista debe pasar a ser:
# s = [0, 4.1, 6.3, 0, 3.2, 8]


def cambiarDecimal(s, x):

    for i in range(len(s)):
        if s[i] < x:
            s[i] = 0

    print(s)


# Ejercicio 22 ⋆
# Escribir un programa que pida al usuario una cadena, y luego escriba en pantalla la cantidad
# de veces que aparece cada letra (sin mostrar las que no aparecen). Ej:
# Palabra ingresada: "conocido"
# c : 2
# o : 3
# n : 1
# i : 1
# d : 1


cadena = input("Escriba una palabra: ")


def aparece(caracter, lista):
    for elem in lista:
        if elem == caracter:
            return True
    return False


def cantidadAparece(caracter, lista):
    contador = 0

    for elem in lista:
        if elem == caracter:
            contador += 1
    return contador


def principal(cadena):

    letras = []
    cantidades = []

    for caracter in cadena:
        if not aparece(caracter, letras):
            letras.append(caracter)
            cantidades.append(cantidadAparece(caracter, cadena))

    for i in range(len(letras)):
        print(letras[i], ":", cantidades[i])
