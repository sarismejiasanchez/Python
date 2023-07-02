"""
¿Qué es una estructura de datos?

Representación interna de una colección de información.

Conceptos clave
Elemento: valor almacenado en las posiciones del array.
Índice: referencia a la posicion del elemento.


Los array son restrictivos

No pueden:
Agregar posiciones.
Remover posiciones.
Modificar su tamaño.
Su capacidad se define al crearse.

¿Dónde se utilizan?
Un videojuego con sprites de 100x100 px.
Opciones en un menu.

Módulo ‘array’ (propio de Python)
Solo almacena números y caracteres.
Basado en listas
"""

"""
Nuestro propio array
Métodos:
Crearse.
Longitud.
Representación string.
Pertenencia.
Índice.
Reemplazo.
"""

from random import randint

# Crear una Clase de Array
class Array:
    def __init__(self, capacity, fill_value = None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    # Obtener el tamaño del array
    def __len__(self):
        return len(self.items)
    
    # Definir como string sus elementos
    def __str__(self):
        return str(self.items)
    
    # Iterador
    def __iter__(self):
        return iter(self.items)
    
    # Obtener un elemento en particular el array
    def __getitem__(self, index):
        return self.items[index] 
    
    # Reemplazar elementos
    def __setitems__(self, index, new_item):
        self.items[index] = new_item    
    
    # Poblar slots con numeros secuenciales
    def __secuentialfill__(self):
        for i in range(self.__len__()):
            self.items[i] = i + 2
        return str(self.items)
    
    # Poblar slots con numeros aleatorios
    def __randomfill__(self, lower, upper):
        self.items = [randint(lower, upper) for i in range (len(self.items))]
        return str(self.items)

    # Sumatoria
    def __sum__(self):
        return sum(self.items)

from Arrays import Array

def main():
    size = int(input("Ingrese el tamaño del arreglo: "))
    arreglo = Array(size)
    print("El tamaño del arreglo es: ", arreglo.__len__())
    print("El arreglo es: ", arreglo.__str__())
    print("El arreglo con datos secuenciales pares es: ", arreglo.__secuentialfill__())
    print("La sumatoria del arreglo secuencial es: ", arreglo.__sum__())
    print("El arreglo con datos aleatorios es: ", arreglo.__randomfill__(0, 100))
    print("La sumatoria del arreglo aleatorio es: ", arreglo.__sum__())
    

if __name__ == '__main__':
    main()

        