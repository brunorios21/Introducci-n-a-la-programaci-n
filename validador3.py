def validadar_contraseña(contraseña):
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
        elif c in "#$%!=":
            cumple_especial = True
        if cumple_mayuscula and cumple_minuscula and cumple_numero and cumple_especial:
            break
    if cumple_longitud and cumple_mayuscula and cumple_minuscula and cumple_numero and cumple_especial:
        return "la contaseña es segura"
    else:
        return "la contraseña no es segura"
contraseña = input("INGRESAR CONTRASEÑA")
print(validadar_contraseña(contraseña))