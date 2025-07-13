def verificar_contraseña(contraseña):
    cumple_longitud = len(contraseña) >= 8
    cumple_mayuscula = False
    cumple_minuscula = False
    cumple_numero = False
    cumple_especial = False

    for c in contraseña:
        if c.isupper():
            cumple_mayuscula = True
        elif c.islower():
            cumple_minuscula = True
        elif c.isdigit():
            cumple_numero = True
        elif c in "!@#$%":
            cumple_especial = True

        # Si ya todos los requisitos se cumplen, se puede salir del bucle
        if cumple_mayuscula and cumple_minuscula and cumple_numero and cumple_especial:
            break

    if cumple_longitud and cumple_mayuscula and cumple_minuscula and cumple_numero and cumple_especial:
        return "¡La contraseña es segura!"
    else:
        return "La contraseña no cumple con los requisitos de seguridad."

# Solicitar la contraseña al usuario
contraseña = input("Ingrese su contraseña: ")
print(verificar_contraseña(contraseña))
