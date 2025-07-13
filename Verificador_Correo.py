#El programa debe realizar lo siguiente:
    #Solicitar al usuario que ingrese una dirección de correo electrónico.
    #Utilizar una estructura de decisión "if" para verificar si la cadena cumple con los siguientes requisitos para ser considerada una dirección de correo electrónico válida:
        #Debe contener un solo símbolo '@'.
        #Debe contener al menos un carácter antes del '@'.
        #Debe contener al menos un carácter después del '@'.
        #Debe tener una extensión de dominio válida, como '.com'.
    #Imprimir un mensaje que indique si la cadena ingresada es una dirección de correo electrónico válida o no.
    #Utilizar funciones de entrada y salida como input() y print().

# Solicitar al usuario que ingrese una dirección de correo electrónico
direccion_correo = input("Ingrese una dirección de correo electrónico: ")

un_caracter = False
arroba = False
otro_caracter = False
punto = False
c = False
o = False
m = False
ultimo_caracter= ""
for x in direccion_correo :
    if (x.isupper() or x.islower()) and not(un_caracter):
        un_caracter = True

    if (un_caracter and x == '@'):
        arroba = True

    if (un_caracter and arroba and (x.isupper() or x.islower())):
        otro_caracter = True
    
    if (un_caracter and arroba and otro_caracter and x == '.'):
        punto = True

    if (un_caracter and arroba and otro_caracter and punto and ultimo_caracter == '.' and x == 'c' ):
        c = True

    if (un_caracter and arroba and otro_caracter and punto and c and ultimo_caracter == 'c' and x == 'o' ):
        o = True

    if (un_caracter and arroba and otro_caracter and punto and o and ultimo_caracter == 'o' and x == 'm' ):
        m = True

    ultimo_caracter = x

if(un_caracter and arroba and otro_caracter and punto and o and m):
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida.")