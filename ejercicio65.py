#65. Escriba un programa que permita cargar por teclado un vector de 10 posiciones, 
# con números
#enteros, luego debe mostrar los números pero si el número termina en 
# 3 8 4 9 debe agregar
#un * antes de mostrar el número (investigue cómo obtener un ultimo digito de un número)

import array  # Importar el módulo array

# Crear un array vacío de enteros
valores = array.array('i')

# Bucle para cargar 10 valores desde el teclado
for i in range(10):  # Repetir 10 veces para ingresar 10 valores
    num = int(input(f"Ingrese el valor {i + 1}: "))  # Solicitar número al usuario y convertirlo a entero
    valores.append(num)  # Añadir el número ingresado al array

# Mostrar los números con modificaciones si es necesario
print("\nNúmeros modificados:")
for valor in valores:  # Iterar sobre los valores en el array
    ultimo_digito = valor % 10  # Calcular el último dígito del número (valor módulo 10)
    if ultimo_digito in [3, 8, 4, 9]:  # Verificar si el último dígito es 3, 8, 4 o 9
        print(f"*{valor}")  # Si es así, mostrar el valor con un '*' delante
    else:
        print(valor)  # Si no, mostrar el valor sin modificaciones
