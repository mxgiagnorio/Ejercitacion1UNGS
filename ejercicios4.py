# Ejercicio 1 ⋆
# a) Escribir un programa que pida al usuario un número n y muestre una línea de n
# asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
# ********
# b) Escribir un programa que pida al usuario un número n y muestre n líneas de
# 1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
# mostrar:
# *
# **
# ***
# ****
# *****
# c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
# asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
# *
# ***
# *****
# *******
# *********


# A

n = int(input("Escriba un numero: "))

for i in range(0, n):
    i = "*"
    print(i, end="")


# B
ast = ""
n = int(input("Escriba un numero: "))
for i in range(0, n):
    ast = ast + "*"

    print(ast)


# C

ast = ""
n = int(input("Escriba un numero: "))

for i in range(1, n+1):

    condicion = 2*i-1

    ast = condicion * "*"
    print(ast)


# Ejercicio 2 ⋆
# a) Sabiendo que la pantalla de la consola tiene 80 caracteres de ancho, hacer un programa que, dada una palabra, la escriba en el centro de la pantalla.
# b) Hacer una programa que, dada una palabra, la escriba pegada a la derecha de la pantalla.

# A


palabra = (input("Escriba una palabra: "))

ancho = 80
longPalabra = len(palabra)
espaciosPalabra = (ancho - longPalabra)//2
espacioTotal = " " * espaciosPalabra + palabra
print(espacioTotal)


# B

palabra = input("Escriba una palabra : ")

ancho = 80
largoPalabra = len(palabra)

espaciosPalabra = ancho - largoPalabra

espacioTotal = " " * espaciosPalabra + palabra

print(espacioTotal)


# Ejercicio 3 ⋆
# Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejemplo,
# si la palabra es "Ganaste", el programa debería escribir:
# ***********
# * Ganaste *
# **********


palabra = input("Escriba una palabra: ")

longitud = len(palabra) + 4

asteriscos = "*" * longitud
print(asteriscos)
print('* ' + palabra + ' *')
print(asteriscos)

# Ejercicio 4
# Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de esa letra.


apariciones = 0

palabra = input("Escriba una palabra: ")
letra = input("Escriba una letra: ")

for cadena in palabra:
    if cadena == letra:
        apariciones = apariciones + 1
print(apariciones)


# Ejercicio 5
# Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos vocales unidas)


palabra = input("Escriba una palabra: ")
vocales = "aeiou"
cont = 0
# tieneDiptongo= False

for cadena in palabra:
    if cadena in vocales:
        cont = cont + 1
    else:
        cont = 0
if cont >= 2:
    # tieneDiptongo = True
    print("la palabra", palabra, "tiene diptongo")
else:
    print("la palabra", palabra, "no tiene diptongo")

# No es necesario el booleano pero ayuda a clarificar el codigo y hacer mas explicito cuando el bucle finaliza.


# Ejercicio 6
# Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
# de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
# "programador"
# "r"
# el programa debe devolver "p ∗ og ∗ amado∗"


palabra = input("Escriba una palabra: ")
letra = input("Escriba una letra: ")
modificada = ""

for cadena in palabra:
    if cadena in letra:

        modificada = modificada + "*"
    else:
        modificada = modificada + cadena

print(modificada)


# Ejercicio 7
# Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
# empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
# primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
# faltantes las reemplazará por "*". Ejemplos:
# clemente CLMN
# rivera RVR*
# oreo R***
# La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
# Ejemplos: CLMN1 RVR*4 R***7


# import random

apellido = input("Ingrese su apellido: ")
vocales = "aeiou"
clave = ""
consonantes = 0

# Obtener las primeras 4 consonantes del apellido o completar con '*'
for letra in apellido:
    if consonantes < 4 and letra not in vocales:
        clave = clave + letra  # Agregar la consonante a la clave
        consonantes = consonantes + 1
        # cuando llega a 4 la condicion se vuelve False y ya no agregara mas consonantes


# Completar con '*' si hay menos de 4 consonantes
if len(clave) < 4:
    clave = clave + '*' * (4 - len(clave))

# Generar un dígito aleatorio entre 0 y 9
digAleatorio = random.randint(0, 9)

# Construir la clave provisional combinando las consonantes y el dígito aleatorio
clave = clave + str(digAleatorio)

# Mostrar la clave provisional generada
print("La clave provisional generada es:", clave)


# Ejercicio 8
# Hacer un programa que solicite el dni, el nombre y apellido y arme el legajo de estudiantes de
# la universidad de la siguiente manera:
# Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
# primeras letras del apellido y por ultimo la primera y ultima del nombre.
# Por ejemplo:
# JavierRodriguez 38946702
# Legajo: 389_rodjr

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
dni = input("Escriba su dni: ")
legajo = ""
cont = 1

for numero in dni:
    if cont <= 3:
        legajo = legajo + numero
    cont = cont + 1

legajo = legajo + "_"

cont = 1
for letra in apellido:
    if cont <= 3:
        legajo = legajo + letra
    cont = cont + 1

cont = 1
for caracter in nombre:
    if cont == 1 or cont == len(nombre):
        legajo = legajo + caracter
    cont = cont + 1

print("El legajo de ", nombre, apellido, " es: ", legajo)


n = int(input("escriba la cantidad de terminos: "))
suma = 0

for i in range (0,n+1):
    i = 1/(2**i)
    suma = suma + i
print (suma)

#1/(2**1) + 1/(2**2) + 1/(2**3) + 1/(2**4) + 1/(2**5) + 1/(2**6) + 1/(2**7) 