"""Información Personal:
Crea un diccionario llamado persona que almacene tu nombre, apellido, edad y ciudad donde vives
(usa claves como 'nombre', 'apellido', 'edad', 'ciudad').
Imprime cada pieza de información accediendo a los valores mediante sus claves.
Modifica el valor de la clave 'ciudad' a otra ciudad.
Añade una nueva clave-valor al diccionario, como 'profesion' con tu profesión o una inventada.
Imprime el diccionario completo para ver los cambios."""

persona = {
    "nombre":"sebastian",
    "apellido":"lopez",
    "edad":38,
    "ciudad":"medellin",
}

# imprimir los valores accediendo a las claves
print("estos son los valores de cada clave guardad en el diccionario =")
for clave in persona.values():
    print(f"{clave}")
print()# espacio
print("-"*20)

#Modifica el valor de la clave 'ciudad' a otra ciudad.
persona["ciudad"] = "la estrella"
print(f"la nueva ciudad es {persona["ciudad"]}")

print()

print("la nueva lista es ahora la siguiente=")

for clave in persona.values():
    print(clave)
print()
print("-"*20)

#Añade una nueva clave-valor al diccionario, como 'profesion' con tu profesión o una inventada.
persona["profesion"] = "mecanic"
persona["celular"] = 313431641
#imprimiendo nuevo diccionario
print(f"la nueva lista de elementos del diccioanrio persona es=")
for clave in persona.values():
    print(clave)
print()
print("-"*50)

"""Mascota Simple:
Crea un diccionario vacío llamado mascota.
Añade las claves 'tipo_animal' y 'nombre_dueño' con sus respectivos valores.
Imprime el diccionario.
Usa la sentencia del para eliminar la clave 'nombre_dueño'.
Imprime el diccionario final."""

mascota = {}

#Añade las claves 'tipo_animal' y 'nombre_dueño' con sus respectivos valores.

mascota["tipo_animal"] = "peligroso"
mascota["nombre_dueño"] = "petrosqui"

print(f"el diccionario mascota contiene los siguientes elementos {mascota}")
print(f"{mascota["tipo_animal"]}")
print(f"{mascota["nombre_dueño"]}")


#Usa la sentencia del para eliminar la clave 'nombre_dueño'.
del(mascota["nombre_dueño"])
print(f"elementos del diccionario mascota {mascota}")

"""Glosario Básico:
Crea un diccionario llamado glosario_python con tres palabras de programación que hayas aprendido 
(ej. 'variable', 'lista', 'diccionario') como claves y sus significados simples como valores.
Imprime cada palabra y su significado de forma separada, accediendo a ellos por su clave."""

glosario_python = {
    "variable":"contenedor que se usa para guardar un valor en el pc",
    "python" : "lenguaje de programacion",
    "lista" : "es un contenedor de elementos de todo tipo, talmente inmutable"
}
print()

print("Diccionario de python basico.")
print()
for clave, valor in glosario_python.items():
    print(f"{clave} = {valor}")

print()
print("otra forma de hacerlo - iterando solo sobre las claves")

for clave in glosario_python: # itero sobre las claves
    valor = glosario_python[clave] # genero una variable llamada valor y la defino con cada clave en cada iteracion
    print(f"{clave} = {valor}") # me devuelve todos los valores y las claves

"""Nivel 2: Iteración y Técnicas Intermedias"""
"""Recorriendo Información Personal:
Retoma el diccionario persona del ejercicio 1.
Utiliza un bucle for y el método .items() para imprimir cada clave y su valor correspondiente en líneas separadas, 
por ejemplo: "Clave: nombre, Valor: [TuNombre]"."""
print()
persona = {
    "nombre":"sebastian",
    "apellido":"lopez",
    "edad":38,
    "ciudad":"medellin",
}

# imprimir la informacion clave valor separa por lineas
print("imprimire el diccionario personas clave y valor")
print("-"*20)
print("En el diccionario persona estos son los items clave y su respectivo valor=")
for clave, valor in persona.items():
    print(f"{clave} = {valor}")
print()
print()

"""Lenguajes Favoritos:

Crea el diccionario lenguajes_favoritos como se muestra en el capítulo.
Usa un bucle for para recorrer solo las claves del diccionario (usando .keys() o el comportamiento por defecto)
e imprime un mensaje para cada persona, como "Gracias por participar, [Nombre]!".
Crea una lista amigos con dos nombres que estén en el diccionario. Dentro del bucle anterior, añade una condición if 
para imprimir un saludo especial si el nombre está en la lista amigos, mostrando también su lenguaje favorito 
(accediendo al valor a través de la clave).
Usa un bucle for para recorrer solo los valores (usando .values()) e imprime cada lenguaje mencionado.
Utiliza set() junto con .values() para imprimir una lista de los lenguajes mencionados sin repeticiones."""
print()

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

#Usa un bucle for para recorrer solo las claves del diccionario (usando .keys() o el comportamiento por defecto)
#e imprime un mensaje para cada persona, como "Gracias por participar, [Nombre]!".
print(f"\nel nombre de cada clave en el diccionario personas es =")
for name in favorite_languages.keys():
    print(f"gracias por participar {name}")
print()
#Crea una lista amigos con dos nombres que estén en el diccionario. Dentro del bucle anterior, añade una condición if
#para imprimir un saludo especial si el nombre está en la lista amigos, mostrando también su lenguaje favorito
#(accediendo al valor a través de la clave).

print(" si jen y sarah estan en el diccionario el saludo debe ser diferente")
print()

