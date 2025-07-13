#Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas el nombre 
# del usuario tantas veces como el número introducido.
def imprimir_nombre_repeticiones():
    try:
        # Solicitar al usuario que ingrese su nombre
        nombre = input("Ingresa tu nombre: ")
        
        # Solicitar al usuario que ingrese un número entero
        repeticiones = int(input("Ingresa un número entero: "))
        
        # Imprimir el nombre del usuario tantas veces como repeticiones
        for _ in range(repeticiones):
            print(nombre)
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no entero
        print("Entrada no válida. Por favor ingresa un número entero para las repeticiones.")

# Llamar a la función para ejecutar el programa
imprimir_nombre_repeticiones()
