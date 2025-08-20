# Problema 7
puntuacion = int(input("Ingresa la puntuacion del empleado: "))
if puntuacion >= 10:
    print("Excelente, recibe $200000")
elif puntuacion >= 7:
    print("Bueno, recibe $100000")
elif puntuacion >= 5:
    print("Meh, recibe $50000")
else:
    print("Pongase a trabajar, no recibe recompensa")