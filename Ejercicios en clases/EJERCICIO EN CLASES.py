#CIFRA DE CESAR (alfabeto español con ñ) para 5 mensajes

alfabeto = "abcdefghijklmñnopqrstuvwyxz" 
ALFABETO = alfabeto.upper

def cifrar_cesar(texto: str, corrimiento: int) -> str:
    corr = corrimiento % 27  # aseguramos 0..26
    salida = []

    for ch in texto:
        if ch in alfabeto:
            i = alfabeto.index(ch)
            salida.append(alfabeto[(i + corr) % 27])
        elif ch in ALFABETO:
            i = ALFABETO.index(ch)
            salida.append(ALFABETO[(i + corr) % 27])
        else:
            # caracteres no alfabéticos se dejan igual (espacios, signos, números, acentos, etc.)
            salida.append(ch)
    return "".join(salida)

# --- Programa principal ---
while True:
    try:
        corrimiento = int(input("Ingrese el corrimiento (entero, puede ser negativo): "))
        break
    except ValueError:
        print("Valor inválido. Intente nuevamente.")

for i in range(1, 6):  # 5 mensajes
    mensaje = input(f"Mensaje {i}: ")
    cifrado = cifrar_cesar(mensaje, corrimiento)
    print(f"Cifrado {i}: {cifrado}")
