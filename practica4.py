#Hacer un programa que ingresas la edad de una persona 
# y calcula cuántos años va a tener dentro de 23 años.
# Mostrar el resultado por pantalla.
def calcular_edad_futura():
    edad_actual = int(input("ingresa tu edad actual: "))
    edad_futura = edad_actual + 23
    print(f"tu edad dentro de 23 años es de:{edad_futura} años")
calcular_edad_futura()