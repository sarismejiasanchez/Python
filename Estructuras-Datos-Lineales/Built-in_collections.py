# Lists
"""
Propósito general
Estructura más utilizada
Tamaño dinámico
De tipo secuencial
Ordenable
"""
list1 = list()
list2 = ['t', 25, 'cat', 3.1415]
list3 = [number ** 2 for number in range(1, 100, 3)]

print(list1)
print(list2)
print(list3)

# Tuples
"""
Inmutable (no se pueden añadir o cambiar valores).
Útiles para datos constantes.
Más rápidas que las listas.
Tipo secuencial.
"""

tuple1 = ()
tuple2 = (1274, 1275, 1276)
"""
 Aunque no tiene parentesis, por la , al final
 Python lo interpreta automáticamente como una Tupla
"""
tuple3 = 'mulan', 'puca', 'percy',

print(tuple1)
print(tuple2)

print(type(tuple3))
print(tuple3)

# Sets
"""
Almacenan objetos no-duplicados.
De acceso rápido.
Aceptan operaciones lógicas.
Son desordenados.
"""

set1 = {3, 5, 9, 3, 9}
set2 = set()
numbers = [1, 2, 3, 4, 5, 6, 1, 2]
set3 = set(numbers)

print(set1)
print(set2)
print(set3)

# Dictionaries
"""
Pares de llave/valor.
Arrays asociativos (hash maps).
Son desordenados.
Son bastante rápidos para realizar consultas.
"""

cats1 = {
    'mulan': 2,
    'pucca': 1.2,
    'percy': 4
}

"""
Usando el método dict, en una lista, incluimos los elementos de llave y valor.
No es muy utilizado, pues puede resultar complejo de leer.
"""
cats2 = dict([('mulan', 2), ('pucca', 1.2), ('percy', 4)])

cats3 = dict(mulan = 2, pucca = 1.2, percy = 4)

print(cats1)
print(cats2)
print(cats3)