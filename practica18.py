#Hacer un algoritmo que #
#se ingresa dos precios (número decimal) 
#Mostrar los precios ordenado de mayor a menor
def mostrar_precios_ordenados():
    try:
        # Solicitar al usuario que ingrese dos precios (números decimales)
        precio1 = float(input("Ingresa el primer precio: "))
        precio2 = float(input("Ingresa el segundo precio: "))
        
        # Crear una lista con los precios ingresados
        precios = [precio1, precio2]
        
        # Ordenar la lista de precios de mayor a menor
        precios_ordenados = sorted(precios, reverse=True)
        
        # Mostrar los precios ordenados por pantalla
        print(f"Los precios ordenados de mayor a menor son: {precios_ordenados}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa números decimales.")

# Llamar a la función para ejecutar el programa
mostrar_precios_ordenados()
