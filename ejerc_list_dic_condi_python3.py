"""Nivel 2: El Desafío (Lógica y Condicionales)
Aquí es donde combinas el Capítulo 4 (Listas) con el Capítulo 5 (Instrucciones if). Esto es crucial.
Ejercicio 2.1: El Filtro (El Portero)
Crea una lista de precios: precios = [15.00, 22.50, 10.15, 30.00, 5.75, 40.20].
Crea dos listas vacías: baratos y caros.
Usa un bucle for para iterar sobre precios.
Dentro del bucle, usa un if-else para comprobar si el precio es menor de 20.00.
Si es menor, añádelo a baratos. Si es mayor o igual, añádelo a caros.
Imprime ambas listas al final."""

# creo la lista de precios
lista_precios = [12000, 1234,4322,34,2345,1233,2322,52525,252552,2,25255]
#creo lista de caros y baratos
baratos = []
caros = []

# bucle para condicionar el algoritmo
for precio in lista_precios:
    if precio < 2000:
        baratos.append(precio)
    elif precio >= 2000:
        caros.append(precio)
print(f"los precios caros (mayores a 2000) son=")
print(caros)
print(f"los precios mas baratos (menores a 2000) son=")
print(baratos)

print()
print("-"*20)

"""Ejercicio 2.2: Búsqueda y Modificación (El Editor)
Crea una lista de invitados: invitados = ['ana', 'luis', 'pedro', 'sofia', 'miguel'].
Supongamos que 'pedro' no puede venir, pero 'juan' lo reemplazará.
Usa un bucle for con enumerate() para obtener tanto el índice como el valor.
Dentro del bucle, comprueba si el invitado es 'pedro'.
Si lo es, usa el índice para modificar la lista invitados en esa posición, cambiándola por 'juan'. 
(Ej: invitados[indice] = 'juan').
Imprime la lista final de invitados."""

lista_invitados = ["juan", "maria","estermocleido", "petrosqui", "uribe"]
lista = []
# convierto en diccionario directamente con dict

lista = dict(enumerate(lista_invitados))
print(lista)

lista[0]="pedro"
print(lista)

#ahora usando un bucle

invitados = ["juan", "maria","estermocleido", "petrosqui", "uribe"]
list = []
# creo el bucle con enumerate para imprimir el dccionario

for i, valor in enumerate(invitados):
    print(i,valor)
print()
print("-"*20)

# bucle para cambiar a juan
print(invitados)
for i in invitados:
    if i == "juan":
        invitados[0]="pedro"
print(invitados)
print()
print("-"*20)

"""1. El Podio de Ganadores (Nivel Básico)
El objetivo: Usar enumerate para crear una lista numerada que empiece en 1 (como un ranking).
Datos: Tienes una lista de los ganadores de una carrera.
Python
ganadores = ['Marcos', 'Lina', 'David']
Misión: Escribe un bucle for que use enumerate para imprimir el podio.
Resultado esperado:
1. Marcos
2. Lina
3. David"""

podio = ["carlos","marcos","mariacamila"]

#bucle par imprimir el podio
lista = dict(enumerate(podio,start=1))
print(lista)

for i,v in lista.items(): #bucle en lista que ya es un diccionario con pares items para iterar en cada item del diccioanrio y no solo en las claves
    print(f"{i}-{v}") # imprimo i y valor

"""2. El Modificador de Índices Pares (Nivel Intermedio)
El objetivo: Usar el índice que te da enumerate para tomar una decisión y modificar la lista original.
Datos: Tienes una lista de tareas.
Python
tareas = ['Lavar ropa', 'Hacer mercado', 'Estudiar Python', 'Pasear al perro', 'Llamar a mamá']
Misión: Quieres poner en mayúsculas solo las tareas que están en posiciones pares (índice 0, 2, 4, etc.).
Pista: Dentro del bucle for, necesitarás un if que revise el índice. Para saber si un número es par, puedes usar
el operador % (módulo): if indice % 2 == 0:.
Resultado esperado:
['LAVAR ROPA', 'Hacer mercado', 'ESTUDIAR PYTHON', 'Pasear al perro', 'LLAMAR A MAMÁ']"""

