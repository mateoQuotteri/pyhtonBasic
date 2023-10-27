# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Inicializar el factorial como 1
factorial = 1

# Calcular el factorial del número ingresado
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print("El factorial de", numero, "es", factorial)