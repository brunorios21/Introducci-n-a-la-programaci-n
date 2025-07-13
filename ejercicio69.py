#69. Escriba un programa que utilice una función propia para calcular
# el cuadrado de un número
#ingresado por teclado, no debe utilizar **,
# esta función retorna el resultado que debe ser
#mostrado por pantalla.
# Función para calcular el cuadrado de un número
def calcular_cuadrado(numero):
    return numero * numero  # Multiplicamos el número por sí mismo

# Programa principal
# Solicitamos un número al usuario
numero_usuario = int(input("Ingrese un número para calcular su cuadrado: "))

# Llamamos a la función calcular_cuadrado y almacenamos el resultado
resultado = calcular_cuadrado(numero_usuario)

# Mostramos el resultado por pantalla
print(f"El cuadrado de {numero_usuario} es {resultado}.")
#Explicación:
#calcular_cuadrado(numero):
#Esta función recibe un número como parámetro y retorna el 
#resultado de multiplicar ese número por sí mismo 
#(lo que equivale a elevarlo al cuadrado).
#Programa principal:
#Se solicita al usuario que ingrese un número utilizando input(). 
# El valor ingresado se convierte a entero con int().
#Luego, se llama a la función calcular_cuadrado con el número ingresado 
# y se almacena el resultado.
#Finalmente, el resultado se muestra por pantalla con un mensaje 
# formateado usando una f-string (f"...").


