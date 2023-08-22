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


#6
#a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
#pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
#Python y por último correr el programa con los valores iniciales de las corridas y
#verificar que funciona como se esperaba.
#b) Ídem anterior pero para encontrar el menor

#ej encontrar mayor:
primerNum = int(input("Escriba un numero"))
segundoNum = int(input("Escriba otro numero"))

if primerNum > segundoNum : 
    print(primerNum, " primerNum es mayor")

elif segundoNum > primerNum :
    print(segundoNum, "segundoNum es mayor")

else :
    print("son iguales")

#ej encontrar menor:

primerNum = int(input("Escriba un numero"))
segundoNum = int(input("Escriba otro numero"))

if primerNum < segundoNum : 
    print(primerNum, " primerNum es menor")

elif segundoNum < primerNum :
    print(segundoNum, "segundoNum es menor")

else :
    print("son iguales")

 #7
#Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
#su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
#"Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.

nota1 = float(input("Escriba la nota"))
nota2 = float(input("Escriba la nota"))
promedio = nota1 + nota2 /2

if promedio >7 :
    print("aprobado")
else :
    print("desaprobado")