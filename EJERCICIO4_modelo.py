#Escribe un programa que le pida al usuario ingresar 5 nombres. Guarda los nombres en una
#lista y luego, utilizando un ciclo for, imprime cada nombre con su posición en la lista (usando
#enumerate)
#Entrada esperada:
#Ingrese el nombre 1: Ana
#Ingrese el nombre 2: Juan
#Ingrese el nombre 3: María
#Ingrese el nombre 4: Pedro
#Ingrese el nombre 5: Laura
###############################
#Salida esperada:
#1. Ana
#2. Juan
#3. María
#4. Pedro
#5. Laura
##############################
#creo una lista vacia
lista = []
#cargo la lista con nombres 
for i in range (5): #RECORRE DEL (0 AL 5)
    nombres = input("ingresa el nombre: ")
    lista.append (nombres)
#Enumero y muestro los nombres de la lista
#(p es el indice) (n es el contenido)
for p, n in enumerate(lista):
    print(f" {p + 1}. {n}")