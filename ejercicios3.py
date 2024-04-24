# Ejercicio 1 ⋆
# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
# (1, 2, 3, 4 y 5).

# while


import random
import math
n = 6

while n > 0:
    print(n)
    n = n-1
print("Termina ciclo")

# for

for i in range(1, 5, 1):
    print(i)

# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).

# while

n = int(input("Escribe un numero natural del 1 al 9"))

while n < 10:
    print(n)
    n = n+1
print("Fin del ciclo")

# for

n = int(input("Escribe un numero natural"))

for n in range(0, n, 1):
    print(n)


# Ejercicio 2 ⋆
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
# 7 (4, 5, 6 y 7).

for i in range(3, 8, 1):
    print(i)

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
# si n es menor que m?

    # while  tiene detalles

n = int(input("Escribe un numero natural"))
m = int(input("Escribe un numero natural"))

if n > m:

    while n > m:

        n = n-1
        m = m+1

        print(m, n)
else:

    m = int(input("Escribe otro numero natural"))

print("fin de ciclo")


# for

n = int(input("Escribe una cota inferior"))
m = int(input("Escribe una cota superior"))


for i in range(n, m+1):  # el m+1 hace que lo incluya.

    print(i)


# Ejercicio 3 ⋆
# a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
# siguen al 10 (11, 12, · · · , 15).


for i in range(11, 16):

    print(i)


# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).


num = int(input("Escribe un numero natural"))

for i in range(num+1, num+6):

    print(i)


# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).


n = int(input("Escribe un numero para N"))
c = int(input("Escribe un numero para C"))


for i in range(n, n+c):

    print(i)


# Ejercicio 4 ⋆
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
# 11 salteando de a 2 elementos (5, 7, 9 y 11)

for i in range(5, 11+1, 2):

    print(i)


# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
# usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
# 2, 5, 8, 11, 14.

m = int(input("Escribe un numero para M"))
n = int(input("Escribe un numero para N"))


for i in range(m, n+1, 3):

    print(i-3)


# c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
# luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
# ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14.

m = int(input("Escribe un numero para M"))
n = int(input("Escribe un numero para N"))
p = int(input("Escribe un numero para P"))


for i in range(m, n+1, p):

    print(i)


# Ejercicio 5 ⋆


# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el
# 3 (8, 7, 6, 5, 4, 3).

for i in range(8, 3-1, -1):

    print(i)


# Ejercicio 6 ⋆
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta
# el 6 pero salteando de a tres (15, 12, 9, 6).


for i in range(15, 6-1, -3):

    print(i)


# Contabilidad Express S.A. es un estudio contable que ofrece servicios de consultoría en materia económica a empresas, principalmente PyMes. Durante la pandemia la mayor parte de sus actividades
#  fueron automatizadas aunque, para un número reducido de tareas de facturación -que no pudieron incluirse en este proceso de simplificación-, se requiere que personal
#  del estudio realice cálculos manuales utilizando una planilla de Excel.


# Uno de los socios fundadores contactó a un grupo de estudiantes de la UNGS para que se encarguen de elaborar una propuesta, en función de los requerimientos de la empresa.
# De las sucesivas reuniones se extrajo la siguiente información:

# 🟢 Se debe permitir el ingreso de n facturas (siendo n una cantidad finita, estipulada por el usuario). Ej. si n = 5, permitirá ingresar 5 facturas.

# 🟢 Cada factura está compuesta 3 datos que debe ingresar el usuario. La razón social del cliente (ej. 'Elevadores Azcuénaga'), su CUIT/CUIL y el monto a abonar.


# Se pide, entonces, desarrollar un algoritmo que, en función de las facturas ingresadas, emita por consola:

# Los datos de cada factura, al finalizar su ingreso y ANTES de ingresar la siguiente.
# La cantidad total de dinero recaudado de todas las facturas.
# El importe que deberá adicionar en concepto de IVA (18%), por el total acumulado (punto anterior) de las facturas.
# Si el monto total acumulado es inferior a $25.000.


# ⚠️ Aclaraciones:

