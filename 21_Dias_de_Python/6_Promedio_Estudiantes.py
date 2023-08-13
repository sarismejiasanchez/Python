'''
Obtén el promedio de los estudiantes
En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.

Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá las siguientes propiedades:

"name": El nombre del estudiante
"grades": Las notas de cada materia del estudiante
A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad "class_average" con el promedio de la clase y una lista de "students" con los estudiantes y sus promedios individuales.

Es importante mencionar que los promedios deben ser calculados con precisión y se deben redondear a dos decimales para que los test pasen sin problema alguno. Puedes usar el método round() el cual se usa de la siguiente manera 👇

number = 100.32433
number = round(number, 2)

# 100.32
'''

def get_student_average(students):
    class_total = 0
    student_averages = []
    
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades) / len(grades)
        student_averages.append({"name": name, "average": round(average, 2)})
        class_total += average
    
    class_average = class_total / len(students)
    
    result = {
        "class_average": round(class_average, 2),
        "students": student_averages
    }
    
    return result

# Ejemplo
estudiantes = [
    {
        "name": "Pedro",
        "grades": [90, 87, 88, 90],
    },
    {
        "name": "Jose",
        "grades": [99, 71, 88, 96],
    },
    {
        "name": "Maria",
        "grades": [92, 81, 80, 96],
    },
]

resultado = get_student_average(estudiantes)
print(resultado)