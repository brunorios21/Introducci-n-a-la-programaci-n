#68. Ejercicio tipo parcial.
#Escriba un programa que simule ser un sorteo al azar con 58 participantes.
#Tenemos sus números de DNI, los participantes tienen números de dni entre 43158258 y
#44200952, no puede haber participantes repetidos, una vez cargados los dni, debe seleccionar
#3 ganadores al azar, no se pueden repetir los ganadores, muestre el listado de participantes,
#muestre el número de dni de los ganadores
#Utilice random y sus métodos.
import random  # Importar random para la selección aleatoria
import array  # Importar el módulo array

# Crear un array con 58 DNIs únicos aleatorios entre 43158258 y 44200952
dni_participantes = array.array('i', random.sample(range(43158258, 44200953), 58))  # random.sample garantiza que no haya repeticiones

print("Listado de participantes:")
for i, dni in enumerate(dni_participantes):  # Usar enumerate para obtener el índice y el valor (DNI)
    print(f"Participante {i + 1}: DNI {dni}")  # Mostrar el número de participante y su DNI

# Seleccionar 3 ganadores al azar sin repetición
ganadores = random.sample(dni_participantes, 3)  # Seleccionar 3 ganadores únicos del array

# Mostrar los ganadores
print("\nGanadores del sorteo:")
for i, ganador in enumerate(ganadores):  # Recorrer los ganadores seleccionados
    print(f"Ganador {i + 1}: DNI {ganador}")  # Mostrar el número del ganador y su DNI

#random.sample(range(...), 58): Selecciona 58 DNIs únicos dentro del rango dado.
#random.sample(dni_participantes, 3): Selecciona 3 ganadores sin repetición.
#enumerate(dni_participantes): Itera sobre el array de DNIs con sus posiciones.
