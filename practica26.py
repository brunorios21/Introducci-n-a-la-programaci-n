#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces. 
# (realizarlo con while y con for)z
def mostrar_palabra_10_veces_while():
    palabra = input("Ingresa una palabra: ")
    contador = 0
    
    while contador < 10:
        print(palabra)
        contador += 1

# Llamar a la función para ejecutar el programa
mostrar_palabra_10_veces_while()
