#Hacer un algoritmo que pida un número entero y determine si es múltiplo de 5. 
# Muestra un mensaje por pantalla.
def determinar_multiplo_de_5():
    try:
        # Solicitar al usuario que ingrese un número entero
        numero = int(input("Ingresa un número entero: "))
        
        # Determinar si el número es múltiplo de 5
        if numero % 5 == 0:
            print(f"{numero} es múltiplo de 5.")
        else:
            print(f"{numero} no es múltiplo de 5.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar el programa
determinar_multiplo_de_5()

