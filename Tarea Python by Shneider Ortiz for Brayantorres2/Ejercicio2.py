#Solicitar capital
capital=float(input( "Ingresar capital que se invierte: "))
#Calcular interes y monta final
interes = capital * 0.02
monto_final = capital + interes
#Resultado
print(f"El interes ganado en un mes quivale a: {interes:.2f} COP")
print(f"El monto final despues de un mes será: {monto_final:.2f} COP")