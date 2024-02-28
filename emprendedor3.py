p = int(input("Ingrese el precio de suscripción: "))
u = int(input("Ingrese el número de usuario: "))
gt = int(input("Ingrese el gasto total: "))
utilidades_anteriores = float(input("ingresa utilidades_anteriores: "))

utilidades = p * u - gt
razon = utilidades_anteriores / utilidades

print(f"la utilidad es:{razon:.2f}")
