#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta 
# cero separados por comas.
def cuenta_atras():
    try:
        # Solicitar al usuario que ingrese un número entero positivo
        numero = int(input("Ingresa un número entero positivo: "))
        
        # Validar que el número ingresado sea positivo
        if numero <= 0:
            print("El número ingresado no es positivo.")
            return
        
        # Inicializar una lista para almacenar los números en la cuenta regresiva
        cuenta_regresiva = []
        
        # Generar la cuenta regresiva desde el número ingresado hasta 0 (inclusive)
        for i in range(numero, -1, -1):
            cuenta_regresiva.append(str(i))  # Agregar números como cadenas a la lista
        
        # Mostrar la cuenta regresiva separada por comas
        print(", ".join(cuenta_regresiva))
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no entero
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar el programa
cuenta_atras()
