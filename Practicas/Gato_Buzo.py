import random
import time

# Al presionar la bandera verde

peces = 0

# Cambiar disfraz a Fish-d
disfraz = "Fish-d"

# Posición inicial
x = 150
y = -10

print("Peces:", peces)
print("Disfraz:", disfraz)
print("Posición inicial:", x, y)

# Equivalente al bloque "por siempre"
while True:

    # Simulamos si el pez está tocando a Sprite1
    tocando = input(
        "¿El pez está tocando a Sprite1? (s/n, q para salir): "
    ).lower()

    if tocando == "q":
        break

    if tocando == "s":

        # Cambiar Peces en 1
        peces += 1
        print("Peces:", peces)

        # Tocar sonido Coin hasta que termine
        print("[Sonido: Coin]")
        time.sleep(1)

        # Ir a una posición aleatoria
        x = random.randint(-240, 240)
        y = random.randint(-180, 180)

        print("Nueva posición:", x, y)

        # Siguiente disfraz
        print("[Siguiente disfraz]")

print("Programa terminado.")
