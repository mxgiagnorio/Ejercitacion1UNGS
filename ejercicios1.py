
# EJERCICIO NUMERO 6
# Escribir un programa en la computadora que imprima en pantalla

print("Mi primer programa en PYTHON")

# EJERCICIO NUMERO 7
"""
Escribir un programa en la computadora que imprima en pantalla
v
e
r
t
i
c
a
l
con un solo print. Ayuda, usar: print("\n")
"""

print("\n", "v", "\n", "e", "\n", "r", "\n", "t",
      "\n", "i", "\n", "c", "\n", "a", "\n", "l")

# Ejercicio 8

"""Escribir un programa en Python que imprima la siguiente figura en la pantalla:
*****
* *
* *
* *
*****
con un solo print.
"""

print("\n", "*****", "\n", "*", "", "*", "\n", "*",
      "", "*", "\n", "*", "", "*", "\n", "*****")

# Ejercicio 9

"""
Escribir un programa en Python que imprima la siguiente figura en la pantalla utilizando un solo print:

*
***
*****
*******
*********
"""

print("\n", "*", "\n", "***""", "\n", "*****",
      "\n", "*******", "\n", "*********")

# Ejercicio 10

# Escribir un programa en Python que pida un dato al usuario y lo imprima por pantalla.

userName = input(("¿Como te llamas?"))

print("Mi nombre es ", userName)

# Ejercicio 11


# Escribir un programa en Python que pida al usuario que ingrese un valor y luego imprima en la
# pantalla:
# ******************************
# * El resultado es: <valor>
# ******************************
# donde en vez de <valor> debe mostrarse el valor que el usuario ingresó por teclado.

valor = int(input("¿Cuantos años tenes?"))

print("Tengo", valor, "años")

# Ejercicio 13
# Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
# su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
# a invertir y la cantidad de meses

inversion = int(input("Escriba cuanto desea invertir"))
meses = int(input("Escriba la cantidad de meses"))

print("usted tendra en su cuenta", inversion*6/100+inversion*meses, "$")

# Ejercicio 14
# Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
# costo por comunicación es de $3 y por cada segundo se cobra $0, 25 hacer dicho programa. Se deben
# ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
# el precio a cobrar

costo = int(input("Cantidad de llamadas"))
costoXSeg = float(input("Tiempo en segundos del costo del programa"))

print(costo*3 + costoXSeg*0, 25)

# Ejercicio 15
# Un vendedor recibe un sueldo base de $7000 más un 10 % extra del total de sus ventas, el vendedor
# desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en
# cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada
# una de las ventas del mes e indique cuál será el sueldo final del vendedor.

sueldoBase = 7000
venta1 = int(input("Monto de la venta"))
venta2 = int(input("Monto de la venta"))
venta3 = int(input("Monto de la venta"))

print("El sueldo final del vendedor sera de ",
      venta1+venta2+venta3*10/100 + sueldoBase, "$")

# Ejercicio 16
# Determinar cuántos segundos tiene una hora, y cuántos tiene un día.
# Escribir una expresión matemática que transforme un lapso de tiempo expresado en segundos a uno
# expresado en minutos.
# Escribir otra para transformar a horas y una última que transforme a días.
# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos
# minutos son, así como también cuantas horas y cuantos días

# El dia en segundos:

# unMinutoEnSegundos = 60
# unaHoraEnSegundos = unMinutoEnSegundos*60
# unDiaEnSegundos = unaHoraEnSegundos*24

# Si tuviera 4500 segundos y quisiera pasarlo a horas deberia hacer: 4500/60
# Si tuviera 15000 segundos y quisiera pasarlo a horas deberia hacer: (15000/60)/60
# Si tuviera 90000 segundos y quisiera pasarlo a dias deberia hacer: (90000/60)/60/24

cantidadSegundos = int(input("Escriba la cantidad de segundos"))
minutos = cantidadSegundos/60
horas = minutos/60
dias = horas/24

print("La cantidad de segundos que escribio equivalen a", minutos, "minutos")
print("La cantidad de segundos que escribio equivalen a", horas, "horas")
print("La cantidad de segundos que escribio equivalen a", dias, "dia/s")

# Ejercicio 17
# La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
# billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada
# denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda:
# El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.

billetes = int(input("ingrese la cantidad de dinero que desea retirar"))

billeteDe10 = billetes/10
billeteDe20 = billetes/20
billeteDe50 = billetes/50
billeteDe100 = billetes/100
billeteDe1000 = billetes/1000
billeteDe2000 = billetes/2000

# Ejercicio 18
# Escribir una expresión que dada una cantidad de segundos, evalúe a la cantidad de horas que éstos
# representan, pero esta vez descontando el total de días completos. Por ejemplo: 90.000 segundos
# equivalen exactamente a 1 día y 1 hora, por lo que dados 90.000 segundos la expresión debería dar
# 1 hora.

segundosEnHoras = 90000//60//60-24
print(segundosEnHoras)

# 90000 seg lo divido por 60(cant.minutos), eso me da esa cantidad de segundos en min, a eso lo divido por 60(cant.min en una hora)
# eso me va a dar la cantidad de horas que hay en 90000 segundos y a ese resultado le descuento 24 que son las horas que tiene un dia.


# Ídem punto anterior para minutos y segundos.
# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla
# la cantidad de días, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461
# segundos el programa debe mostrar por pantalla: 1 día 0 horas 1 minuto 1 segundo.

segundos = int(input("Escriba la cantidad de segundos"))
minutos = segundos//60
horas = minutos//60
dias = horas//24

print(dias, "dia/s", horas, "horas", minutos, "minutos", segundos, "segundos")

# Ejercicio 19
# Escribir en Python un programa que pida al usuario que ingrese dos valores y los guarde en dos
# variables, x e y. El programa deberá intercambiar los valores de x e y y luego mostrar en pantalla:
# El valor de x es: <x>
# El valor de y es: <y>
# donde en lugar de <x> e <y> deberá mostrarse el valor de las respectivas variables