# ✏️ La cantidad de facturas DEBE ser ingresada por el usuario.

# ✏️ Los mensajes a imprimir DEBEN ser descriptivos. Imprimir 1 (un) mensaje por cada ítem del problema.

# 👁‍🗨 Diseñar una solución que permita que, en caso de que el porcentaje de IVA o el monto del último ítem ($25.000) cambien, su actualización sea relativamente
# (editando, en lo posible, 2 líneas de código como máximo).

facturaActual = 0

iva = 0.18

totalAbonar = 0

montoAcumulado = 25000

cantFacturas = int(input("Ingrese el numero de facturas: "))

while cantFacturas > facturaActual:

    razonSocial = input("escribir razon social: ")

    cuitCuil = int(input("escribir cuit/cuil de la empresa: "))

    montoAbonar = float(input("Monto a abonar: "))

    print("La empresa ", razonSocial, " cuyo cuit/cuil es: ",
          cuitCuil, "debera pagar un monto de ", montoAbonar)

    totalAbonar = montoAbonar + totalAbonar

    print("Hasta el momento se tiene que abonar un total de : $", totalAbonar)

    facturaActual = facturaActual + 1

print("El monto total de las facturas es :", totalAbonar)

if (totalAbonar < montoAcumulado):
    totalAbonar = totalAbonar*iva + totalAbonar
    print("al ser el importe menor a $25000 habra que abonar sumando el iva $:", totalAbonar)


# Ejercicio 8 ⋆
# Es verdad que las únicas soluciones de x
# (x+2)(x+3) = 1 son x = 1 x = −2 y x = −3?.
# Hacer un programa que encuentre todas las soluciones de 1 0 2 cifras tanto negativas como positivas


for x in range(-99, 100, 1):  # Este ejercicio no esta bien resuelto

    x**((x+2)*(x+3)) == 1
    print(x)


# Ejercicio 9
# a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
# menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
# 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
# b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
# 16 32.
# c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
# 256. Es decir 1**2, 2**3, 3**4, 4**5


# a


n = int(input("escriba un numero : "))

contador = 0

pot = 2**contador

while pot < n:

    print(pot)
    contador = contador+1
    pot = 2**contador


# b

n = int(input("escriba un numero mayor a 0 : "))
x = 2

for i in range(1, n+1):

    i = x**i

    print(i, end=" ")

# 2**1 2**2 2**3 2**4 2**5 2**6


# c

n = int(input("escriba un numero mayor a 0 : "))
x = n

for i in range(1, n+1):

    i = x**i

    print(i, end=" ")


# Ejercicio 10
# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores de n.
# b) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores pares de n.
# c) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla la cantidad de divisores de n.
# d) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla la suma de los divisores de n.
# e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los primeros c divisores de n.
# f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los últimos c divisores de n.


# A

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):

    if n % i == 0:
        print(i, end=" ")

# B

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):

    if n % i == 0 and i % 2 == 0:
        print(i, end=" ")


# C


contador = 0

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):

    if n % i == 0:

        contador = contador + 1

print("Los divisores del numero", n, "son:", contador)


# D

contador = 0

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):

    if n % i == 0:

        contador = contador + i


print("La suma de los divisores de ", n, " es :", contador)


# E


n = int(input("Ingrese un número positivo n: "))
c = int(input("Ingrese un número positivo c: "))


contadorDivisores = 0


print("Los primeros", c, "divisores de", n, "son: ")
divisor = 1


while contadorDivisores < c:
    if n % divisor == 0:

        print(divisor)
        contadorDivisores += 1
    divisor += 1


# F


n = int(input("escriba un numero mayor a 0 : "))
c = int(input("escriba un numero mayor a 0 : "))


contadorDivisores = 0

divisor = n

print("Los ultimos", c, "divisores de", n, "son : ")

while contadorDivisores < c:

    if n % divisor == 0:
        print(divisor, end=" ")

        contadorDivisores = contadorDivisores + 1
    divisor = divisor - 1


# Ejercicio 11
# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
# pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n.


