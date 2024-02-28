import math

g = float(input("Ingrese la constante g: "))
r = int(input("Ingrese el radio kilómetros: "))

r = r * 1000

ve = math.sqrt(2 * g * r)

print(f"La velocidad de escape es: {ve} m/s")