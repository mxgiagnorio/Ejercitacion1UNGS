# 1

a = int(input("dame un numero entero"))
b = int(input("dame un numero entero"))
c = int(input("dame un numero entero"))

print("Usted ingreso los valores", a, b, c)
print(a, "es mayor que", b, a > b)
print(a, "y", b, "son iguales", a == b)
print(a, "es el mayor de todos", a > b and a > c)
print(b, "es el menor de todos", b < a and b < c)
print(a, "es mayor que alguno de los otros dos", a > b or a > c)
print(a, "es menor o igual que alguno de los otros dos", a <= b or a <= c)
print("Los tres numeros son iguales", a == b, c == b)
print("Los tres numeros son distintos", a != b, c != b, a != c)
print(a, "es par", a % 2 == 0)
print("alguno es par", a % 2 == 0 or b % 2 == 0 or c % 2 == 0)
print("Ninguno es par", a % 2 != 0 and b % 2 != 0 and c % 2 != 0)
print("Todos son pares", a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
print(a, "es multiplo de 3", a % 3 == 0)
print(a, "es multiplo de 3 y de 5", a % 3 == 0 and a % 5 == 0)
print(a, "es multiplo de 3 y par", a % 3 == 0 and a % 2 == 0)
print(a, "-", b, "da numero positivo", (a - b) > 0)
print(a, "-", b, "da un numero par positivo", (a - b) > 0 and (a-b) % 2 == 0)

# 2
# Un ciudadano argentino está exento de votar en estos casos:
# Tiene más de 70 años
# Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
# Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano,
# escribir la expresión lógica que representa esta situación


edad = int(input("Que edad tiene el votante?"))
distancia = int(input("A que distancia esta el votante?"))

if edad >= 18 and edad < 70 and distancia <= 500:
    print("Vota")
else:
    print("no vota")


# 3
# Para cada uno de los siguientes programas indicar qué se imprime cuando se ejecuta
# A

a = 10
if a != 0:
    print("perro")

    # perro

# B

a = 10
if a > 0:
    print("manzana")
else:
    print("naranja")

    # Manzana

# C


a = 10
if a > 0:
    print("Te quiero")
print("bien lejos")

# Te quiero

# D


a = 5
b = 3
c = 2
if a < b * c:
    print("Hola!")
else:
    print("Chau!")

    # Hola

# E

p1 = 3, 14
p2 = 3, 141569
if p1 == p2:
    print("p1 y p2 son iguales!")
else:
    print("p1 y p2 no son iguales!")

# "p1 y p2 no son iguales"

# F

a = "Hola"
b = "hola"
if a == b:
    print("Python es insensible!")
else:
    print("Python es muy sensible!")

# Python es muy sensible"


# Leer el siguiente programa.¿Para qué valores de la variable a imprime "hola!"  cuando se
# ejecuta? y para cuáles "chau!"?

a = int(input("Ingrese un valor para a"))
if a == 0:
    print("hola!")
else:
    print("chau!")

# Imprime "hola!" unicamente para los valores que sean iguales a 0. Para cualquier otro imprimira "Chau!"

# 5
# Escribir en papel un programa que pida una nota y que en el caso de que sea menor a cuatro
# muestre "Debe recuperar". Luego pasarlo a Python

nota = int(input("Que nota se saco)"))

if nota < 4:
    print("debe recuperar")


# 6
# a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
# pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
# Python y por último correr el programa con los valores iniciales de las corridas y
# verificar que funciona como se esperaba.
# b) Ídem anterior pero para encontrar el menor

# ej encontrar mayor:
primerNum = int(input("Escriba un numero"))
segundoNum = int(input("Escriba otro numero"))

if primerNum > segundoNum:
    print(primerNum, " primerNum es mayor")

elif segundoNum > primerNum:
    print(segundoNum, "segundoNum es mayor")

else:
    print("son iguales")

# ej encontrar menor:

primerNum = int(input("Escriba un numero"))
segundoNum = int(input("Escriba otro numero"))

if primerNum < segundoNum:
    print(primerNum, " primerNum es menor")

elif segundoNum < primerNum:
    print(segundoNum, "segundoNum es menor")

else:
    print("son iguales")

 # 7
# Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
# su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
# "Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.

nota1 = float(input("Escriba la nota"))
nota2 = float(input("Escriba la nota"))
promedio = nota1 + nota2 / 2

if promedio > 7:
    print("aprobado")
else:
    print("desaprobado")


# 8
# Escribir en papel un programa que tome un número entero positivo ingresado por el usuario
# y muestre por pantalla "Usted ingresó un número de una sola cifra" o "Usted ingresó un número
# de más de una cifra" según corresponda. Realizar 4 corridas de escritorio, escribirlo en Python
# y luego correrlo en la computadora con los valores iniciales de las corridas y verificar que hayan
# dado como se esperaba.

num = int(input("Ingrese un numero entero positivo"))

if num >= 0 and num < 10:
    print("Usted ingreso un numero de una sola cifra")
else:
    print("Usted ingreso un numero de mas de una cifra")

# 9
# Se tiene la siguiente lista con DNIs de personas.
# 30612453
# 23763290
# 21448503
# 34582048
# 15364857
# Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
# de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python

dni = int(input("Escriba el dni que desea buscar"))

dni1 = 30612453
dni2 = 23763290
dni3 = 21448503
dni4 = 34582048
dni5 = 15364857

if dni == dni1 or dni == dni2 or dni == dni3 or dni == dni4 or dni == dni5:
    print("El dni esta en la lista")
else:
    print("El dni no se encuentra en la lista")


# 10
# Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
# cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
# fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
# a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
# comienzo y al fin del período.


consumo = int(input("¿Cuantos kw consumio el usuario?"))
tarifaFija = 480
kw = 25.5
impuestos = 78

print("El consumo fue de",consumo," KW")

if consumo >200 : 
    total = (consumo-200)*kw + tarifaFija + impuestos
    print ("el usuario debera pagar", "$",total, "por el consumo de ",consumo,"KW")
else : 
    total = tarifaFija + impuestos
    print("El usuario debera pagar","$",total,"por el consumo de",consumo,"KW")


#11
# Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
# ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
# verificar los resutlados.

a = int(input("Escriba un numero entero"))
b = int(input("Escriba un numero entero"))
c = int(input("Escriba un numero entero"))

if a > b and a > c :
    print(a,"es el mayor")
elif b > a and b > c :
    print(b,"es el mayor")
elif c > a and c > b :
    print(c,"es el mayor")
elif a > b and a == c :
    print (a,"y",c,"Son iguales y mayores que",b)
elif b > a and b == c :
    print (b,"y",c,"Son iguales y mayores que",a)
elif a  > c and a == b :
    print (a,"y",b,"Son iguales y mayores que",c)
else :
    print (a,b,c,"Son iguales")

# 12
# Un profesor clasifica las notas de sus alumnos de la siguiente manera:
# 1-3 Reprobado
# 4-6 Debe rendir examen final
# 7-10 Eximido
# a) Escribir un programa que indique la clasificación de una nota.
# b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
# del mismo.

#a)

nota = int(input("Escriba la nota del alumno"))

if nota >= 7 :
    print ("El alumno esta eximido")
elif nota >=4 and nota <=6 :
    print ("El alumno debera rendir un final")
else :
    print ("El alumno sera reprobado")
    
#b)

nota1 = int(input("Escriba la nota del alumno"))
nota2 = int(input("Escriba la nota del alumno"))
nota3 = int(input("Escriba la nota del alumno"))
promedio = (nota1 + nota2 + nota3)//3

if promedio >= 7 :
    print ("El alumno esta eximido")
elif promedio >=4 and promedio <=6 :
    print ("El alumno debera rendir un final")
else :
    print ("El alumno sera reprobado")

# 13 
# Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
# mayor que el segundo o viceversa.

num1 = int(input("Escriba un numero entero"))
num2 = int(input("Escriba otro numero entero"))

if num1 > num2 : 
    print (num1,"es mayor que",num2)
else :
    print(num2,"es mayor que",num1)

# 14 
# Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
# primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
# valores de las variables y mostrarlos de mayor a menor

num1 = int(input("Escriba un numero entero"))
num2 = int(input("Escriba otro numero entero"))

if num1 < num2 : 
    valorNum1 = num1
    num1 = num2
    num2 = valorNum1 
    print("num1",num1,"num2",num2)
else :
    print(num1,"es mayor a",num2)
    
# 15
# Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
# El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
# b el intermedio y en c el mayor (es decir, ordenará los valores).

a = int(input("ingrese un valor"))
b = int(input("ingrese un valor"))
c = int(input("ingrese un valor"))

print("el valor de a es",a,"el valor de b es",b,"el valor de c es",c)

if a > b and a > c and b > c :
    valorA = a
    a=c
    c=valorA
    print("c es",c,"b es",b,"a es",a)

elif b>a and b>c and a>c : 
        valorc = c
        valorA = a
        c=b
        b=valorA
        a=valorc
        print("c es",c,"b es",b,"a es",a)

elif b>a and b>c and c>a : 
        valorc = c
        c=b
        b=valorc
        print("c es",c,"b es",b,"a es",a)

else :
   print("c es",c,"b es",b,"a es",a)


