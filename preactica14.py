#Hacer un algoritmo que ingresé un número decimal, 
# súmale 15 y dividí por 2 mostrar el resultado por pantalla en formato decimal
def operacion_numerica():
    try:
        # Solicitar al usuario que ingrese un número decimal
        numero_decimal = float(input("Ingresa un número decimal: "))
        
        # Realizar la operación: sumar 15 y dividir por 2
        resultado = (numero_decimal + 15) / 2
        
        # Mostrar el resultado por pantalla en formato decimal
        print(f"El resultado es: {resultado:.2f}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número decimal.")

# Llamar a la función para ejecutar el programa
operacion_numerica()
