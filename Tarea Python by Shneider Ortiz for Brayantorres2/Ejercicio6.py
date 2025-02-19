#Ingresar cantidades de hombres y mujeres
hombres = int(input("Ingrese el número de hombres en el grupo: "))
mujeres = int(input("Ingrese el número de mujeres en el grupo: "))

#Calcular el total de estudiantes
total_estudiantes = hombres + mujeres

#Calcular los porcentajes
porcentaje_hombres = (hombres / total_estudiantes) * 100
porcentaje_mujeres = (mujeres / total_estudiantes) * 100

#Resultado final
print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
