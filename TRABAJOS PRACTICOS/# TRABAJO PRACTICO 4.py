# TRABAJO PRACTICO 4

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0-101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un numero entero: "))
print("Cantidad de digitos: ", len(str(abs(num))))

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0

for i in range(min(a, b) + 1, max(a, b)):
    suma += 1
print("La suma es: ", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0 
while True:
    n = int(input("Ingrese un numero (0 para terminar): "))
    if n == 0:
        break
    suma += 1
print("La suma total es: ", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el numero entre 0-9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"Correcto! {intentos} intentos.")
        break

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += 1
print("La suma es: ", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

cantidad = int(input("Ingrese un numero (hasta 100): "))

for i in range(cantidad):
    n = int(input(f"Ingrese el numero {i + 1}: "))

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("\nresultados:")
print("Pares", pares)
print("Impares", impares)
print("Negativos", negativos)
print("Positivos", positivos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor)

suma = 0
cantidad = int(input("Ingrese un numero (hasta 100): "))

for i in range(cantidad):
    n = int(input(f"Ingrese el numero {i + 1}: "))
    suma += n

media = suma / cantidad
print("\nLa media de valores es: ", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un numero entero: "))

invertido = int(str(numero)[::-1])
print("NUmero invertido: ", invertido)
