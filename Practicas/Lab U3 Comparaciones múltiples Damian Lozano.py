## Lab U3 Comparaciones múltiples

##Clasificación por edad
edad = int(input("Ingrese la edad de la persona: "))

if edad < 13:
    print("Clasificación: Niño")
elif edad <= 17:
    print("Clasificación: Adolescente")
else:
    print("Clasificación: Adulto")

# el programa pide la edad y la convierte a entero con int(). Luego usa una cadena if / elif / else: si la edad es menor de 13 es "niño";
# si no, y es menor o igual a 17, es "adolescente"; en cualquier otro caso (18 o más) es "adulto". Como las condiciones se evalúan en orden, el elif no necesita revisar que la edad sea mayor o igual a 13.

## Validar acceso (usuario y contraseña)
usuario_correcto = "admin"
contrasena_correcta = "contraseña"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido")
elif usuario == usuario_correcto and contrasena != contrasena_correcta:
    print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")

# el programa guarda un usuario y una contraseña correctos en dos variables y luego pide al usuario que escriba los suyos. La estructura
# if / elif / else cubre los tres casos: primero revisa si ambos datoscoinciden (acceso concedido); si no, revisa solo el usuario, lo que
# significa que la contraseña es la que falló (contraseña incorrecta); y sini el usuario coincide, se imprime "usuario no encontrado".

## Calculadora de envío
peso = float(input("Ingrese el peso del paquete en kg: "))
if peso <= 1:
    costo_envio = 50
elif peso <= 5:
    costo_envio = 90
else:
    costo_envio = 150

#descuento del 10% si el paquete pesa más de 10 kg
if peso > 10:
    costo_envio *= 0.9  # Aplica un descuento del 10%
    print("Se aplicó un descuento del 10% por peso mayor a 10 kg.")

print(f"El costo de envío es: ${costo_envio:.2f}")

# el programa pide el peso como número decimal con float() y usa una cadena if / elif / else para asignar el costo base: $50 hasta 1 kg,
# $90 hasta 5 kg y $150 para más de 5 kg. Después, un if independiente revisa si el peso supera los 10 kg; en ese caso multiplica el costo por
# 0.90 (equivale a restar el 10%). Finalmente imprime el costo con dos decimales.

##clasificación la temperatura
temperatura = float(input("Ingrese la temperatura del refrigerante en grados Celsius: "))

if temperatura < 10:
    print("Clasificación: frío")
elif temperatura <= 25:
    print("Clasificación: templado")
else:
    print("Clasificación: caliente")

# el programa pide la temperatura como número decimal con float() para aceptar valores como 24.5. 
# Luego usa una cadena if / elif / else: si la temperatura es menor a 10 es "frío"; si no, y es menor a 25, es
# "templado" (cubre de 10 a 24.9); en cualquier otro caso (25 o más) es "calor".

##Ejercicio :Calificación con letras
clasificacion = float(input("Ingrese la calificación numérica (0-100): "))
if clasificacion >= 90:
    print("Calificación: A")
elif clasificacion >= 80:
    print("Calificación: B")
elif clasificacion >= 70:
    print("Calificación: C")
else:
    print("Calificación: D")

# el programa pide la calificación como número decimal con float() y usa una cadena if / elif / else de cinco ramas. Las comparaciones van de
# mayor a menor: primero se revisa si es 90 o más (A); si no, se revisa si es 80 o más (B), y así sucesivamente hasta 60 (D). Todo lo que no cumple
# ninguna condición anterior (menos de 60) cae en el else y recibe una F.

## Ejercicio: Descuento por monto de compra
monto_compra = float(input("Ingrese el monto de la compra: $"))

if monto_compra > 500:
    descuento = 20
elif monto_compra > 200:
    descuento = 10
else:
    descuento = 0

monto_final = monto_compra - (monto_compra * descuento / 100)

print(f"Descuento aplicado: {descuento}%")
print(f"Monto final a pagar: ${monto_final:.2f}")

# el programa pide el monto como número decimal con float() y usa una cadena if / elif / else para asignar el porcentaje de descuento. Se
# revisa primero la condición más alta (más de $500 → 20%); si no se cumple, se revisa si es más de $200 (10%); en cualquier otro caso el descuento es
# 0%. Después calcula el monto final restando el descuento (monto * descuento / 100) e imprime tanto el porcentaje como el total a pagar.

##Ejercicio :Validar un rango con comparación encadenada
numero = float(input("Ingrese un número: "))

if 1 <= numero <= 100:
    print("El número etá en el rango (entre 1 y 100).")
else:
    print("El número no está en el rango (entre 1 y 100).")

# el programa pide un número con float() para aceptar también
# decimales. La condición 1 <= numero <= 100 es una comparación encadenada:Python la interpreta como (1 <= numero) and (numero <= 100), pero de forma
# más corta y legible. Si ambas partes son verdaderas, el número está en
#  rango; de lo contrario, el else imprime que no lo está. Al usar <= en ambos extremos, los valores 1 y 100 se consideran dentro del rango.

# Clasificar el IMC
peso = float(input("ingresa el peso en kg: "))
estatura = float(input("ingresa la estatura en metros: "))

#se calcula el IMC antes de clacificarlo
imc = peso / estatura ** 2

print(f"Tu IMC es: {imc:.1f}")

if imc < 18.5:
    print("Clasificación: bajo peso")
elif imc < 25:
    print("Clasificación: normal")
elif imc < 30:
    print("Clasificación: sobrepeso")
else:
    print("Clasificación: obesidad")

# el programa pide el peso y la estatura como números decimales con float() y calcula el IMC con la fórmula peso / estatura ** 2 antes de
# clasificarlo. Luego usa una cadena if / elif / else de cuatro ramas, de
# menor a mayor: menos de 18.5 es "bajo peso"; si no, menos de 25 es "normal"; si no, menos de 30 es "sobrepeso"; y 30 o más cae en el else como "obesidad".

##Ejercicio Tarifas de electricidad
consumo = float(input("Ingresa el consumo mensual en kWh: "))

if consumo <= 150:
    costo = consumo * 1.20
elif consumo <= 300:
    costo = 150 * 1.20 + (consumo - 150) * 1.80
else:
    costo = 150 * 1.20 + 150 * 1.80 + (consumo - 300) * 2.50

print(f"Consumo: {consumo} kWh")
print(f"Costo total: ${costo}")

# el programa pide el consumo en kWh con float() y usa una cadena if / elif / else para identificar el tramo. Si el consumo es de
# hasta 150 kWh, todo se cobra a $1.20. Si es de hasta 300, los primeros 150 kWh se cobran a $1.20 y el excedente (consumo - 150) a $1.80. Si es mayor
# a 300, se suman los primeros 150 a $1.20, los siguientes 150 a $1.80 y el
# resto (consumo - 300) a $2.50. Cada tramo solo cobra la parte del consumo que cae dentro de él, por eso se suman los costos de los tramos anteriores
# completos. Al final imprime el consumo y el costo total.