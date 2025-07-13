# Solicitar al usuario que ingrese un número entero no negativo
numero = int(input("Ingrese un número entero no negativo: "))

# Validar que el número sea no negativo
if numero < 0:
    print("¡El número ingresado es negativo!")
else:
    # Calcular el factorial
    factorial = 1
    if numero != 0:
        for i in range(1, numero + 1):
            factorial *= i
    
    # Imprimir el resultado del cálculo
    print(f"El factorial de {numero} es {factorial}")

