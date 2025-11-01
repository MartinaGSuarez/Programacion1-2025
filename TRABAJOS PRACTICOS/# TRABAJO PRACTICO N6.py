import math

# 1️⃣ Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")


# 2️⃣ Saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# 3️⃣ Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4️⃣ Área y perímetro del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# 5️⃣ Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600


# 6️⃣ Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7️⃣ Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division


# 8️⃣ Calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)


# 9️⃣ Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# 🔟 Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# 🧠 Programa principal
def main():
    print("=== 1. Hola Mundo ===")
    imprimir_hola_mundo()
    print()

    print("=== 2. Saludo Personalizado ===")
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))
    print()

    print("=== 3. Información Personal ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()

    print("=== 4. Área y Perímetro del Círculo ===")
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
    print()

    print("=== 5. Segundos a Horas ===")
    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas.")
    print()

    print("=== 6. Tabla de Multiplicar ===")
    numero = int(input("Ingrese un número: "))
    tabla_multiplicar(numero)
    print()

    print("=== 7. Operaciones Básicas ===")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
    print()

    print("=== 8. Calcular IMC ===")
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))
    print(f"Su IMC es: {calcular_imc(peso, altura)}")
    print()

    print("=== 9. Celsius a Fahrenheit ===")
    celsius = float(input("Ingrese temperatura en °C: "))
    print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")
    print()

    print("=== 10. Calcular Promedio ===")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
    print()


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
