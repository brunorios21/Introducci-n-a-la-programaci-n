#64. Escriba un programa que cargue un vector desde el número 100 al 200,
#debe utilizar 2 métodos
#de carga,usando range y otro utilizando while, 
# luego muestre los valores uno al lado del otro.
import array  # Importar el módulo array

# Método 1: Usar range para cargar un array de enteros desde 100 a 200
valores_range = array.array('i', range(100, 201))  # Crear un array usando range del 100 al 200 (inclusive)

# Método 2: Usar while para cargar manualmente el array
valores_while = array.array('i')  # Inicializar un array vacío
num = 100  # Inicializar la variable num en 100
while num <= 200:  # Bucle que corre mientras num sea menor o igual a 200
    valores_while.append(num)  # Añadir el valor actual de num al array
    num += 1  # Incrementar num en 1

# Mostrar valores cargados con range
print("Valores usando range:")
print(valores_range)  # Imprimir array generado por range

# Mostrar valores cargados con while
print("\nValores usando while:")
print(valores_while)  # Imprimir array generado por while


