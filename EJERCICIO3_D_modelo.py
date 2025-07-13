#Escribe un programa que le pida al usuario ingresar números enteros. El programa debe
#calcular el máximo de todos los números ingresados. El proceso terminará cuando el usuario
#ingrese un número negativo. Finalmente, el programa debe imprimir el número máximo
#ingresado.
#Entrada esperada:
#Ingrese un número (o un número negativo para salir): 5
#Ingrese un número (o un número negativo para salir): 10
#Ingrese un número (o un número negativo para salir): 2
#Ingrese un número (o un número negativo para salir): -1 
#Salida esperada:
#El número máximo ingresado es: 10 
numero = int(input("Ingrese numero entero positivo o negativo para salir: "))
maximo = numero
while numero >= 0:
    if numero > maximo:
        maximo = numero
    numero = int(input("ingrese un nuevo numero positivo o negativo para salir: "))

print(f"el maximo es: {maximo}")

