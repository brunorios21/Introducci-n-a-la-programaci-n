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

maximo = -1
numero = 0
while numero >= 0:
    numero = int(input("Ingrese un número positivo o un número negativo para salir: "))
    if numero > maximo:
        maximo = numero

if maximo != -1:
    print(f"El número máximo es: {maximo}")
else:
    print("No se ingresaron números positivos.")
