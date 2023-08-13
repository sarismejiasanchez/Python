'''
Playground - Calcula la propina
En este desafío tendrás que calcular la propina que deben dejar 
los clientes de un restaurante en función de su consumo.

La función calculate_tip recibirá dos parámetros, 
bill_amount que representa el costo total de lo que se haya consumido y 
tip_percentage que representa el porcentaje de propina a dejar. 
Ambos valores serán de tipo float y siempre serán positivos, incluyendo el 0. 
La función deberá devolver el valor de la propina como un número.

Recuerda que para redondear a dos decimales tendrás que hacer uso de 
round(numero, cantidad de decimales)
'''
def calculate_tip(bill_amount, tipPercentage):
  tip = round(((bill_amount * tipPercentage) / 100), 2)
  return tip
 
tip = calculate_tip(100, 10)
print(tip)
tip = calculate_tip(1524.33, 25)
print(tip)