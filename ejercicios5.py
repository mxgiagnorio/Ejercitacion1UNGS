# Ejercicio 1 ⋆
# Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
# pantalla el resultado de evaluar las siguientes fórmulas:

import math

# a) raiz  cuadrada de x
# b) |x|
# c) |x - 3|
# d) raiz cuadrada de |x - 5|

# a)

x = float(input("Escriba un numero para X: "))


def raizCuadrada(numero):
    resultado = math.sqrt(numero)
    print(resultado)


raizCuadrada(x)


# B)


x = float(input("Escriba un numero para X: "))


def absoluto(numero):
    resultado = abs(numero)
    print(resultado)


absoluto(x)


# c)

x = float(input("Escriba un numero para X: "))


def absolutos(numero):
    resultado = abs(numero - 3)
    print(resultado)


absolutos(x)


# d)

x = float(input("Escriba un numero para X: "))


def raizYModulo(numero):
    resultado = math.sqrt(abs(numero - 5))
    print(resultado)


raizYModulo(x)


# Ejercicio 2 ⋆
# Teniendo estas definiciones de funciones:
# def cuak ( ) :
# chan ( )
# print ( " pienso que " , end="" )
# chan ( )
# def chan ( ) :
# print ( "yo" , end="" )
# plin ( )
# def plin ( ) :
# print ( "." )
# Indicar qué se imprime en pantalla luego de ejecutar este programa:
# print ( "No , yo " , end="" )
# cuak ( )
# print ( "Yo " , end="" )
# chan ( )
# AYUDA: Empezar describiendo con palabras qué hacen chan y cuak cuando se las llama.
# REGLA: No vale correrlo en la computadora.


# Por consola:
# No , yo yo pienso que yoYo yo.


# Ejercicio 3 ⋆
# a) Escribir una función que reciba como parámetro una cadena y la muestre en pantalla
# 3 veces.
# b) Guardar esta definición de función en un archivo.
# c) Hacer un programa que le pida al usuario una cadena y que la muestre en pantalla
# 3 veces utilizando la función defiida anteriormente.


def unaCadena(cadena):
    print(cadena)
    print(cadena)
    print(cadena)


unaCadena("mostrala 3 veces")


texto = input("Escribi algo : ")


unaCadena(texto)


# Ejercicio 4 ⋆
# a) Escribir una función que reciba dos números reales como parámetros y retorne su
# promedio.
# b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla
# el resultado de llamar a la función del primer inciso.
# c) Idem de los dos anteriores pero con tres números. Escribir la función en el mismo
# archivo donde se escribió la del item a.


# a)

def numerosReales(a, b):
    promedio = (a+b) / 2
    return promedio


print(numerosReales(10, 8))


# b)

numero1 = float(input("Escriba un numero real: "))
numero2 = float(input("Escriba un numero real: "))

print(numerosReales(numero1, numero2))


# c)

numero1 = float(input("Escriba un numero real: "))
numero2 = float(input("Escriba un numero real: "))
numero3 = float(input("Escriba un numero real: "))


def numerosReales(a, b, c):
    promedio = (a+b+c) / 3
    return promedio


print(numerosReales(numero1, numero2, numero3))


# Ejercicio 5 ⋆
# Definir una función que devuelva el valor absoluto de un número. (Hacerlo sin utilizar la
# función abs)


def absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return -numero


print(absoluto(-20))  # Dara 20


# Ejercicio 6 ⋆
# a) Escribir una función con el siguiente encabezado: def exclamar(unaCadena): que
# retorne la misma cadena entre símbolos de exclamación (¡!)
# b) Escribir una función con el siguiente encabezado: def gritar(unaCadena): que
# retorne la misma cadena entre 3 símbolos de exclamación (¡¡¡!!!)
# c) De no haberlo hecho en el punto anterior, escribir de nuevo la función gritar utilizando solo la función exclamar.
# Nota: gritar("Ouch") deberá devolver la cadena ¡¡¡Ouch!!!
# Ayuda: Recordar que + utilizado entre cadenas las concatena.


def exclamar(unaCadena):
    return "¡" + unaCadena + "!"


exclamar("Hola")


def exclamar(unaCadena):
    return "¡" + unaCadena + "!"


def gritar(unaCadena):

    return "¡¡" + exclamar(unaCadena) + "!!"


print(gritar("Hola"))


