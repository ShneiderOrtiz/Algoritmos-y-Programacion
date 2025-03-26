num_estudiantes = int(input("Ingrese el número de estudiantes: "))
puntajes = {}
for _ in range(num_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    puntaje = float(input("Ingrese el puntaje: "))
    puntajes[nombre] = puntaje

max_estudiante = max(puntajes, key=puntajes.get)
min_estudiante = min(puntajes, key=puntajes.get)
promedio = sum(puntajes.values()) / num_estudiantes
menor_al_promedio = sum(1 for p in puntajes.values() if p < promedio) / num_estudiantes * 100
mayor_al_promedio = sum(1 for p in puntajes.values() if p > promedio) / num_estudiantes * 100

print(f"Mayor puntaje: {max_estudiante} con {puntajes[max_estudiante]}")
print(f"Menor puntaje: {min_estudiante} con {puntajes[min_estudiante]}")
print(f"Promedio general: {promedio:.2f}")
print(f"Porcentaje debajo del promedio: {menor_al_promedio:.2f}%")
print(f"Porcentaje encima del promedio: {mayor_al_promedio:.2f}%")
