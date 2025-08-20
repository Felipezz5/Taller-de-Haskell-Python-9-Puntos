# Problema 3 
try:
    num1 = float(input("Ingresa el numero que quieres dividir: "))
    num2 = float(input("Ingresa el divisor: "))
    print("Resultado:", num1 / num2)
except ZeroDivisionError:
    print("No se puede dividir por cero")