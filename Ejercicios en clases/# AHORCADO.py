# AHORCADO
import random

# LISTA DE SABORES DE HELADO
def elegir_palabra():
    sabores = ["chocolate","vainilla", "frutilla", "limon", "sambayon", "maracuya", "pistacho", "tiramisu", "frambuesa", "coco"]
    return random.choice(sabores)


# Dibujos del ahorcado segun los intentos

AHORCADO = [
    """
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    =========
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   / 
    |
    =========
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |    
    |
    =========
    """,
    """
    ------
    |    |
    |    O
    |   /|
    |    
    |
    =========
    """,
    """
    ------
    |    |
    |    O
    |    |
    |    
    |
    =========
    """,
    """
    ------
    |    |
    |    O
    |    
    |    
    |
    =========
    """,
    """
    ------
    |    |
    |    
    |    
    |    
    |
    =========
    """

]

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + ""
        else:
            tablero += "_ "
    return tablero

palabra = elegir_palabra()
letras_adivinadas = []
intentos = 6
print("¡Bienvenidos al Ahorcado de sabores de helados!")

while intentos >= 0:
    print(AHORCADO[intentos])
    print("Palabra:", mostrar_tablero(palabra, letras_adivinadas))
    print("Intentos restantes: ", intentos)

    if all(letra in letras_adivinadas for letra in palabra):
        print("n\ ¡Ganaste! El sabor era:", palabra.upper())
        break

    if intentos == 0:
        print("n\ Perdiste. El sabor era:", palabra.upper())
        break

    letra = input("Ingresa una letra:").lower()
    
    if letra in letras_adivinadas:
        print("Ya intentaste esta letra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra:
        print("La letra esta en la palagra. ¡Sigue asi!")
    else:
        print("La letra no esta en la palabra.")
        intentos -= 1


