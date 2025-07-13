# Programa que gestiona ventas de una tienda

# Inicialización de variables
productos = []
precios = []

# Solicitar la cantidad de productos
cantidad_productos = int(input("¿Cuántos productos desea registrar?: "))

# Registrar cada producto con su precio
for i in range(cantidad_productos):
    nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
    precio_producto = float(input(f"Ingrese el precio del producto {i+1}: "))
    
    productos.append(nombre_producto)
    precios.append(precio_producto)

# Calcular el total de la venta
total_venta = sum(precios)

# Calcular el precio del producto más caro y más barato
precio_maximo = max(precios)
precio_minimo = min(precios)

# Mostrar el listado de productos con sus precios
print("\nProductos registrados:")
for i in range(cantidad_productos):
    print(f"{i+1}. {productos[i]}: ${precios[i]}")

# Mostrar el total de la venta, el producto más caro y el más barato
print(f"\nTotal de la venta: ${total_venta}")
print(f"El producto más caro cuesta: ${precio_maximo}")
print(f"El producto más barato cuesta: ${precio_minimo}")
