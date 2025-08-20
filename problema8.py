# Problema 8
edad_cliente = int(input("Ingresa tu edad: "))
if edad_cliente < 12:
    print("Precio del ticket: $6000")
elif edad_cliente < 18:
    print("Precio del ticket: $9000")
elif edad_cliente < 65:
    print("Precio del ticket: $13000")
else:
    print("Precio del ticket: $7000")
