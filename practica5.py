#Hacer un programa en el que se ingresa precio y calcula el precio final con el iva (21%).
# Mostrar el resultado por pantalla
def calcular_precio_final_con_iva():
    try:
        # Solicitar al usuario que ingrese el precio sin IVA
        precio_sin_iva = float(input("Ingresa el precio sin IVA: "))
        
        # Calcular el precio con IVA (21%)
        iva = 0.21
        precio_con_iva = precio_sin_iva * (1 + iva)
        
        # Mostrar el resultado con formato
        print(f"El precio final con IVA (21%) incluido es: {precio_con_iva:.2f}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número válido.")

# Llamar a la función para ejecutar el programa
calcular_precio_final_con_iva()
