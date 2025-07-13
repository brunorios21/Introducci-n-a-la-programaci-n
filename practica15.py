#Un señor tiene 10 pares de zapatillas,
#  esa cantidad la ingresa a su computadora, 
# en el momento del ingreso le llegan 5 pares más, 
# que debe ingresar también en la computadora.
#  Mostrar por pantalla cuantas zapatillas tiene en total

def calcular_total_zapatillas():
    # Definir la cantidad inicial de pares de zapatillas
    cantidad_inicial = 10
    
    # Sumar la cantidad adicional de pares que recibe
    cantidad_adicional = 5
    total_zapatillas = cantidad_inicial + cantidad_adicional
    
    # Mostrar por pantalla el total de pares de zapatillas
    print(f"El señor tiene en total {total_zapatillas} pares de zapatillas.")

# Llamar a la función para ejecutar el programa
calcular_total_zapatillas()
