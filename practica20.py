#Hacer un algoritmo que se ingresa tres números. 
# Mostrar por pantalla si están ordenados de menor a mayor
def verificar_orden():
    try:
        # Solicitar al usuario que ingrese tres números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))
        
        # Verificar si los números están ordenados de menor a mayor
        if num1 <= num2 <= num3:
            print("Los números están ordenados de menor a mayor.")
        else:
            print("Los números no están ordenados de menor a mayor.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa números decimales.")

# Llamar a la función para ejecutar el programa
verificar_orden()
