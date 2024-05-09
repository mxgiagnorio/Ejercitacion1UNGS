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


# Ejercicio 10
# Hacer una función potencia, que reciba dos enteros a y b y retorne a
# b
