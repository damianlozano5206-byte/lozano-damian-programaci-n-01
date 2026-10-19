##Damian Emiliano Lozano Pozos## ##222452061##
##Es un programa de consola en python que simula una caja registradora de una tienda de comics y mangas. Primero pregunta cuántos productos se van a comparar y valida que la respuesta sea un numero mayor a 0. Despues por cada producto pide el nombre, precio y la cantidad, verificando que el precio y la cantidad sean validos y posítivos. Después, con los números calculados se calcula el subtotal mas un IVA del 16% y muestra el total a pagra para al final mostrar un recibo donde aoarecen los productos, precios, cantidades y subtotales, junto al desgloce de los montos, todo con decimales.

#================================================
#RECIBO DE COMPRA -     Tienda de Comics y Mangas
#================================================

print("===Bienvenido a la tienda de comics y mangas===")

#---------- CAPTURA DE DATOS: cantidad de productos ----------
cantidad_productos = input("¿Cuántos productos va a registrar? ")

# Validamos con isdigit() que la cantidad de productos sea un número entero positivo
while not cantidad_productos.isdigit() or int(cantidad_productos) == 0:
    print("Error: Debe ingresar un número entero positivo mayor a 0.")
    cantidad_productos = input("¿Cuántos productos va a registrar? ")

cantidad_productos = int(cantidad_productos)

#Lista para guardar los datos de cada producto
lista_nombres = []
lista_precios = [] 
lista_cantidades = []
lista_subtotales = []

#variable para ir sumando el subtotal general
subtotal_general = 0

# ---------- CAPTURA DE DATOS: ciclo por cada producto ----------
for i in range(cantidad_productos):
    print(f"\n--- Producto {i + 1} ---")

    nombre_producto = input("Nombre del producto (ej. Black Clover Tomo 1): ")

# ---------- VALIDACIÓN DEL PRECIO ----------
precio_valido = False
while not precio_valido:
    cantidad_precio = input("Precio del producto (ej. 150.00): ")
    try:
        precio_producto = float(cantidad_precio)  # intentamos convertir a float
        if precio_producto > 0:
            precio_valido = True
        else:
            print("Error: el precio debe ser mayor a 0.")
    except ValueError:
        print("Error: escribe un número válido para el precio.")

# ---------- CÁLCULO: subtotal de cada producto ----------
subtotal_producto = precio_producto * cantidad_productos

#Guardamos todos los datos en las listas correspondientes
lista_nombres.append(nombre_producto)
lista_precios.append(precio_producto)
lista_cantidades.append(cantidad_productos)
lista_subtotales.append(subtotal_producto)

#sumamos al subtotal general
subtotal_general = subtotal_general + subtotal_producto

# ---------- CÁLCULOS: IVA y total ----------
iva = subtotal_general * 0.16
total = subtotal_general + iva

# ---------- IMPRESIÓN DEL RECIBO ----------
print("\n")
print("=" * 55)
print("        TIENDA DE COMICS Y MANGAS")
print("              RECIBO DE COMPRA")
print("=" * 55)
print(f"{'Producto':<20}{'Precio':>10}{'Cant.':>8}{'Subtotal':>12}")
print("-" * 55)

# Recorremos las listas para imprimir cada producto
for i in range(cantidad_productos):
    print(f"{lista_nombres[i]:<20}{lista_precios[i]:>10.2f}{lista_cantidades[i]:>8}{lista_subtotales[i]:>12.2f}")

print("-" * 55)
print(f"{'Subtotal:':<38}${subtotal_general:>10.2f}")
print(f"{'IVA (16%):':<38}${iva:>10.2f}")
print(f"{'TOTAL A PAGAR:':<38}${total:>10.2f}")
print("=" * 55)
print("   ¡Gracias por tu compra, vuelve pronto!")
print("=" * 55)
