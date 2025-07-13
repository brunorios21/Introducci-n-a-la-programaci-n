#Hacer un algoritmo que se ingresa el tiempo registrado de dos autos 
# que corrieron una carrera. El tiempo se guardó como número decimal. 
# Mostrar por pantalla cual llegó primero
def determinar_ganador():
    try:
        # Solicitar al usuario que ingrese los tiempos de los dos autos
        tiempo_auto1 = float(input("Ingresa el tiempo del primer auto: "))
        tiempo_auto2 = float(input("Ingresa el tiempo del segundo auto: "))
        
        # Determinar cuál auto llegó primero
        if tiempo_auto1 < tiempo_auto2:
            print("El primer auto llegó primero.")
        elif tiempo_auto2 < tiempo_auto1:
            print("El segundo auto llegó primero.")
        else:
            print("Ambos autos llegaron al mismo tiempo.")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa números decimales para los tiempos.")

# Llamar a la función para ejecutar el programa
determinar_ganador()

