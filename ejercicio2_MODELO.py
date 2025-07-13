#Escribe un programa que le pida al usuario ingresar su edad y muestre en pantalla uno de los
#siguientes mensajes, según la edad ingresada:
#• Si es menor de 18 años, imprimir: "Eres menor de edad."
#• Si tiene entre 18 y 65 años, imprimir: "Eres adulto."
#• Si tiene 65 años o más, imprimir: "Eres adulto mayor." 



#Pedir al usuario que ingrese su edad:
edad1 = int(input("Ingrese su edad:  "))
#CREA UNA CONDICION EN LA CUAL SI ES MENOR A  < 18 
if edad1 < 18:
    print("eres menor de edad")
#elif SINO QUE SEA MAYOR >18: 
elif edad1 >18:
    print("eres adulto")
else:
    print("eres un adulto mayor")

    
