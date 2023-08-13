'''
Playground - Retorna el tipo

En este desafío encontrarás una función llamada solution que 
recibe un parámetro llamado valor. 
Debes encontrar el tipo de dato del parámetro valor 
y retornarlo desde la función solution.
'''

def found_type(value):
  return type(value)
  
response = found_type(1)
print(response )
response = found_type("Dieguillo")
print(response)
response = found_type(True)
print(response)