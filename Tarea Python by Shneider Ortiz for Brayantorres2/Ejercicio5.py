#Insertar valor de las notas parciales
nota1 =float(input("Ingrese la calificacion de la primera nota"))
nota2 =float(input("Ingrese la calificacion de la segunda nota"))
nota3 =float(input("Ingrese la calificacion de la tercera nota"))

#Insertar valor del examen final
nota_examen =float(input("Ingrese la calificacion del examen final"))

#Insertar valor del trabajo final
trabajo_final =float(input("Ingrese la calificacion del trabajo final"))

#Calcular el total de las notas (teniendo en cuenta que vale el 55%)
total_notas = (nota1 + nota2 + nota3) / 3

#Calcular el total de el examen final
total_examen = (nota_examen) * 0.30

#Calcular el total del trabajo final
total_trabajo = (trabajo_final) * 0.15

#Calcular calificacion final
Calificacion_final = (0.55 * total_notas + total_examen + total_trabajo)

#Resultado
print(f"El total de las notas que valen el 55% es:{total_notas:.2f}")
print(f"El total en el examen que vale el 30% es:{total_examen:.2f}")
print(f"El total en el trabajo final que vale el 15% es:{total_trabajo:.2f}")
print(f"La calificacion final del estudiante es:{Calificacion_final:.2f}")