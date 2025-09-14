# TRABAJO PRACTICO 2
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Eres menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad"))

if edad < 12:
    print("Niño/a")
elif edad >= 12:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese su contraseña: ")

if 8 <= len(contraseña) >=14:
    print("Contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números.

import random
from statistics import mode, median, mean

# Generamos una lista de 50 numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Lista de numeros:", numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media: 2f}")

# Determinamos el sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

texto = input("Ingrese una palabra o frase: ")

# Verificamos el ultimo caracter
if texto[-1].lower() in "aeiou":
    texto = texto + "!"
print("Resultado:", texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.


# Pedimos al usuario que ingrese su nombrre y una opcion
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opcion (1 = MAYUSCULAS, 2 = minusculas, 3 = Primera letra mayuscula): "))

if opcion == 1:
    print("Nombre en MAYUSCULAS:", nombre.upper())
elif opcion == 2:
    print("Nombre en minusculas:", nombre.lower())
elif opcion == 3:
    print("Nombre con la primera letra en mayuscula:", nombre.title())
else:
    print("opcion invalida. Ingrese 1, 2, 3.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud <= 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud <=5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud <= 6:
    print("Fuerte (puede causar daños en estructuras debiles).")
elif magnitud >= 6 and magnitud <= 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes en numero (1-12):"))
dia = int(input("Ingrese el dia (1-31): " ))

fecha = mes * 100 + dia

#Hemisferio norte
if hemisferio == "N":
    if (fecha >= 1221 and fecha <= 1231) or (fecha > 101 and fecha <= 320):
        estacion = "Invierno"
    elif fecha >= 321 and fecha <= 620:
        estacion = "Primavera"
    elif fecha >= 621 and fecha <= 920:
        estacion = "Verano"
    else:
        estacion = "Otoño"

#Hemisferio sur
elif hemisferio == "S":
    if (fecha >= 1221 and fecha <= 1231) or (fecha > 101 and fecha <= 320):
        estacion = "Verano"
    elif fecha >= 321 and fecha <= 620:
        estacion = "Otoño"
    elif fecha >= 621 and fecha <= 920:
        estacion = "Invierno"
    else:
        estacion = "Primavera"

else: 
    estacion = "Hemisferio invalido."

print("La estacion del año es:", estacion)