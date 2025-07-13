# Declaro mi variable alumnos igual a 40
alumnos = 40

# Imprimir en consola la cantidad de alumnos
print("Cantidad de alumnos")
print(alumnos)

# Declaro mi variable de asistencias, ingresando el valor de asistencias por consola
asistieron_a_clases = int(input("INGRESE EL VALOR DE CUANTOS ALUMNOS ASISTIERON A CLASES: "))

# Imprimir en consola la cantidad de asistencias
print("Cantidad de asistencias")
print(asistieron_a_clases)

# Controlo que la cantidad de alumnos sea igual a la cantidad que asistieron
if alumnos == asistieron_a_clases:
  # Si asistieron todos imprimo en pantalla un mensaje
  print("Asistieron todos")
else:
  # Si no asistieron todos imprimo en pantalla otro mensaje
  print("No asistieron todos")

# Genero un listado de 0 al 25, itero (recorro) cada alumno
for alumno in range(asistieron_a_clases):
  # Imprime un saludo para cada uno
  print("Hola alumno", alumno)