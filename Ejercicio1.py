# Ejercicio 1 - "Caja del kiosco"

#Inizializamos las variables:
total_general= 0

# Solicitamos el nombre del cliente y lo validamos:
nombre_cliente= input("Ingrese el nombre del cliente: ")

while not nombre_cliente.isalpha():
    print("Error: debe ingresar el nombre y debe contener solo letras: ")
    nombre_cliente= input("Ingrese nuevamente el nombre del cliente: ")

# Solicitamos la cantidad de productos a comprar y lo validamos:
cantidad_productos= input("Ingrese la cantidad de productos a comprar: ")

while not cantidad_productos.isdigit() or int(cantidad_productos)==0:
    print("Error: La cantidad debe ser un numero entero positivo mayor a 0: ")
    cantidad_productos= input( "Ingrese nuevamente la cantidad de productos a comprar: ")

# Convertimos la cantidad en numero entero:
cantidad_productos= int(cantidad_productos)

# Lista para almacenar datos de cada producto: 
precios= []
tiene_descuento= []
precios_finales= []

# Por cada producto, pedimos precio y descuento:

for i in range(cantidad_productos):
    print(f"Producto: {i + 1}")

    #Validamos que el precio sea un numero entero positivo:
    precio= input(f"Ingrese el precio del producto: {i + 1}: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un numero entero positivo: ")
        precio= input(f"Ingrese nuevamente el precio del producto: {i + 1}: ")

    # Convertimos el precio en numero entero:
    precio= int(precio)
    precios.append(precio)

    # Validamos si tiene descuento (S/N):

    descuento= input("El producto seleccionado tiene descuento? (S/N): ")

    while descuento not in ['S', 's', 'N', 'n']:
        print("Error: Debe ingresar S o N")
        descuento= input("Ingrese nuevamente si el producto tiene descuento (S/N)")

    tiene_descuento.append(descuento)    

    # Aplicamos el 10% de descuento si corresponde:

    if descuento == 'S' or descuento == 's':
        precio_final= precio * 0.9 
        print(f"Entra al IF - precio con descuento: {precio_final}")
    else:
        precio_final= float(precio)
        print(f"Entra al ELSE - precio con descuento: {precio_final}")

    precios_finales.append(precio_final)


# Calculamos totales: 
total_sin_descuentos= sum(precios)
total_con_descuentos= sum(precios_finales)
ahorro= total_sin_descuentos - total_con_descuentos
promedio_por_producto= total_con_descuentos / cantidad_productos 

# Mostramos el resultado final:
print(f"{'-'*60}")
print(f"RESUMEN DE COMPRA")
print(f"{'-'*60}")
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"{'-'*60}")
print(f"DETALLE DE PRODUCTOS")
print(f"{'-'*60}")

for i in range(cantidad_productos):
    print(f"Producto {i + 1}: ")
    print(f"Precio: $ {precios[i]:.2f}")
    if tiene_descuento[i]=='S':
        print("Tiene descuento? SI, el 10% ")
        print(f"Precio con descuento: {precios_finales[i]:.2f}")
    else:
        print("Tiene descuento? NO" )
        print(f"Precio final: $ {precios_finales[i]:.2f}")
    print()

print(f"{'-'*60}")
print(f"TOTALES")
print(f"{'-'*60}")
print(f"Total sin descuentos: $ {total_sin_descuentos:.2f}")
print(f"Total con descuentos: $ {total_con_descuentos:.2f}")  
print(f"Ahorro total: $ {ahorro:.2f}")
print(f"Promedio por producto: $ {promedio_por_producto:.2f}") 
print(f"{'-'*60}")     

    







