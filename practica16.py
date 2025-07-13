#Hacer un algoritmo que ingresa un número, mostrar por pantalla si es par
def determinar_par_o_impar():
    try:
        # Solicitar al usuario que ingrese un número entero
        numero = int(input("Ingresa un número entero: "))
        
        # Determinar si el número es par o impar
        if numero % 2 == 0:
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} es un número impar.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar el programa
determinar_par_o_impar()