# lista de tares
tareas = ['Lavar ropa', 'Hacer mercado', 'Estudiar Python', 'Pasear al perro', 'Llamar a mamá']

for i,t in enumerate(tareas):
    if i%2==0:
        tareas[i]=t.upper()
print(tareas)
print()
print("-"*20)

"""3. El Detective de Índices (Nivel Pro)
El objetivo: Usar enumerate para encontrar todas las posiciones de un ítem específico en una lista.
Datos: Tienes una lista de ventas donde un producto se repite.
Python
ventas = ['camisa', 'pantalon', 'zapatos', 'camisa', 'corbata', 'camisa']
Misión: El usuario quiere saber en qué posiciones de la lista se vendió una 'camisa'.
Crea una lista vacía llamada posiciones_encontradas.
Usa enumerate para recorrer ventas.
Cada vez que el valor sea 'camisa', añade el índice a tu lista posiciones_encontradas.
Imprime la lista posiciones_encontradas al final.
Resultado esperado:"""

ventas = ['camisa', 'pantalon', 'zapatos', 'camisa', 'corbata', 'camisa']
encontrar = []

# encontrar en que posiciones se vendio camisas
for i,v in enumerate(ventas):
    if v == "camisa":
        encontrar.append(i)

print(f"psosiciones en las que camisa se vendio {encontrar}")
print()
print("-"*20)

"""El objetivo: Usar el índice para aplicar un cambio a la lista de forma periódica.
Datos: Tienes una lista de productos en un almacén.
Python
productos = ['caja', 'caja', 'caja', 'caja', 'caja', 'caja', 'caja', 'caja']
Misión: Tienes que revisar la calidad de cada 3er producto. Modifica la lista para que cada 3er ítem 
(índice 0, 3, 6, ...) sea reemplazado por 'caja REVISADA'.
Pista: Necesitarás el operador módulo (%). Un índice es múltiplo de 3 si indice % 3 == 0.
Resultado esperado:"""

#lista de productos del almacen
productos = ['caja', 'caja', 'caja', 'caja', 'caja', 'caja', 'caja', 'caja']

#revisar la calidad de cadda 3er producto
for i,p in enumerate(productos): # bucle for con enumerate para poder obtener indicey valor
    if i%3==0: # si el indice es multiplo de 3
        productos[i]="caja revisada" # se modificara ese indice a su valor (caja revisada)
print(productos)
print()
print("-"*20)

"""5. Las Listas Paralelas (El uso "Pro" de enumerate)
El objetivo: Usar el índice de enumerate para "conectar" dos listas que se corresponden.
Datos: Tienes dos listas. La primera tiene los nombres de los estudiantes y la segunda tiene sus notas.
La nota en notas[0] pertenece al estudiante en estudiantes[0].
Python
estudiantes = ['Ana', 'Luis', 'Pedro', 'Sofia']
notas = [85, 55, 92, 48]
Misión:
Crea una lista vacía llamada reprobados.
Recorre una de las listas (ej: notas) usando enumerate para obtener el indice y la nota.
Usa un if para comprobar si la nota es menor a 60.
Si es menor a 60, usa el indice para buscar el nombre del estudiante en la otra
lista (estudiantes[indice]) y añádelo a la lista reprobados.
Imprime la lista reprobados al final.
Resultado esperado:"""

estudiantes = ['Ana', 'Luis', 'Pedro', 'Sofia']
notas = [85, 55, 92, 48]
notas_perdidas = []
estudiantes_reprobados = []
#bucle para recorrer la lista de nota e identificar notas menores a 60
for i,v in enumerate(notas):
    if v<60:
        notas_perdidas.append(i)
print(f"indices con valores menores a 60 {notas_perdidas}")
print()
print("-"*20)

for i,v in enumerate(estudiantes):
    if i in notas_perdidas:
        estudiantes_reprobados.append(v)
print(estudiantes_reprobados)