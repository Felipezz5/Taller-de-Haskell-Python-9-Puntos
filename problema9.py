# Problema 9
tipo = input("¿Quieres pizza vegetariana? (s/n): ")
if tipo.lower() == "s":
    print("Ingredientes: lechuga, champiñones, espinaca,: ")
    ingrediente = input("Elige un ingrediente: ")
    print("Pizza vegetariana con mozzarella, tomate y", ingrediente)
else:
    print("Ingredientes: pepperoni, jamon, piña")
    ingrediente = input("Elige un ingrediente: ")
    print("Pizza no vegetariana con mozzarella, tomate y", ingrediente)