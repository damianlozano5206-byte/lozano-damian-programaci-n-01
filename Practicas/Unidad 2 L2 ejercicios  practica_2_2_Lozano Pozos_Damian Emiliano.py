##Ejercicio 1##
valor = 7
es_par= valor % 2 ==0
print("El numero(",es_par,")es par")
## Se especifica cada variable y primero es par y luego el numero%2 )

##Ejercicio 2##
texto_a="5"
texto_b="3"
suma_texto= texto_a + texto_b
print(f"sin convertir: {texto_a} + {texto_b} = {suma_texto}")
resultado_con_numero=int(texto_a)+int(texto_b)
print(f"resultado de la suma es {resultado_con_numero}")
##La diferencia entre la version sin convertir y la version con numero es que la primera version al tener los numeros entre "" python los detecta como texto y los agrupa en vez de sumarlos y int lo que hace es que python los detecte como numeros##

##Ejercicio 3##
nombre_persona = "Damian"
Edad_persona = 18
Estatura_persona = 1.66
es_estudiante = True
print("Reporte")
print("Nombre:", nombre_persona, type(nombre_persona))
print("Edad:", Edad_persona, type(Edad_persona))
print("Estatura:", Estatura_persona, type(Estatura_persona))
print("Es estudiante:", es_estudiante, type(es_estudiante))
##Extra##
presentación = "hola soy " + nombre_persona + " y tengo " + str(Edad_persona) + " años y mido " + str(Estatura_persona)
print(presentación)
##note que si pones un 0 en un numero entero python no lo detecta y solo te suelta los numeros del 1 en adelante##

##Ejercicio 4##
num_a = 5
num_b = 5
print(f" {num_a}+{num_b} es {num_a+num_b}")
print(f" {num_a}-{num_b} es {num_a-num_b}")
print(f" {num_a}*{num_b} es {num_a*num_b}")
print(f" {num_a}/{num_b} es {num_a/num_b}")
## las operaciones de dos variables se tienen que usar print(f"etc)si no solo imprimira el texto dentro de los parentesis

##Ejercicio 5##
num_a= 5
num_b= 5
print("divison:",num_a/num_b)
print("residuos:",num_a%num_b)

##para mostrar residuos se usa como si fuera una division normal pero en vez de / se usa %##

##Ejercicio 6##
##numeros distintos##
x = 10
y = 5
mayor = x > y
menor = x < y
igual = x == y
es_diferente = x != y
print(f"{x} > {y} es {mayor}")
print(f"{x} < {y} es {menor}")
print(f"{x} == {y} es {igual}")
print(f"{x} != {y} es {es_diferente}")

##numeros iguales##
x = 10
y = 10
mayor = x > y
menor = x < y
igual = x == y
es_diferente = x != y
print(f"{x} > {y} es {mayor}")
print(f"{x} < {y} es {menor}")
print(f"{x} == {y} es {igual}")
print(f"{x} != {y} es {es_diferente}")

##para estas operaciones funcionan muy parecido a las demas solo cambia la simbologia y siempre se usa print(f" etc)para que funcione y las variables van en {}

##Ejercicio 7##
edad = 18
estatura = 1.60
es_mayor_de_edad = edad >=18
es_alto = estatura <=1.70
es_mayor_de_edad_y_alto = es_mayor_de_edad and es_alto
es_mayor_de_edad_o_alto = es_mayor_de_edad or es_alto
es_mayor_de_edad_no = not es_mayor_de_edad

print(f"es mayor de edad: {es_mayor_de_edad}")
print(f"es alto: {es_alto}")
print(f"es mayor de edad y alto: {es_mayor_de_edad_y_alto}")
print(f"es mayor de edad o alto: {es_mayor_de_edad_o_alto}")
print(f"no es mayor de edad: {es_mayor_de_edad_no}")

##Las expresiones booleanas serian como edad y estatura y para este ejercicio el > tiene que estar apuntando hacia la opcion que se requiera por ejemplo para la edad necesitamos que tena mas de 18 años ,entonces queda asi edad >=18,si el daro de edad es menor a 18 marcara false a es mayor de edad

##Ejercicio 8##
v1 = 7
v2 = 8
v3 = 8
promedio = (v1 + v2 + v3)/3
positivo = promedio >= 6 
print(f"calificaciones: {v1}, {v2}, {v3}")
print(f"promedio: {promedio}")
print(f"está aprobado: {positivo}")

v1 = 6
v2 = 5
v3 = 4
promedio = (v1 + v2 + v3)/3
positivo = promedio >= 6 
print(f"calificaciones: {v1}, {v2}, {v3}")
print(f"promedio: {promedio}")
print(f"está aprobado: {positivo}")
##para sacar el promedio se suman las variables y se dividen entre el numero de variables y para saber si esta aprovado se hace una expresion booleana que diga si el promedio es mayor o igual a 6 y para que se pueda expresar correctamente se tiene que imprimir de forma separada como se muestra en el ejercicio y yimportante no poner ==True despues de el >=6 por que si no solo soltara false##

##Ejercicio 9##

##combinacion 1##
edad = 18
pais_origen = "mexicana"
es_elegible= edad >=17 and pais_origen == "mexicana"
es_elegible_or = edad > 17 or pais_origen == "mexicana"
print(f"edad: {edad}")
print(f"pais de origen: {pais_origen}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##combinacion 2##

edad = 15
pais_origen = "mexicana"
es_elegible= edad >=17 and pais_origen == "mexicana"
es_elegible_or = edad > 17 or pais_origen == "mexicana"
print(f"edad: {edad}")
print(f"pais de origen: {pais_origen}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##combinacion 3##

edad = 25
pais_origen = "canadienses"
es_elegible= edad >=17 and pais_origen == "mexicana"
es_elegible_or = edad > 17 or pais_origen == "mexicana"
print(f"edad: {edad}")
print(f"pais de origen: {pais_origen}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##combinacion 4##

edad = 15
pais_origen = "canadienses"
es_elegible= edad >=17 and pais_origen == "mexicana"
es_elegible_or = edad > 17 or pais_origen == "mexicana"
print(f"edad: {edad}")
print(f"pais de origen: {pais_origen}")
print(f"es elegible: {es_elegible}")
print(f"es elegible or: {es_elegible_or}")

##el es elegible se escibre como edad >=17 and pais_origen == "mexicana" y el es elegible or se escribe como edad > 17 or pais_origen == "mexicana" y para que funcione correctamente se tiene que poner print(f" etc) y las variables van entre {} y si no se hace asi solo imprimira el texto dentro de los parentesis##
