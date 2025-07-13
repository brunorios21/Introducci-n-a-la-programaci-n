#66. Escriba un programa que llene un vector de 100 posiciones con números aleatorios entre 1990
#y 2022,muestre los elementos del vector y su cantidad de elementos , 
# luego debe eliminar los
#números terminados en 5, 8, 4 ,0 ,por último vuelva a mostrar el vector. 
# y su cantidad de
#elementos.
import random  # Importar random para generar números aleatorios
import array  # Importar el módulo array

# Crear un array con 100 números aleatorios entre 1990 y 2022
valores = array.array('i', [random.randint(1990, 2022) for _ in range(100)])  # Usar list comprehension para generar 100 valores aleatorios

print("Valores originales:")
print(valores)  # Mostrar el array original
print(f"Cantidad de elementos: {len(valores)}")  # Mostrar la cantidad de elementos originales

# Filtrar y eliminar valores que terminan en 5, 8, 4 o 0
valores_filtrados = array.array('i', [num for num in valores if num % 10 not in [5, 8, 4, 0]])  # Crear un nuevo array sin los números cuyos últimos dígitos sean 5, 8, 4 o 0

print("\nValores después de eliminar los terminados en 5, 8, 4, 0:")
print(valores_filtrados)  # Mostrar el array filtrado
print(f"Cantidad de elementos: {len(valores_filtrados)}")  # Mostrar la cantidad de elementos después del filtro
