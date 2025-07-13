#Parte 3: Ejercicio integrador (50 puntos)
#Ejercicio 5: Programa completo utilizando todo lo aprendido
#Desarrolla un programa que permita gestionar las ventas de una pequeña tienda. El programa
#debe tener las siguientes funcionalidades:
#1. Pedir al usuario que ingrese la cantidad de productos que desea registrar.
#2. Por cada producto, ingresar el nombre del producto y su precio.
#3. Al finalizar el registro de los productos, el programa debe:
# Calcular el total de la venta.
# Calcular el precio del producto más caro.
# Calcular el precio del producto más barato.
# Mostrar un listado con todos los productos ingresados y sus precios.
##Ejemplo de entrada esperada:
#¿Cuántos productos desea registrar?: 3
#Ingrese el nombre del producto 1: Pan
#Ingrese el precio del producto 1: 20
#Ingrese el nombre del producto 2: Leche
#Ingrese el precio del producto 2: 50
#Ingrese el nombre del producto 3: Arroz
#Ingrese el precio del producto 3: 30
#Ejemplo de salida esperada:
#Productos registrados:
#1. Pan: $20
#2. Leche: $50
#3. Arroz: $30
#Le pido al cliente la cantidad de productos a registrar en las listas
cantidad_producto = int(input("INGRESE LA CANTIDAD DE PRODUCTOS A REGISTRAR: "))
#creamos las listas correspondientes (vacias)
productos = []
precios = []
#cargo los productos con sus precios
for i in range (cantidad_producto):
    nombre_del_producto = input(f"ingrese nombre del producto {i + 1}: ")
    productos.append(nombre_del_producto)
    precio_del_producto = float(f"ingrese el precio del producto {i + 1}: ")
    precios.append(precio_del_producto) 
#calculamos el total de venta
#producto mas caro
#producto mas barato
#mostrar una lista de sus productos ingreados con sus precios
total_venta = 0
producto_caro = productos [0] #mouse
precio_caro = precios [0] #10.000$
producto_barato = productos [0] # mouse
precio_baratos = precios [0] #10.000
for i in range (len (precios)):
    total_venta = total_venta + precios[i]
    if precios [i] > precio_caro:
        precio_caro = precios [i]
        producto_caro = productos[i]
    elif precios [i] < precio_baratos:
        precio_baratos = precios[i]
        producto_barato = productos[i]
for indice, i in enumerate(productos):
    print(f"{indice +1}.{i}: {precios[i]}")
    print(f"el producto mas caro es el {producto_caro}, su precio es: {precio_caro}")
    print(f"el producto mas barato es el {producto_barato} y su precio es {producto_barato}")
    print(f"el total de ventas es: {total_venta}")





