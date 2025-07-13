#Hacer un algoritmo que nos permita introducir un número, 
# luego muestre por pantalla el mensaje 
# “Este número es positivo” o “Este número es negativo”

def determinar_positivo_o_negativo():
    try:
        # Solicitar al usuario que ingrese un número
        numero = float(input("Introduce un número: "))
        
        # Determinar si el número es positivo o negativo
        if numero > 0:
            print("Este número es positivo.")
        elif numero < 0:
            print("Este número es negativo.")
        else:
            print("El número es cero.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número válido.")

# Llamar a la función para ejecutar el programa
determinar_positivo_o_negativo()

