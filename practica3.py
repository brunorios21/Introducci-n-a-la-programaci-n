#############Hacer un programa en el que se ingresa un número entero ################
#########y por pantalla informa el doble de ese número.#############

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#el try y except se utilizan para manejar excepciones en Python. 
# En este caso, sirven para capturar cualquier error que ocurra al intentar convertir 
# la entrada del usuario en un número entero. 
# Si el usuario ingresa algo que no puede convertirse a un entero (como un texto), 
# se generará una excepción ValueError.
#Aquí tienes el código con anotaciones:
def calcular_doble():
        # Intentamos obtener un número entero del usuario
        numero = int(input("Ingresa un número entero: "))
        doble = numero * 2
        # Mostramos el resultado
        print(f"El doble de {numero} es {doble}.")
# Llamamos a la función para ejecutar el programa
calcular_doble()