n = int(input("escriba un numero mayor a 0 : "))


for i in range(1, n+1):

    producto = i*n
    print("El producto entre", i, "y", n, "son: ", producto)


# Ejercicio 12
# Hacer un programa que reciba un número m y determine el primer n para el cual la suma
# 1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
# 10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11


m = int(input("escriba un numero mayor a 0 : "))
n = 0
acc = 1
while n < m:
    n = n + acc
    if n > m:
        print("El numero por el cual la suma sera mayor a", m, "es: ", acc)
    else:
        acc = acc + 1


# Ejercicio 13
# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4, 6..
# b) Idem anterior para la sucesión an = 2n − 1.
# c) Idem anterior para la sucesión an = n**2
# d) Idem anterior para la sucesión an = n**3 - n**2
# e) Idem anterior para la sucesión an = 1/n**2


# A

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):
    print(i*2, end=" ")


# B

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):
    print(i*2-1, end=" ")


# C

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):
    print(i**2, end=" ")


# D

n = int(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):
    print(i**3 - i**2, end=" ")


# E

n = float(input("escriba un numero mayor a 0 : "))

for i in range(1, n+1):
    print(1/i**2, end=" ")


# Ejercicio 14
# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
# 2 6 12 20...
# b) Idem anterior para la sucesión an = n**2
# c) Idem anterior para la sucesión an = n**3 - n**2
# d) Idem anterior para la sucesión an = 1/n**2
# e) A qué valor se va acercando la suma del inciso anterior a medida que utilizamos un valor alto de n?


# A

n = int(input("escriba un numero mayor a 0 : "))

suma = 0

for i in range(1, n+1):
    i = i*2
    suma = suma + i
    print(suma, end=" ")


# B

n = int(input("escriba un numero mayor a 0 : "))

suma = 0

for i in range(1, n+1):
    i = i**2
    suma = suma + i
    print(suma, end=" ")


# C

n = int(input("escriba un numero mayor a 0 : "))

suma = 0

for i in range(1, n+1):
    i = i**3 - i**2
    suma = suma + i
    print(suma, end=" ")


# D

n = int(input("escriba un numero mayor a 0 : "))

suma = 0

for i in range(1, n+1):
    i = 1/i**2
    suma = suma + i
    print(suma, end=" ")

# E
# Este resultado es un resultado famoso en matemáticas y se conoce como la fórmula de Basilea o la fórmula de Euler


# Ejercicio 15

# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:

# ln(2) = 1 - 1/2 + 1/3 - 1/4 + 1/5 ....

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y que muestre la aproximación de ln(2) con esa cantidad de términos.
# b) A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que da la calculadora? En python se puede aproximar este valor usando math.log(2)
# c) A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor queda la calculadora?
# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,pida al usuario un número decimal ϵ (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor qe ϵ


# A


n = int(input("escriba la cantidad de terminos a sumar : "))

suma = 0

for i in range(1, n+1):

    if i % 2 == 0:
        termino = -1/i
    else:
        termino = 1/i
    suma = suma + termino

print(suma)


# B

# import math

n = int(input("escriba la cantidad de terminos a sumar : "))

suma = 0

for i in range(1, n+1):

    if i % 2 == 0:
        termino = -1/i
    else:
        termino = 1/i
    suma = suma + termino

print(suma)
# en python log se hace en base a e (log natural) y no en base 10 como en otro contexto
print(math.log(2))


# D

# import math

log2 = math.log(2)
print(log2)

suma = 0

i = 1

while (abs(log2-suma) >= 0.0001):

    termino = i/1
    if i % 2 == 0:
        suma = suma - termino
    else:
        suma = suma + termino
    i = i + 1
print(i, suma)


# Solicitar al usuario un número natural n
n = int(input("Ingrese un número natural: "))

# Variable para almacenar la suma de divisores pares de n
sumDivParesN = 0

# Calcular la suma de divisores pares de n
for i in range(1, n + 1):
    if i % 2 == 0 and n % i == 0:
        sumDivParesN = sumDivParesN + i

