#71. Escriba un programa que utilice tres funciones, 
# que dada una secuencia numérica (lista,
#tupla, vector) debe:
#a. Encontrar el mayor de los valores
#b. Calcular el promedio
#c. Encontrar el valor más bajo
#El programa debe mostrar los tres resultados por pantalla.
# Función para encontrar el mayor valor
def encontrar_mayor(secuencia):
    return max(secuencia)  # Usamos la función integrada max() para encontrar el valor máximo

# Función para calcular el promedio
def calcular_promedio(secuencia):
    return sum(secuencia) / len(secuencia)  # Sumamos todos los valores y dividimos por la cantidad de elementos

# Función para encontrar el valor más bajo
def encontrar_menor(secuencia):
    return min(secuencia)  # Usamos la función integrada min() para encontrar el valor mínimo

# Programa principal
# Definimos la secuencia numérica (puede ser una lista, tupla, etc.)
secuencia = [12, 45, 67, 23, 89, 34, 22]  # Ejemplo de lista numérica

# Llamamos a las funciones para obtener los resultados
mayor = encontrar_mayor(secuencia)
promedio = calcular_promedio(secuencia)
menor = encontrar_menor(secuencia)

# Mostramos los resultados por pantalla
print(f"El valor mayor es: {mayor}")
print(f"El promedio es: {promedio:.2f}")  # Mostramos el promedio con 2 decimales
print(f"El valor más bajo es: {menor}")

 
 