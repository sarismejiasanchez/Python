'''
En este desafío, debes dibujar un triángulo equilatero usando bucles.

Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, respectivamente. Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable.
'''
def print_triangle(size, character):
  
  triangle = ""
  
  for i in range(size):
    spaces = " " * (size - i - 1) 
    chars = character * (2 * i + 1)
    triangle += spaces + chars + "\n"
  return triangle

response = print_triangle(3, '*')
print(response)
response = print_triangle(6, "$")
print(response)

'''
def print_triangle(size, character):
  triangle = ""
  
  for i in range(1, size + 1):
    spaces = " " * (size - 1)
    lines = character * (2 * i - 1)
    
    if (i == size):
      triangle += spaces + lines
    else:
      triangle += spaces + lines + "\n"
      
  return triangle

print(print_triangle(3, "$"))
'''
      