amigos = ['jen', 'sarah']
for name in favorite_languages.keys(): #keys para que me de solo las clave
    if name in amigos: # condicional si estan en la lista amigos un mensaje diferente
        print(f"hola {name} ustedes son perbersos")
    else: # condicional sino el mensjae sera diferente
        print(f"hola {name} ustedes si son mis amigos")
print()
print("-"*20)
for name, lenguaje in favorite_languages.items(): # items para iteras sobre la clave yel valor
    if name in amigos:
        print(f"a {name} que le gusta {lenguaje} no sabes que estas haciendo")
    else:
        print(f"a {name} que le gusta {lenguaje} bienvenido")
print()

"""Usa un bucle for para recorrer solo los valores (usando .values()) e imprime cada lenguaje mencionado.
Utiliza set() junto con .values() para imprimir una lista de los lenguajes mencionados sin repeticiones."""
print(f"estos son los lenguajes que hay en el diccionario=")
for valor in favorite_languages.values():
    print(valor)

lenguajes = set(favorite_languages.values())
print(f"los lenguajes que se usan sin repetir ninguno {lenguajes}")

"""
6.  **Glosario Completo:**
    * Retoma el `glosario_python` del ejercicio 3.
    * Añade 5 términos más de Python con sus significados.
    * Utiliza un bucle `for` con `.items()` para imprimir cada palabra y su significado de forma ordenada y limpia (ej. con la palabra en negrita o seguida de dos puntos y el significado en la línea siguiente).
    * Intenta imprimir el glosario ordenado alfabéticamente por clave utilizando `sorted()` sobre las claves.
"""
print()
print("-"*20)
# creo el diccionario de python con mas palabras
palabras_python = {
    "variable": "Espacio de memoria que almacena un valor y se identifica con un nombre",
    "función": "Bloque de código reutilizable que realiza una tarea específica",
    "lista": "Estructura de datos ordenada y mutable que almacena elementos",
    "diccionario": "Estructura de datos que almacena pares clave-valor",
    "bucle": "Estructura de control que repite la ejecución de código",
    "módulo": "Archivo que contiene definiciones y declaraciones de Python",
    "clase": "Plantilla para crear objetos que define atributos y métodos",
    "string": "Tipo de dato que representa texto (cadena de caracteres)",
    "import": "Instrucción para incluir módulos o librerías en el código",
    "sintaxis": "Conjunto de reglas que definen cómo escribir código correctamente"
}

# Añade 3 términos más de Python con sus significados.
palabras_python["tupla"] = "Estructura de datos ordenada e inmutable que almacena elementos"
palabras_python["excepción"] = "Error que ocurre durante la ejecución de un programa"
palabras_python["decorador"] = "Función que modifica el comportamiento de otra función"

# imprimire las palabras y significados del diccionario apra ver que valores y claves tiene.
print("estos son las palabras y significados que hay en el diccionario palabras_python")
print()

for palabra, significado in palabras_python.items():
    print(f"{palabra} = {significado}")


#si quisiera que cada palabra tuviera la enumeracion seria asi
print()
print("estos son las palabras y significados que hay en el diccionario palabras_python")
print("_"*20)

contador = 0 #debo inicilizar el contador para uqe el for permita sumar desde 1 como lo tengo definido en lavariable

for palabra, significado in sorted(palabras_python.items()): #sorted para organizar en orden alfabetico.
    contador= contador + 1 #variable contador mas 1 para que empiece desde 1 por que contador vale 0
    print(f"{contador}. {palabra} = {significado}")
print()
print("-"*20)
"""
7.  **Acceso Seguro con `get()`:**
    * Crea un diccionario `inventario` con nombres de frutas como claves y sus cantidades como valores
     (ej. `'manzana': 10`, `'banana': 5`).
    * Pide al usuario que ingrese el nombre de una fruta.
    * Usa el método `.get()` para obtener la cantidad de esa fruta. Si la fruta no está en el inventario,
     `.get()` debe devolver `0`. Imprime un mensaje indicando cuántas unidades hay o si no hay de esa fruta.
"""
# creo el diccionario frutas
frutas = {
    "manzanas": 15,
    "platanos": 8,
    "naranjas": 12,
    "uvas": 25,
    "fresas": 30,
    "mangos": 6,
    "piñas": 3,
    "sandias": 2,
    "peras": 10,
    "kiwis": 18
}

# pido al ususario que ingrese el nombre de una fruta para averiguar si cantidad
buscar_fruta = input("ingresa el nombre de la fruta que deseas consultar sin espacios: ").lower()

# con get defino la clave y le asigno un get con un mensaje en caso de que no tenga cantidad valores
cantidad = frutas.get(buscar_fruta,0)

print(f"la fruta {buscar_fruta} tiene cantidad {cantidad} uds")
print()
print("-"*20)

# hacer lo mismo con el diccionario de palabras python
palabras_python = {
    "variable": "Espacio de memoria que almacena un valor y se identifica con un nombre",
    "función": "Bloque de código reutilizable que realiza una tarea específica",
    "lista": "Estructura de datos ordenada y mutable que almacena elementos",
    "diccionario": "Estructura de datos que almacena pares clave-valor",
    "bucle": "Estructura de control que repite la ejecución de código",
    "módulo": "Archivo que contiene definiciones y declaraciones de Python",
    "clase": "Plantilla para crear objetos que define atributos y métodos",
    "string": "Tipo de dato que representa texto (cadena de caracteres)",
    "import": "Instrucción para incluir módulos o librerías en el código",
    "sintaxis": "Conjunto de reglas que definen cómo escribir código correctamente"
}

buscar = input("ingresa la palabra a buscar: ").lower()

significado = palabras_python.get(buscar,"no esta en el diccionario")

print(f"{buscar} = {significado}")

print()
print("-"*20)



