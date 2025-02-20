#Ingresar notas de Matemáticas
examen_mate = float(input("Ingrese la nota del examen de Matemáticas: "))
tarea1_mate = float(input("Ingrese la nota de la tarea 1 de Matemáticas: "))
tarea2_mate = float(input("Ingrese la nota de la tarea 2 de Matemáticas: "))
tarea3_mate = float(input("Ingrese la nota de la tarea 3 de Matemáticas: "))

#Se calcula promedio de tareas y nota final de Matemáticas
promedio_tareas_mate = (tarea1_mate + tarea2_mate + tarea3_mate) / 3
promedio_mate = (0.90 * examen_mate) + (0.10 * promedio_tareas_mate)

#Ingresar notas de Física
examen_fisica = float(input("Ingrese la nota del examen de Física: "))
tarea1_fisica = float(input("Ingrese la nota de la tarea 1 de Física: "))
tarea2_fisica = float(input("Ingrese la nota de la tarea 2 de Física: "))

#Se calcula promedio de tareas y nota final de Física
promedio_tareas_fisica = (tarea1_fisica + tarea2_fisica) / 2
promedio_fisica = (0.80 * examen_fisica) + (0.20 * promedio_tareas_fisica)

#Inrgresar notas de Química
examen_quimica = float(input("Ingrese la nota del examen de Química: "))
tarea1_quimica = float(input("Ingrese la nota de la tarea 1 de Química: "))
tarea2_quimica = float(input("Ingrese la nota de la tarea 2 de Química: "))
tarea3_quimica = float(input("Ingrese la nota de la tarea 3 de Química: "))

#Se calcula promedio de tareas y nota final de Química
promedio_tareas_quimica = (tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3
promedio_quimica = (0.85 * examen_quimica) + (0.15 * promedio_tareas_quimica)

#Se calcula promedio general
promedio_general = (promedio_mate + promedio_fisica + promedio_quimica) / 3

#Resultado final
print("\n---- Promedios Finales ----")
print(f"Promedio en Matemáticas: {promedio_mate:.2f}")
print(f"Promedio en Física: {promedio_fisica:.2f}")
print(f"Promedio en Química: {promedio_quimica:.2f}")
print(f"Promedio General: {promedio_general:.2f}")

