#72. Escriba una función para cargar un vector con n cantidad
#de elementos con valores 0 y 1 correlativamente , luego debe retornar el vector. 
# Para probar la función escriba un programa que solicite al 
# usuario la cantidad de elementos para el vector este número debe ser
#  entero positivo, Utilice la función integrada de python .isnumeric() 
# para verificar, ejemplo: mi_numero.isnumeric() devuelve True o False, 
# si es correcto debe llamar a la función y devolver el vector con los elementos 
# pedidos y luego debe mostrar los elementos del vector uno debajo del otro por
#  pantalla pero si es incorrecto debe volver a solicitar un nuevo número antes
#  avise que hubo un error EN PYTHON
def cargar_vector(n):
    # Creamos el vector con valores alternados de 0 y 1
    vector = []  # Inicializamos una lista vacía para almacenar el vector
    for i in range(n):  # Recorremos un rango desde 0 hasta n-1
        vector.append(i % 2)  # Alternamos entre 0 y 1 usando el operador módulo (%)
    return vector  # Retornamos el vector una vez que se ha llenado

def solicitar_numero():
    # Esta función solicita un número entero positivo al usuario y lo valida
    while True:  # Ciclo infinito que se repetirá hasta que el usuario ingrese un valor válido
        mi_numero = input("Ingrese un número entero positivo para el tamaño del vector: ")
        # Verificamos que lo ingresado sea numérico y mayor que 0
        if mi_numero.isnumeric() and int(mi_numero) > 0:
            return int(mi_numero)  # Si la entrada es válida, retornamos el número convertido a entero
        else:
            # Si la entrada no es válida, mostramos un mensaje de error
            print("Error: Debe ingresar un número entero positivo. Intente de nuevo.")

# Programa principal
n = solicitar_numero()  # Llamamos a la función para solicitar y validar el número de elementos
vector = cargar_vector(n)  # Llamamos a la función cargar_vector para crear el vector

# Mostramos el vector generado, un ele
