#Hacer un programa que ingresa un precio y calcula un descuento del 9%.
#Mostrar por pantalla el resultado
def calcular_descuento():
    try:
        # Solicitar al usuario que ingrese el precio
        precio = float(input("Ingresa el precio: "))
        
        # Calcular el descuento del 9%
        descuento = precio * 0.09
        
        # Calcular el precio final con descuento
        precio_final = precio - descuento
        
        # Mostrar el resultado con formato
        print(f"El precio final con descuento del 9% es: {precio_final:.2f}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número válido.")

# Llamar a la función para ejecutar el programa
calcular_descuento()
