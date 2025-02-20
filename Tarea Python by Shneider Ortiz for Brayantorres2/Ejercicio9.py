#Ingresar datos al usuario
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))

#Se calcula sueldo bruto
sueldo_bruto = horas_trabajadas * pago_por_hora

#Se calcula descuento del 20%
descuento = sueldo_bruto * 0.20

#Se calcula sueldo neto
sueldo_neto = sueldo_bruto - descuento

#Resultado final
print(f"Sueldo bruto: {sueldo_bruto:.2f} COP")
print(f"Descuento por impuestos (20%): {descuento:.2f} COP")
print(f"Sueldo neto: {sueldo_neto:.2f} COP")
