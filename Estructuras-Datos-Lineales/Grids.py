"""
Otros nombres:
Bi-dimensional array
Two-dimensional array
Grid
Rejilla
Malla
Tabla

Grid type class
Methods:
    1. Initialize
    2. Get height
    3. Get width
    4. Access item
    5. String representation
"""

from Arrays import Array

class Grid():
    def __init__(self, rows, columns, fill_value = None):
        # Definir Datos
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    
    # Obtener altura
    def get_height(self):
        # Returns the number of rows.
        return len(self.data)
    
    # Obtener ancho
    def get_width(self):
        """
        self.data[0] porque estamos anidando un array en otro
        y lo estamos haciendo en la posicion 0
        """
        # Returns the number of columns.
        return len(self.data[0])
    
    # Obtener un elemento en particular
    def __getitem__(self, index):
        # Supports two-dimensional indexing with [row][column].
        return self.data[index]
    
    # Representacion en string
    def __str__(self):
        result = ""
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row, col]) +  " "
            
            result += "\n"
        
        return str(result)


def main():
    weigth = int(input("Ingrese el alto de la matriz: "))
    width = int(input("Ingrese el ancho de la matriz: "))
    matrix = Grid(weigth, width)
    print(matrix)
    #print("El tamaño de la matriz es: ", matrix.__get_height__())
    
    #print("El arreglo es: ", matrix.__str__())
    """
    print("El arreglo con datos secuenciales pares es: ", arreglo.__secuentialfill__())
    print("La sumatoria del arreglo secuencial es: ", arreglo.__sum__())
    print("El arreglo con datos aleatorios es: ", arreglo.__randomfill__(0, 100))
    print("La sumatoria del arreglo aleatorio es: ", arreglo.__sum__())
    """

if __name__ == '__main__':
    main()