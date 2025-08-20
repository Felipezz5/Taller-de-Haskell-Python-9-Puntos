
# Problema 1
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Problema 2 
contrasena = "lebronjames123"
ingreso = input("Escribe la contraseña: ")
if contrasena.lower() == ingreso.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# Problema 3 
try:
    num1 = float(input("Ingresa el numero que quieres dividir: "))
    num2 = float(input("Ingresa el divisor: "))
    print("Resultado:", num1 / num2)
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Problema 4
n = int(input("Ingresa un numero: "))
if n % 2 == 0:
    print("Eel numero es par")
else:
    print("El numero es impar")

# Problema 5
edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresa tus ingresos anuales: "))
if edad >= 18 and ingresos >= 160232000:
    print("Debes declarar renta")
else:
    print("No debes declarar renta")

# Problema 6
nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu genero (M/F): ")
if genero.upper() == "F":
    print(nombre, "esta en el Grupo A")
elif genero.upper() == "M":
    print(nombre, "esta en el Grupo B")


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

# Problema 8
edad_cliente = int(input("Ingresa tu edad: "))
if edad_cliente < 12:
    print("Precio del ticket: $5000")
elif edad_cliente < 18:
    print("Precio del ticket: $8000")
elif edad_cliente < 65:
    print("Precio del ticket: $12000")
else:
    print("Precio del ticket: $6000")

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
