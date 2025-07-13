#Hacer un algoritmo que ingresa 2 letras, 
# mostrarlas por pantalla ordenadas alfabéticamente.
def mostrar_letras_ordenadas():
    try:
        # Solicitar al usuario que ingrese dos letras
        letra1 = input("Ingresa la primera letra: ")
        letra2 = input("Ingresa la segunda letra: ")
        
        # Ordenar las letras alfabéticamente
        letras_ordenadas = sorted([letra1, letra2])
        
        # Mostrar las letras ordenadas por pantalla
        print(f"Las letras ordenadas alfabéticamente son: {letras_ordenadas[0]} {letras_ordenadas[1]}")
    
    except:
        # Manejar cualquier tipo de excepción que pueda ocurrir
        print("Ha ocurrido un error.")

# Llamar a la función para ejecutar el programa
mostrar_letras_ordenadas()
