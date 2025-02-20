#Insertar los datos primarios
sueldo_base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

#Calcular las comisiones (10% de cada venta)
comision_total = (venta1 + venta2 + venta3) * 0.10

#Calcular el sueldo final
sueldo_total = sueldo_base + comision_total

#Resultados
print(f"La comision total es: {comision_total:.2f} COP")
print(f"El sueldo total del vendedor es: {sueldo_total:.2f} COP")
