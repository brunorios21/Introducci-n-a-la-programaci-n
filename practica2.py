def mi_calculadora():
    numero1= float(input("INGRESA EL PRIMER NUMERO QUE DESEAS CALCULAR: "))
    numero2= float(input("INGRESA EL SEGUNDO NUMERO QUE DESEAS CALCULAR: "))
    suma= numero1 + numero2
    resta= numero1 - numero2
    multiplicacion= numero1 * numero2
    if 2 !=0:
        division= numero1 / numero2
    else:
        print(f"no se puede dividir por 0")
    print(f"resultado de suma: {suma}")
    print(f"resultado de resta: {resta}")
    print(f"resultado de multiplicacion: {multiplicacion}")
    print(f"resultado de division: {division}")
mi_calculadora()
