#Hacer un algoritmo que permita ingresar tres números enteros y, 
# si el primero de ellos es negativo, calcular el producto de los tres, 
# en caso contrario calcular la suma de ellos.
def calcular_operacion():
    try:
        # Solicitar al usuario que ingrese tres números enteros
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))
        num3 = int(input("Ingresa el tercer número entero: "))
        
        # Verificar si el primer número es negativo
        if num1 < 0:
            # Calcular el producto de los tres números si num1 es negativo
            producto = num1 * num2 * num3
            print(f"El producto de los tres números es: {producto}")
        else:
            # Calcular la suma de los tres números si num1 no es negativo
            suma = num1 + num2 + num3
            print(f"La suma de los tres números es: {suma}")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no entero
        print("Entrada no válida. Por favor ingresa números enteros.")

# Llamar a la función para ejecutar el programa
calcular_operacion()
