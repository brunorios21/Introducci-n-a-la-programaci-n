# INICIALIZAR FUNCION (verificar_contraseña)
def verificar_contraseña(contraseña):
    # Verificamos si la longitud de la contraseña es al menos 8 caracteres y almacenamos el resultado (True o False)
    cumple_longitud = len(contraseña) >= 8  
    
    # Inicializamos estas variables como False
    cumple_mayuscula = False 
    cumple_minuscula = False
    cumple_numero = False
    cumple_especial = False  # Ya que inicialmente asumimos que la contraseña no cumple con estos requisitos

    # Paso 3: Iterar sobre cada carácter de la contraseña
    for c in contraseña:
        # Paso 4: Verificar cada carácter
        if c.isupper():  # Verifica si el carácter es una letra mayúscula
            cumple_mayuscula = True
        elif c.islower():  # Verifica si el carácter es una letra minúscula
            cumple_minuscula = True
        elif c.isdigit():  # Verifica si el carácter es un dígito
            cumple_numero = True
        elif c in "!@#$%":  # Verifica si el carácter es uno de los caracteres especiales !@#$%
            cumple_especial = True

        # Si ya todos los requisitos se cumplen, se puede salir del bucle
        if cumple_mayuscula and cumple_minuscula and cumple_numero and cumple_especial:
            break

    # Verificar si la contraseña es segura
    if cumple_longitud and cumple_mayuscula and cumple_minuscula and cumple_numero and cumple_especial:
        return "¡LA CONTRASEÑA ES SEGURA!"
    else:
        return "¡LA CONTRASEÑA NO ES SEGURA!"

# SOLICITAR AL USUARIO QUE INGRESE LA CONTRASEÑA
contraseña = input("INGRESAR CONTRASEÑA: ")
print(verificar_contraseña(contraseña))

    

    