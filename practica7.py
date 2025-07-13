#Hacer un programa en el que ingresas 
# un número que representa cierta cantidad de una fruta y divides esa cantidad por 3 chicos.
# Mostrar por pantalla el resultado
# Pedir al usuario su edad y mostrar si es mayor o no de edad
def dividir_frutas_entre_niños():
    cantidad_de_frutas= int(input("INGRESA LA CANTIDAD DE FRUTAS DISPONIBLES: "))
    cantidad_por_niño= cantidad_de_frutas / 3
    print(f"cada niño debe recibir: {cantidad_por_niño}")
dividir_frutas_entre_niños()
#comprobar si es mayor de edad!
def usuario_mostrar_su_edad():
    edad = int(input("INGRESAR TU EDAD: "))
    if edad >= 18:
        print(f"eres mayor de edad, buen provecho{edad}")
    else:
        print(f"eres menor de edad, sorry")
usuario_mostrar_su_edad()
