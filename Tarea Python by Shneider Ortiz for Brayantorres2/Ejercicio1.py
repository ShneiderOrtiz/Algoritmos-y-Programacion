#Ingresar dato de edad de cada persona
edad1 = float(input("Ingrese la primera edad: "))
edad2 = float(input("Ingrese la segunda edad: "))
edad3 = float(input("Ingrese la tercera edad: "))

#Se calcula el promedio
promedio = (edad1 + edad2 + edad3) / 3

#Resultado final
print(f"El promedio de edad es: {promedio:.2f}")