# Variable para almacenar la mayor suma de divisores pares de números menores que n
maxSumDivParesMenores = 0

# Calcular la mayor suma de divisores pares de números menores que n
for m in range(1, n):
    sumDivParesM = 0
    for j in range(1, m + 1):
        if j % 2 == 0 and m % j == 0:
            sumDivParesM = sumDivParesM + j
    if sumDivParesM > maxSumDivParesMenores:
        maxSumDivParesMenores = sumDivParesM

# Verificar si n es cuasi cuantioso
if sumDivParesN > maxSumDivParesMenores:
    print(n, "es cuasi cuantioso.")
else:
    print(n, " NO es cuasi cuantioso.")


# ejercicio 16

# El número 1/4π se puede aproximar de la siguiente manera:

# 1/4π = 1 - 1/3 + 1/5 - 1/7 + 1-9 - 1/11 + 1/13 - 1/15

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de π con esa cantidad de términos.
# b) A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora?
# c) A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ϵ (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor q ϵ


# A

print("Calcularemos PI")
n = int(input("Ingrese la cantidad de términos: "))

suma = 0  # Inicializamos la variable para almacenar la suma de términos
signo = 1  # Variable para alternar el signo de cada término en la serie

# Iteramos sobre los primeros n términos de la serie (1, 3, 5, ..., hasta el n-ésimo término impar)
# Empezamos desde 1 hasta n (de 2 en 2, para incluir solo los términos impares)
for i in range(1, n + 1, 2):
    suma = suma + 1 / i * signo  # Sumamos el término actual con el signo correspondiente
    signo = -signo  # Cambiamos el signo para el próximo término

# Finalmente, multiplicamos la suma obtenida por 4 para obtener una aproximación de π
print(4 * suma)


# B

print("Calcularemos PI")
n = int(input("Ingrese la cantidad de términos: "))
π = 3.1415926535897932384626433832795
suma = 0  # Inicializamos la variable para almacenar la suma de términos
signo = 1  # Variable para alternar el signo de cada término en la serie

# Iteramos sobre los primeros n términos de la serie (1, 3, 5, ..., hasta el n-ésimo término impar)
# Empezamos desde 1 hasta n (de 2 en 2, para incluir solo los términos impares)
for i in range(1, n + 1, 2):
    suma = suma + 1 / i * signo  # Sumamos el término actual con el signo correspondiente
    signo = -signo  # Cambiamos el signo para el próximo término

# Finalmente, multiplicamos la suma obtenida por 4 para obtener una aproximación de π
print(4 * suma)
print(π)

# C = Cuantos mas cantidad de terminos elija, mas cerca estara de π

# D


print("Calcularemos PI")

epsilon = 0.000001  # Se define el margen de error permitido

suma = 0  # Inicializamos la variable para almacenar la suma de términos
signo = 1  # Variable para alternar el signo de cada término en la serie
i = 1  # Inicializamos el contador para los términos de la serie

pi = math.pi  # Obtenemos el valor de PI de la biblioteca math

# Utilizamos un bucle while para calcular la serie hasta que el error sea menor que epsilon
while abs(4 * suma - pi) > epsilon:
    suma = suma + 1 / i * signo  # Sumamos el término actual con el signo correspondiente
    signo = -signo  # Cambiamos el signo para el próximo término
    i = i + 2  # Incrementamos el contador para pasar al siguiente término impar

# Finalmente, imprimimos la aproximación de PI
print(4 * suma)

# Ejercicio 18
# a) Hacer un programa que permita al usuario elegir un número m y un n y muestre
# pares de numeros complementarios, o sea (m, n)(m + 1, n − 1)(m + 2, n − 2). . .(n −
# 1, m + 1)(n, m). Por ejemplo, el usuario ingresa 5 y 10, 5 será el complementario de
# 10, 6 el de 9 y 7 el de 8, y deberá mostrarse:
# 5 10
# 6 9
# 7 8
# 8 7
# 9 6
# 10 5

m = int(input("Ingrese un número natural: "))
n = int(input("Ingrese un número natural: "))

