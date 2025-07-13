#67. Escriba un programa que llene un vector de 200 posiciones con números 
# aleatorios entre 135
#y 762, debe separar los números impares de los pares,
#  por último muestre los 3 vectores, el
#original , los impares y los pares y la cantidad de elementos por vector
import random  # Importar random para generar números aleatorios
import array  # Importar el módulo array

# Crear un array de 200 números aleatorios entre 135 y 762
valores = array.array('i', [random.randint(135, 762) for _ in range(200)])

# Separar los números pares e impares
pares = array.array('i', [num for num in valores if num % 2 == 0])  # Crear un array de números pares
impares = array.array('i', [num for num in valores if num % 2 != 0])  # Crear un array de números impares

# Mostrar resultados
print("Array original:")
print(valores)  # Mostrar el array original
print(f"Cantidad de elementos: {len(valores)}")  # Mostrar la cantidad de elementos originales

print("\nArray de números pares:")
print(pares)  # Mostrar el array de números pares
print(f"Cantidad de elementos: {len(pares)}")  # Mostrar la cantidad de elementos pares

print("\nArray de números impares:")
print(impares)  # Mostrar el array de números impares
print(f"Cantidad de elementos: {len(impares)}")  # Mostrar la cantidad de elementos impares
