#TRABAJO PRACTICO 1
# EJERCICIO 1
# SE IMPRIME POR PANTALLA "Hola, mundo"
print( "Hola, mundo")


# EJERCICIO 2
# LE PEDIMOS AL USUARIO QUE INGRESE SU NOMBRE
nombre = input(f"Por favor, ingrese su nombre: ")

# SE IMPRIME POR PANTALLA "Hola, <nombre>"
print(f"Hola, {nombre}")


# EJERCICIO 3
# LE PEDIMOS AL USUARIO QUE INGRESE SU NOMBRE, APELLIDO, EDAD Y RESIDENCIA
nombre = input(f"Por favor, ingrese su nombre: ")
apellido = input(f"Por favor, ingrese su apellido: ")
edad = input(f"Por favor, ingrese su edad: ")
residencia = input(f"Por favor, ingrese su residencia: ")

# SE IMPRIME POR PANTALLA "Soy <nombre>, <apellido>, tengo <edad> años y vivo en <residencia>"
print(f"Soy {nombre}, {apellido}, tengo {edad} años y vivo en {residencia}")


# EJERCICIO 4
# LE PEDIMOS AL USUARIO EL RADIO DE UN CIRCULO 
import math

radio_circulo = float(input(f"Por favor, ingrese el radio del circulo: "))

# SE CALCULA EL AREA DEL CIRCULO
area_circulo = math.pi * (radio_circulo ** 2)

# SE CALCULA EL PERIMETRO DEL CIRCULO
perimetro_circulo = 2 * math.pi * radio_circulo

# SE IMPRIME POR PANTALLA "El area del circulo es <area_circulo> y el perimetro es <perimetro_circulo>"
print(f"El area del circulo es {area_circulo} y el perimetro es {perimetro_circulo}")



# EJERCICIO 5
# LE PEDIMOS AL USUARIO QUE INGRESE LA CANTIDAD DE SEGUNDOS
cantidad_segundos = int(input(f"Por favor, ingrese la cantidad de segundos a convertir: "))

# SE CALCULA LA CANTIDAD DE HORAS, SABIENDO QUE 1 HORA TIENE 3600 SEGUNDOS
cantidad_horas = cantidad_segundos // 3600

# SE IMPRIME POR PANTALLA "La cantidad de horas es <cantidad_horas>"
print(f"La cantidad de horas es {cantidad_horas}")



# EJERCICIO 6
# LE PEDIMOS AL USUARIO QUE INGRESE UN NUMERO 
numero_a_multiplicar = int(input(f"Por favor, ingrese un numero: "))

# SE REALIZAN LAS MULTIPLICACIONES DEL NUMERO INGRESADO POR EL USUARIO 
numero_por_0 = numero_a_multiplicar * 0
numero_por_1 = numero_a_multiplicar * 1
numero_por_2 = numero_a_multiplicar * 2
numero_por_3 = numero_a_multiplicar * 3
numero_por_4 = numero_a_multiplicar * 4
numero_por_5 = numero_a_multiplicar * 5
numero_por_6 = numero_a_multiplicar * 6
numero_por_7 = numero_a_multiplicar * 7
numero_por_8 = numero_a_multiplicar * 8
numero_por_9 = numero_a_multiplicar * 9

# SE IMPRIME POR PANTALLA EL RESULTADO, UTILIZANDO COMILLAS TRIPLES
print(f"""
      {numero_a_multiplicar} * 0 = {numero_por_0}
      {numero_a_multiplicar} * 1 = {numero_por_1}
      {numero_a_multiplicar} * 2 = {numero_por_2}
      {numero_a_multiplicar} * 3 = {numero_por_3}
      {numero_a_multiplicar} * 4 = {numero_por_4}
      {numero_a_multiplicar} * 5 = {numero_por_5}
      {numero_a_multiplicar} * 6 = {numero_por_6}
      {numero_a_multiplicar} * 7 = {numero_por_7}
      {numero_a_multiplicar} * 8 = {numero_por_8}
      {numero_a_multiplicar} * 9 = {numero_por_9}""")



# EJERCICIO 7
# LE PEDIMOS AL USUARIO QUE INGRESE DOS NUMEROS DINTINTOS A 0, PARA REALIZAR LA SUMA, RESRA, MULTIPLICACION Y DIVISION
numero_a = float(input(f"Por favor, ingrese el primer numero distinto a 0: "))
numero_b = float(input(f"Por favor, ingrese el segundo numero distinto a 0: "))

# SE RELIZAN LAS OPERACIONES ARITMETICAS
# SE REALIZA LA SUMA DE LOS NUMEROS PARA ALMACENAR EL RESULTADO EN LA VARIABLE suma_a_b
suma_a_b = numero_a + numero_b

# SE REALIZA LA RESTA DE LOS NUMEROS PARA ALMACENAR EL RESULTADO EN LA VARIABLE resta_a_b
resta_a_b = numero_a - numero_b

# SE REALIZA LA MULTIPLICACION DE LOS NUMEROS PARA ALMACENAR EL RESULTADO EN LA VARIABLE multiplicacion_a_b
multiplicacion_a_b = numero_a * numero_b

# SE REALIZA LA DIVISION DE LOS NUMEROS PARA ALMACENAR EL RESULTADO EN LA VARIABLE division_a_b, REDONDEANDO A 2 DECIMALES
division_a_b = round(numero_a / numero_b, 2)

# SE IMPRIME POR PANTALLA EL RESULTADO DE LAS OPERACIONES ARITMETICAS, UTILIZANDO COMILLAS TRIPLES
print(f"""   La suma de {numero_a} + {numero_b} es: {suma_a_b}
      La resta de {numero_a} - {numero_b} es: {resta_a_b}
      La multiplicacion de {numero_a} * {numero_b} es: {multiplicacion_a_b}
      La division de {numero_a} / {numero_b} es: {division_a_b}""")



#EJERCICIO 8
#LE PEDIMOS AL USUARIO QUE INGRESE SU ALTURA EN METROS Y SU PESO EN KILOGRAMOS
altura = float(input(f"Por favor, ingrese su altura en metros: "))
peso = float(input(f"Por favor, ingrese su peso en kilogramos: "))

# SE CALCULA EL IMC CON LA FORMULA PESO / ALTURA^2
imc = round(peso / (altura ** 2), 2)

# SE IMPRIME POR PANTALLA "Su indice de masa corporal es <imc>"
print(f"Su indice de masa corporal es {imc}")



# EJERCICIO 9
# LE PEDIMOS AL USUARIO QUE INGRESE UNA TEMPERATURA EN GRADOS CELSIUS
temperatura_celsius = float(input(f"Por favorr, ingrese una temperatura en grados celsius. "))

# SE CONVIERTE LA TEMPERATURA A GRADOS FAHRENHEIT CON LA FORMULA (C * 9/5) + 32
temperatura_fahrenheit = round((temperatura_celsius * 9/5) + 32, 2)

# SE IMPRIME POR PANTALLA "La temperatura en grados fahrenheit es <temperatura_fahrengeit>"
print(f"La temperatura en grados fahrenheit es {temperatura_fahrenheit}")



# EJERCICIO 10
# LE PEDIMOS AL USUARIO QUE INGRESE 3 NUMEROS 
numero_1 = float(input(f"Por favor, ingrese el primer numero: "))
numero_2 = float(input(f"Por favor, ingrese el segundo numero: "))
numero_3 = float(input(f"Por favor ingrese el tercer numero: "))

# SE IMPRIME POR PANTALLA EL PROMEDIO DE LOS 3 NUMEROS
promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los 3 numeros es {promedio}")

