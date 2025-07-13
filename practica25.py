#Ingresar dos números 
#y mostrar el menor de ellos. 
# El ejercicio finaliza cuando se ingresan números iguales
def encontrar_menor():
    while True:
        try:
            # Solicitar al usuario que ingrese dos números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Verificar si los números ingresados son iguales
            if num1 == num2:
                print("Los números ingresados son iguales. El programa ha finalizado.")
                break  # Salir del bucle while
            
            # Determinar cuál número es el menor
            if num1 < num2:
                print(f"El número {num1} es menor que {num2}")
            else:
                print(f"El número {num2} es menor que {num1}")
        
        except ValueError:
            # Manejar el caso en que el usuario ingrese un valor no numérico
            print("Entrada no válida. Por favor ingresa números.")

# Llamar a la función para ejecutar el programa
encontrar_menor()
