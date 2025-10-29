"""Ejercicio 1.2: Creando una Nueva Lista (El Transformador)
Crea una lista de números del 1 al 10: numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Crea una lista vacía llamada dobles.
Usa un bucle for para iterar sobre numeros. Dentro del bucle, multiplica cada número por 2 y añade el
resultado a la lista dobles.
Al final, imprime la lista numeros y la lista dobles para comparar."""

numeros = [1,2,3,4,5,6,7,8,9,10] #lista de numeros del 1 al 10
dobles = [] # lista vacia llamada dobles

#bucle para multiplicar cada elemento de la lista por 2
for num in numeros:
    num = num*2
    dobles.append(num) # inserto cada elemento en la lista vacia dobles
print(dobles)
print(numeros)

print()
print("-"*20)

# ejercicios
"""Ejercicio 1.1: El Fanático de la Comida Basado en el ejercicio 4-1 del libro.
Crea una lista de tus 3 comidas favoritas (ej: comidas = ['pasta', 'tacos', 'ensalada']).
Usa un bucle for para imprimir el nombre de cada comida.
Modifica tu bucle para imprimir una frase sobre cada comida, como "Uno de mis platos favoritos es 
[nombre de comida]".
Añade una línea final fuera del bucle, como "¡Realmente me encanta la comida!"."""

comidas=["arroz", "lentejas", "mariscos"]

#bucle para imprimir el nombre de cada comida
print("El nombre de cada comida es =")
for comida in comidas:
    print(comida)
print("realmente me encanta la comida")

print()
print("-"*20)

#bucle modificado para imprimir frase sobre cada comida
for comida in comidas:
    print(f"{comida} es la comida favorita de sebastian")
print("realmente me encanta la comida")

print()
print("-"*20)

"""Ejercicio 1.3: Estadísticas Simples (El Analista Básico)
Usa list(range(1, 101)) para crear una lista de números del 1 al 100.
Usa min(), max() y sum() en la lista para verificar que funciona.
El reto: Sin usar sum(), usa un bucle for para calcular la suma total de todos los números en la lista. 
(Necesitarás una variable total_suma inicializada en 0 antes del bucle)."""

#crear lista del 1 al 101
lista = []

for num in range(1,101):
    lista.append(num)
print(lista)

# sin usar bucle

lista_num = list(range(1,101))
print(lista_num)

minimo = min(lista)
maximo = max(lista)
suma = sum(lista)
print(minimo)
print(maximo)
print(suma)

# bucle para sumar todos los numeros de la lista
print()
print("-"*20)

print("sumar los numeros de la lista con un bucle")

total_suma = 0 #variable total_suma la iniciamos en cero con el fin de que empiece de cero
for num in lista:
    total_suma = total_suma + num # empieza desde num 1 + total 0 , 1  + 2 = 3, ,,,,
print(total_suma)

print()
print("-"*20)

"""Misión:
Datos: Tienes una lista con las notas finales de un examen.
Imprime la nota más alta (la mejor nota).
Imprime la nota más baja (la peor nota).
Imprime cuántos estudiantes presentaron el examen (¡usa len()).
Desafío: Calcula e imprime la nota promedio de la clase. Pista: 
El promedio es (la suma total) / (la cantidad de notas)."""

# lista notas de clase
notas = [5,4.1,3.4,2,5]

print("nota mas alta=")
maxima = max(notas)
print()
print("nota mas baja")
minima = min(notas)
print()
print("numero de estudiantes que presentaron el examen=")
numero = len(notas)
print(numero)
print()
print("promedio de las notas ")
promedio = sum(notas)/len(notas)
print(promedio)

"""Ejercicio B: "Gastos de la Semana" 🛒

Datos: Tienes una lista que registra cuánto gastaste en almuerzos cada día de la semana laboral (lunes a viernes).
Python
Misión:
Imprime el almuerzo más caro de la semana.
Imprime el almuerzo más barato.
Imprime el gasto total en almuerzos de la semana."""

gastos = [1500, 23000,34000,4500,2000]

# almuerzo mas caro de la semana
maximo = max(gastos)
print(f"el almuerzo mas costoso fue {maximo}")
print("-"*20)
minimo = min(gastos)
print(f"el almuerzo mas economico es {minimo}")
print("-"*20)
suma = sum(gastos)
print(f"total gastado en almuerzos {suma}")

