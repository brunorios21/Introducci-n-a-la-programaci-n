#Estructuras colecciones vectores(arrays)
#63. Escriba un programa que contenga un vector de 10 posiciones con valores enteros mayores a
#1000 y menores a 2000, luego muestre los valores y sus posiciones.
# Ejercicio 63



#Programa que contiene un array de 10 posiciones con valores enteros mayores a 1000 y menores a 2000, 
# y muestra los valores y sus posiciones.

import array  # Importar el módulo array para trabajar con arreglos de tipo fijo

# Crear un array de enteros con valores predeterminados entre 1000 y 2000
valores = array.array('i', [1500, 1700, 1300, 1800, 1100, 1600, 1200, 1400, 1900, 1550])

print("Valores y sus posiciones:")  # Mostrar título para la salida
for i, valor in enumerate(valores):  # Recorrer el array con el índice (i) y valor (valor) usando enumerate
    print(f"Posición {i}: {valor}")  # Mostrar la posición y el valor correspondiente en el array



