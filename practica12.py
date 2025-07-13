#Hacer un algoritmo que ingrese dos números y determinar 
# si alguno de los dos números es divisible por 3.
def determinar_divisibilidad_por_3():
    try:
        # Solicitar al usuario que ingrese dos números
        numero1 = int(input("Ingresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
        
        # Determinar si alguno de los dos números es divisible por 3
        if numero1 % 3 == 0 or numero2 % 3 == 0:
            print("Al menos uno de los dos números es divisible por 3.")
        else:
            print("Ninguno de los dos números es divisible por 3.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa números enteros.")

# Llamar a la función para ejecutar el programa
determinar_divisibilidad_por_3()