# Ejercicio 7 ⋆
# a) Escribir una función que se llame elevarAlCubo que tome un número y retorne el
# valor de ese número al cubo.
# b) Guardar el ejercicio anterior en un archivo llamado funcionCubo.py
# c) Correr el siguiente código en un archivo nuevo y chequear que los resultados sean
# correctos:


# asi se hace para importar la funcion :
# from alCuboFuncion import elevarAlCubo   supongamos que guarde la funcion en alCuboFuncion y la funcion se llama elevarAlCubo

def elevarAlCubo(numero):
    return numero ** 3


# print(0, "al cubo:", elevarAlCubo(0))
# print(1, "al cubo:", elevarAlCubo(1))
# print(2, "al cubo:", elevarAlCubo(2))
# print(3, "al cubo:", elevarAlCubo(3))
# print(4, "al cubo:", elevarAlCubo(4))
# print(5, "al cubo:", elevarAlCubo(5))
# print(6, "al cubo:", elevarAlCubo(6))
# print(-1, "al cubo:", elevarAlCubo(-1))
# print(-2, "al cubo:", elevarAlCubo(-2))
# print(-3, "al cubo:", elevarAlCubo(-3))
# print(-4, "al cubo:", elevarAlCubo(-4))
# print(-5, "al cubo:", elevarAlCubo(-5))


# Ejercicio 8 ⋆
# a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad
# de divisores positivos de ese número.
# b) Escribir una función que tome un parámetro de tipo entero y devuelva el valor True
# si se la llama con un número primo y False en caso contrario.
# c) ¿Cuál es el número primo más grande que encontraste?
# d) Hacer una función (no pura) que reciba un entero e imprima sus factores primos.
# Por ejemplo para a = 20 la función debe mostrar 2 y 5.
# Nota: Los números primos son aquellos cuyos únicos divisores positivos son ellos
# mismos y el 1.


# a)

def contarDivisoresPositivos(entero):
    count = 0

    for i in range(1, entero + 1):

        if entero % i == 0:
            if i > 0:
                count += 1

    return count


print(contarDivisoresPositivos(12))


def enteroPrimo(entero):

    if contarDivisoresPositivos(entero) == 2:
        return True
    else:
        return False


# Ejercicio 9
# a) Hacer una función que reciba dos enteros y retorne el mayor.
# b) Hacer una función que reciba tres enteros y retorne el mayor.


# a)
def mayor(a, b):

    if a > b:
        return a
    else:
        return b

# b)


