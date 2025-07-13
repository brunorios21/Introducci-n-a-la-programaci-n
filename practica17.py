#Hacer un algoritmo que se ingresa un precio (número decimal)
#  y le calcula un incremento de 10% Mostrar por pantalla el resultado
def calcular_incremento():
    try:
        # Solicitar al usuario que ingrese un precio (número decimal)
        precio = float(input("Ingresa el precio: "))
        
        # Calcular el incremento del 10%
        incremento = precio * 0.10
        
        # Calcular el precio con el incremento incluido
        precio_con_incremento = precio + incremento
        
        # Mostrar el resultado por pantalla
        print(f"El precio inicial era: {precio:.2f}")
        print(f"El incremento del 10% es: {incremento:.2f}")
        print(f"El precio con el incremento del 10% es: {precio_con_incremento:.2f}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número decimal.")

# Llamar a la función para ejecutar el programa
calcular_incremento()
