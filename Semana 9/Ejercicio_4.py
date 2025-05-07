estudiantes = {}
num_estudiantes = int(input("¿Cuántos estudiantes deseas ingresar? (máximo 10): "))
num_estudiantes = min(num_estudiantes, 10)

for i in range(1, num_estudiantes + 1):
    nombre = input(f"Nombre del estudiante #{i}: ")
    nota = float(input(f"Nota de {nombre}: "))
    estudiantes[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }

aprobados = []
suspendidos = []
suma_notas = 0

for est in estudiantes.values():
    suma_notas += est["nota"]
    if est["nota"] >= 5:
        aprobados.append(est["nombre"])
    else:
        suspendidos.append(est["nombre"])

print("\nEstudiantes aprobados:", aprobados)
print("Estudiantes suspendidos:", suspendidos)
print("Nota media de la clase:", round(suma_notas / num_estudiantes, 2))
