# Problema 6
nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu genero (M/F): ")
if genero.upper() == "F":
    print(nombre, "esta en el Grupo A")
elif genero.upper() == "M":
    print(nombre, "esta en el Grupo B")