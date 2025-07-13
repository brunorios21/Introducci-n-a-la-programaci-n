#Hacer un algoritmo que nos permita introducir un número, 
# luego muestre por pantalla el mensaje “Este número es par” o “este número es impar”

def determinar_par_o_impar():
    try:
        # Solicitar al usuario que ingrese un número
        numero = int(input("Introduce un número entero: "))
        
        # Determinar si el número es par o impar
        if numero % 2 == 0:
            print("Este número es par.")
        else:
            print("Este número es impar.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar el programa
determinar_par_o_impar()
