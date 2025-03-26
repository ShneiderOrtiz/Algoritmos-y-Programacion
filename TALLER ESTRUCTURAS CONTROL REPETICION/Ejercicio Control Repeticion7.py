n = int(input("Ingrese el número de estudiantes: "))
max_altura = 0
for _ in range(n):
    altura = float(input("Ingrese la altura del estudiante: "))
    if altura > max_altura:
        max_altura = altura
print("Altura máxima:", max_altura)
