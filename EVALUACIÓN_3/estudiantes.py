# Lista de estudiantes con sus respectivas notas
resultados_estudiantes = [
    ['Aquiles Baeza', 4.5, 5.7, 7.0, 5.3],
    ['Wendy Sulca', 4.3, 4.5, 5.2, 5.3],
    ['Delfin Quispe', 3.9, 4.8, 5.5, 5.0],
    ['Armando Casas', 2.8, 4.0, 5.5, 6.1]
]

# Procesamos cada estudiante
for estudiante in resultados_estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1:]  # Todas las posiciones después del nombre
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Notas = {notas} | Promedio = {round(promedio, 2)}")
