#Diseñar un algoritmo que calcule la longitud de la circunferencia y 
# el área del círculo. 
# Considerar que por pantalla se ingresa el radio de dicha circunferencia.


import math

def calcular_circunferencia_y_area():
    try:
        # Solicitar al usuario que ingrese el radio del círculo
        radio = float(input("Ingresa el radio del círculo: "))
        
        # Calcular la longitud de la circunferencia (2 * pi * radio)
        longitud_circunferencia = 2 * math.pi * radio
        
        # Calcular el área del círculo (pi * radio^2)
        area_circulo = math.pi * radio**2
        
        # Mostrar los resultados por pantalla
        print(f"La longitud de la circunferencia es: {longitud_circunferencia}")
        print(f"El área del círculo es: {area_circulo}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número para el radio.")

# Llamar a la función para ejecutar el programa
calcular_circunferencia_y_area()

