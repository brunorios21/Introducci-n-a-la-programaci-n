#73. Crear una función con dos parámetros, uno para un sting y otro para una letra.
#La función debe contar cuantas veces aparece la letra en el string, 
# debe devolver el resultado.
#Cree un programa que solicite al usuario 
# el texto y la letra a buscar (pase a mayúsculas) e
#invoque la función, muestre cuántas veces aparece la letra en el texto
# Función que cuenta cuántas veces aparece una letra en un texto
def contar_letra(texto,letra):
    contador = 0 #inicializamos el contador en 0
    for caracter in texto: # reco
        if caracter == letra:
            contador +=1
    return contador
#programa principal
#solicitar al usuario texto y la letra a buscar
texto_usuario = input("ingrese un texto: ")
letra_usuario = input("ingrese una letra para buscar: ")
#convertir el texto  y las letras en mayuscula
texto_usuario = texto_usuario.upper()
letra_usuario = texto_usuario.upper()

# Llamar a la función contar_letra y mostrar el resultado
cantidad = contar_letra(texto_usuario, letra_usuario)
print(f"La letra '{letra_usuario}' aparece {cantidad} veces en el texto.")

