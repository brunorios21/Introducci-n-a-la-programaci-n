#70. Escriba una función que devuelva el largo de un texto
#(cuántos caracteres tiene). luego utilice
#la función en un programa, que solicita se ingrese un texto, 
# palabra u oración y muestre por
#pantalla el largo.
# Función que devuelve el largo de un texto
def largo_texto(texto):
    return len(texto)  # Utilizamos la función integrada len() para contar los caracteres

# Programa principal
# Solicitamos un texto, palabra u oración al usuario
texto_usuario = input("Ingrese un texto, palabra u oración: ")

# Llamamos a la función largo_texto y almacenamos el resultado
largo = largo_texto(texto_usuario)

# Mostramos el largo del texto por pantalla
print(f"El texto ingresado tiene {largo} caracteres.")
