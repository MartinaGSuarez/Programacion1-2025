import random

print("=== Juego: Piedra, Papel o Tijera ===")

jugador_gana = 0
computadora_gana = 0

# OPCIONES DEL JUEGO
opciones = ["piedra", "papel", "tijera"]

while True:
    print("/nElige una opcion: ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    eleccion = input("Ingrese un numero de su opcion: ")

    if eleccion == "4":
        print("\nSaliendo del juego ...")
        break
    if eleccion not in ["1", "2", "3"]:
        print("Opcion invalida, intenta de nuevo. ")
        continue

    jugador = opciones[int(eleccion) - 1]
    computadora = random.choice(opciones)

    print(f"\nTu elegiste: {jugador}")
    print(f"La computadora eligio: {computadora}")

    # COMPARACION DE JUGADAS
    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
    (jugador == "tijera" and computadora == "papel") or \
    (jugador == "papel" and computadora == "piedra"):
        print("Ganaste!")
        jugador_gana += 1
    else:
        print("La computadora gana!")
        computadora_gana += 1

    # MOSTRAR MARCADOR PARCIAL
    print(f"\nMarcador -> Jugador: {jugador_gana} | Computadora. {computadora_gana}")

# RESULTADO FINAL
print("\n=== Resultado Final ===")
print(f"Jugador: {jugador_gana} | Computadora: {computadora_gana}")

if jugador_gana > computadora_gana:
    print("¡Felicidades! Ganaste el juego.")
elif computadora_gana > jugador_gana:
    print("La computadora gano esta vez.")
else:
    print("Fue un empate.")