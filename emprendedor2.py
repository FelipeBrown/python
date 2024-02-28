p= float(input("Ingrese el precio de suscripción para usuarios normales: "))
u = int(input("Ingrese el número de usuarios normales: "))
up = int(input("Ingrese el número de usuarios premium: "))
gt = int(input("ingrese gasto total: "))

preciopremiun = 1.5 * p

up = up * preciopremiun


utilidades = p * u + up -gt


print(f"Las utilidades del proyecto son: {utilidades}")