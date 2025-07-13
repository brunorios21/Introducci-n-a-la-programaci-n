# Parte 3: Ejercicio integrador (50 puntos)
# Ejercicio 5: Programa completo utilizando todo lo aprendido

# Solicitar la cantidad de productos a registrar
cantidad_producto = int(input("¿Cuántos productos desea registrar?: "))

# Crear listas vacías para almacenar los productos y precios
productos = []
precios = []

# Ingresar los productos y sus precios
for i in range(cantidad_producto):
    nombre_del_producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    productos.append(nombre_del_producto)
    
    # Aquí se corrige la forma de pedir el precio
    precio_del_producto = float(input(f"Ingrese el precio del producto {i + 1}: "))
    precios.append(precio_del_producto)

# Inicializar variables para el cálculo
total_venta = 0
producto_caro = productos[0]
precio_caro = precios[0]
producto_barato = productos[0]
precio_barato = precios[0]

# Calcular total de ventas, producto más caro y más barato
for i in range(len(precios)):
    total_venta += precios[i]
    if precios[i] > precio_caro:
        precio_caro = precios[i]
        producto_caro = productos[i]
    if precios[i] < precio_barato:
        precio_barato = precios[i]
        producto_barato = productos[i]

# Mostrar los productos registrados con sus precios
print("\nProductos registrados:")
for indice, nombre in enumerate(productos):
    print(f"{indice + 1}. {nombre}: ${precios[indice]}")

# Mostrar el producto más caro y más barato
print(f"\nEl producto más caro es {producto_caro} y su precio es: ${precio_caro}")
print(f"El producto más barato es {producto_barato} y su precio es: ${precio_barato}")
print(f"El total de ventas es: ${total_venta}")
