#Ingresar datos al usuario
nombre = input("Ingrese el nombre del trabajador: ")
horas_normales = float(input("Ingrese el número de horas normales trabajadas: "))
pago_hora = float(input("Ingrese el pago por hora normal: "))
horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
num_hijos = int(input("Ingrese el número de hijos: "))

#se hace el calculo del sueldo base (solo horas normales)
sueldo_base = horas_normales * pago_hora

#se hace calculo del sueldo por horas extras (25% más del pago normal)
pago_hora_extra = pago_hora * 1.25
sueldo_extras = horas_extras * pago_hora_extra

#Se calcula el sueldo bruto (sueldo base + extras)
sueldo_bruto = sueldo_base + sueldo_extras

#Se calcula de deducciones (5% pago forzoso, 2% política habitacional, 7% caja de ahorro)
deducciones = sueldo_base * (0.05 + 0.02 + 0.07)

#Se calcula  Cálculo de asignaciones
asignacion_actualizacion = 250000
asignacion_hijos = num_hijos * 173000
asignacion_hogar = 180000
asignaciones = asignacion_actualizacion + asignacion_hijos + asignacion_hogar

#Se calcula  Cálculo del sueldo neto
sueldo_neto = sueldo_bruto + asignaciones - deducciones

# Mostrar resultados
print("\n---- Resumen del salario ----")
print(f"Nombre del trabajador: {nombre}")
print(f"Sueldo base: {sueldo_base:.2f} COP")
print(f"Sueldo por horas extras: {sueldo_extras:.2f} COP")
print(f"Total deducciones: {deducciones:.2f} COP")
print(f"Total asignaciones: {asignaciones:.2f} COP")
print(f"Sueldo neto final: {sueldo_neto:.2f} COP")