def elMayor(a, b, c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# Ejercicio 10
# Hacer una función potencia, que reciba dos enteros a y b y retorne a ** b


def potencia(a, b):
    return a**b


# Ejercicio 11
# a) Hacer una función que sume los divisores propios de un número.
# b) Hacer una función que indique si un número es perfecto. Número perfecto: a es
# perfecto si la suma de sus divisores propios es igual a a.
# c) Hacer una función que determine si un número ingresado por el usuario es un número
# abundante. Número abundante: todo número natural que cumple que la suma de sus
# divisores propios es mayor que el propio número. Por ejemplo, 12 es abundante ya
# que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor
# al propio 12


# a)

def sumaDivisores(n):

    suma = 0

    for i in range(1, n+1):
        if n % i == 0:
            suma = suma + i

    return suma


# b)


# def sumaDivisoresPropios(n):
#     suma = 0
#     for i in range(1, n):
#         if n % i == 0:
#             suma = suma + i

#     if suma == n:
#         return "Es perfecto"
#     else:
#         return "No es perfecto"

def sumaDivisoresPropios(n):
    if sumaDivisores(n) == 0:
        return "es perfecto"
    else:
        return "No es perfecto"


# c)


n = int(input("escriba un numero :"))


def abundante(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma = suma + i

    if suma > n:
        return "Es abundante"
    else:
        return "No es abundante"


print(abundante(n))


# Ejercicio 12
# Hacer una función que indique si un número es Poderoso: Número poderoso: es un número
# natural n que cumple que todos sus divisores primos al cuadrado también son divisores, es decir,
# si p es un divisor primo entonces p**2 también lo es. Por ejemplo, el número 36 es un número
# poderoso ya que los únicos primos que son divisores suyos son 2 y 3 y se cumple que 4 y 9
# también son divisores de 36.


def primo(n):
    bandera = True
    # arranca del 2 porque el 1 es divisor de todos, lo divide asi no hace el ciclo al pedo.
    for i in range(2, n // 2 + 1):
        if n % i == 0:  # Si tiene algun divisor que no sea 1 y el mismo es porque no es primo
            bandera = False
    return bandera


a = int(input("Ingrese un número: "))
poderoso = True

for i in range(1, a + 1):  # recorre el numero que pidio el user
    # verifica si a es divisible por I y si I es primo de a
    if a % i == 0 and primo(i):
        # Si es primo pero la division de ese numero por I al cuadrado no es 0 entonces no es poderoso porque el resultado no es divisor del numero que se eligio.
        if a % (i * i) != 0:
            poderoso = False

if poderoso == True:
    print(a, "es poderoso")
else:
    print(a, "NO es poderoso")


# Ejercicio 13
# Hacer una función que indique si un número es Libre de Cuadrados: Número libre de cuadrados:
# todo número natural que cumple que en su descomposición en factores primos no aparece ningún
# factor repetido. Por ejemplo, el número 30 es un número libre de cuadrados

def primo(n):
    bandera = True
    for i in range(2, n//2+1):
        if (n % i == 0):
            bandera = False
    return bandera


a = int(input("Ingrese un numero"))
producto = 1
for i in range(1, a+1):
    if (a % i == 0 and primo(i)):
        producto = producto*i

if (producto == a):
    print(a, "SI es libre de cuadrados")
else:
    print(a, "NO es libre de cuadrados")


# Ejercicio 14
# Hacer un programa que solicite al usuario un número entero positivo e indique cuál es el
# número primo mayor más cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
# programa devolverá 29 (29 es el número primo más cercano mayor que 24). Si el usuario ingresa
# 5 el programa devolverá 7


n = int(input("Ingrese un numero"))


def primo(n):
    bandera = True
    for i in range(n, n+100):
        if (n % i == 0):
            bandera = False
    return bandera


# Ejercicio 15
# Hacer una función (no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
# Por ejemplo si la cadena fuera sobrevivir, la función debería imprimir
# **************
# * sobrevivir *
# **************


def imprimir_con_marco(palabra):
    """Función que imprime la palabra rodeada de asteriscos."""
    longitud = len(palabra) + 4
    asteriscos = "*" * longitud

    print(asteriscos)
    print('* ' + palabra + ' *')
    print(asteriscos)


# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Llamar a la función para imprimir la palabra con marco de asteriscos
imprimir_con_marco(palabra)


# Ejercicio 17 ⋆
# Escribir una función (y probarla en un programa) para cada una de las siguientes descripciones:
# a) una función que se llame tieneRepetidas que tome una cadena como parámetro y
# devuelva True si esa cadena tiene alguna letra que aparece más de una vez y False
# en caso contrario.
# b) una función que se llame aparece que tome dos parámetros, una letra y una cadena,
# y devuelva True si la letra aparece en la cadena y False en caso contrario.
# c) una función que se llame dameRepetida que tome una cadena como parámetro y
# retorne la primer letra que aparece repetida en la cadena
# d) una función que se llame quitarRepeticiones que tome dos parámetros, una
# cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las
# repeticiones de esa letra. Por ejemplo, un programa que llame a la función
# así: quitarRepeticiones("mate cocido", "c"), deberá retornar la cadena "mate
# coido".


# a)


def contar(letra, cadena):

    contador = 0

    for caracter in cadena:
        if letra == caracter:
            contador = contador + 1

    return contador


def tieneRepetidas(cadena):

    for caracter in cadena:
        if contar(caracter, cadena) > 1:
            return True

    return False


# programa

a = "Hoytengounmaldia"
b = "holi"

if tieneRepetidas(a):
    print(a, "tiene repetidas")
else:
    print(a, "No tiene repetidas")


# b)

def aparece(letra, cadena):

    for caracter in cadena:
        if letra == caracter:
            return True

    return False


# c)


def dameRepetida(cadena):
    # Iterar sobre cada letra en la cadena
    for i in range(len(cadena)):
        # Comparar la letra actual con las letras siguientes en la cadena
        for j in range(i + 1, len(cadena)):
            if cadena[i] == cadena[j]:
                return cadena[i]

    # Si no se encuentra ninguna letra repetida, devolver None
    return "no hay repetidas"


# Ejemplo de uso:
cadena = "jom"
print(dameRepetida(cadena))


# d)


def quitarRepeticiones(cadena, letra):
    nuevaCadena = ""

    for caracter in cadena:
        if caracter == letra:
            if contar(letra, nuevaCadena) == 0:
                nuevaCadena = nuevaCadena + letra
            else:
                nuevaCadena = nuevaCadena + letra
    return nuevaCadena


