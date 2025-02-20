import math  #Importamos la librería para la raíz cuadrada

#Ingresar los lados del triángulo
a = float(input("Ingrese el lado a del triángulo: "))
b = float(input("Ingrese el lado b del triángulo: "))
c = float(input("Ingrese el lado c del triángulo: "))

#Se calcula el semiperímetro
s = (a + b + c) / 2

#Se calcula el área usando la fórmula de Herón
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

#Resultados
print(f"El área del triángulo es: {area:.2f}")