for i in range(1, n+1):
    print(m, n, end=" ")

    m = m+1
    n = n-1


# b) Ídem anterior pero deberá frenarse cuando el lado izquierdo pase a ser más grande que el derecho.


m = int(input("Ingrese un número natural: "))
n = int(input("Ingrese un número natural: "))


while n > m:
    print(m, n, end=" ")
    m = m+1
    n = n-1

# Ejercicio 19 ⋆ ♣
# a) Escribir un programa que permita al usuario elegir un número m y un n y muestre
# todos los pares de numeros que se pueden formar con los números que están entre
# ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberá mostrar
# 4 4
# 4 5
# 4 6
# 5 4
# 5 5
# 5 6
# 6 4
# 6 5
# 6 6

# b) Cambiar el programa para que use sólo un ciclo en vez de dos

# A

m = int(input("Ingrese un número natural: "))
n = int(input("Ingrese un número natural: "))

for i in range(m, n+1):
    for j in range(m, n+1):
        print(i, j, end="")

# B
for i in range(m * (n - m + 1), (n + 1) ** 2, m):
    print(i // n, i % n)


# Ejercicio 21 ⋆
# Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
# 0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
# suerte debe ser elegido al azar)
# Ejercicio 22 ⋆
# Hacer un programa que permita al usuario jugar al piedra, papel o tijera contra la computadora. Se debe jugar al mejor de 5, es decir, si uno de los participantes consigue 3 victorias el
# juego termina.
# Ejercicio 23 ⋆
# ¾Para qué números enteros distintos de cero es cierto que A + B + C = A x B x C ? (lo
# curioso es que sólo hay una solución)

# 21

numUser = int(input("Ingrese un número del 0 al 99 "))
apuesta = int(input("Monto a apostar "))

w = random.randint(0, 100)
print("el numero ganador es el ", w)

if numUser == w:
    print("Felicitaciones ganaste $:", apuesta*70)
else:
    print("perdiste, no adivinaste el numero")


# 22

# import random
vicUser = 0
vicCom = 0


while vicUser <= 3 or vicCom <= 3:
    user = int(input("Ingrese 1 para piedra, 2 para papel, 3 para tijera"))
    print(user)
    com = random.randint(1, 4)
    print(com)
if user == 1:
    if com == 1:
        print(" Empatamos, los 2 elegimos piedra")
    elif com == 2:
        vicCom = vicCom + 1
        print("Gano la com, el papel le gana a piedra")
    else:
        vicUser = vicUser + 1
        print("Gano usuario porque piedra le gana a tijera")
if user == 2:
    if com == 2:
        print(" Empatamos, los 2 elegimos papel")
    elif com == 1:
        vicUser = vicUser + 1
        print("Gano el usuario, el papel le gana a piedra")
    else:
        vicCom = vicCom + 1
        print("Gano la com porque tijera le gana a papel")
if user == 3:
    if com == 3:
        print(" Empatamos, los 2 elegimos tijera")
    elif com == 1:
        vicCom = vicCom + 1
        print("Gano la com, piedra le gana a tijera")
    else:
        vicUser = vicUser + 1
        print("Gano el usuario, porque tijera le gana a papel")

if vicUser >= 3:
    print("¡Has ganado el juego!")
else:
    print("La computadora ha ganado el juego.")


# import random

# vicUser = 0
# vicCom = 0

# while vicUser < 3 and vicCom < 3:
#     user = int(input("Ingrese 1 para piedra, 2 para papel, 3 para tijera: "))
#     com = random.randint(1, 3)

#     if user == com:
#         print("Empate. Ambos eligieron lo mismo.")
#     elif user == 1 and com == 3 or user == 2 and com == 1 or user == 3 and com == 2:
#         vicUser += 1
#         print("¡Ganaste esta ronda!")
#     else:
#         vicCom += 1
#         print("La computadora gana esta ronda.")

#     print(f"Usuario: {vicUser} - Computadora: {vicCom}")

# if vicUser >= 3:
#     print("¡Felicidades! Has ganado el juego.")
# else:
#     print("La computadora ha ganado el juego.")
