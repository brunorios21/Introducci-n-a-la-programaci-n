#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número 
# separados por comas.
def mostrar_impares_hasta_numero():
    try:
        # Solicitar al usuario que ingrese un número entero positivo
        numero = int(input("Ingresa un número entero positivo: "))
        
        # Validar que el número ingresado sea positivo
        if numero <= 0:
            print("El número ingresado no es positivo.")
            return
        
        # Inicializar una lista para almacenar los números impares
        impares = []
        
        # Iterar desde 1 hasta el número ingresado (inclusive)
        for i in range(1, numero + 1, 2):
            impares.append(str(i))  # Agregar números impares como cadenas a la lista
        
        # Mostrar los números impares separados por comas
        print(", ".join(impares))
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no entero
        print("Entrada no válida. Por favor ingresa un número entero.")

# Llamar a la función para ejecutar el programa
mostrar_impares_hasta_numero()
