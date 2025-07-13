#Escribir 
# un programa que pregunte al usuario por el número de horas trabajadas 
# y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.
def calcular_paga():
    try:
        # Solicitar al usuario que ingrese el número de horas trabajadas y el costo por hora
        horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
        costo_por_hora = float(input("Ingresa el costo por hora: "))
        
        # Calcular la paga total
        paga = horas_trabajadas * costo_por_hora
        
        # Mostrar el resultado
        print(f"La paga correspondiente es: {paga:.2f} pesos")
    
    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no numérico
        print("Entrada no válida. Por favor ingresa un número válido.")

# Llamar a la función para ejecutar el programa
calcular_paga()
